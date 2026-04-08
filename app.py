import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from rag.pipeline import MedicalRAGPipeline
from utils.pdf_generator import generate_medical_summary_pdf
from utils.normal_ranges import STATUS_ICONS, NORMAL_RANGES
from utils.styles import apply_custom_styles

load_dotenv()

# Streamlit App Config
st.set_page_config(page_title="Medical Report Hub", layout="wide", page_icon="🩺")

# Initialize session state variables
if "pipeline" not in st.session_state:
    st.session_state.pipeline = MedicalRAGPipeline()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_summary" not in st.session_state:
    st.session_state.current_summary = ""
if "current_glossary" not in st.session_state:
    st.session_state.current_glossary = ""

pipeline = st.session_state.pipeline

# Apply Professional CSS Styles
apply_custom_styles()

# Header Section
st.title("🩺 Medical Report Hub")
st.caption("Advanced AI Analysis for Laboratory Reports • Powered by Groq Llama-3")

# 1. Top Control Bar (Unified Header)
with st.container():
    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
    with c1:
        uploaded_file = st.file_uploader("Upload Lab Report (PDF)", type="pdf", label_visibility="collapsed")
    with c2:
        if uploaded_file is not None:
            if st.button("🚀 Analyze Report", use_container_width=True, type="primary"):
                with st.spinner("Processing..."):
                    os.makedirs("data", exist_ok=True)
                    temp_path = f"data/{uploaded_file.name}"
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    try:
                        pipeline.process_new_report(temp_path)
                        st.session_state.report_loaded = True
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    with c3:
        language = st.selectbox("Language", ["English", "Hindi"], label_visibility="collapsed")
    with c4:
        if st.button("♻️ Reset App", use_container_width=True, type="secondary"):
            st.session_state.report_loaded = False
            st.session_state.messages = []
            st.session_state.current_summary = ""
            st.session_state.current_glossary = ""
            st.rerun()

# Disclaimer
st.warning("⚠️ **Clinical Disclaimer:** This tool is for educational purposes only and does NOT provide medical advice. Consult a healthcare provider for diagnosis.")

# Main Dashboard Navigation
if "report_loaded" in st.session_state and st.session_state.report_loaded:
    tab1, tab2, tab3 = st.tabs(["📊 Results Dashboard", "💬 AI Assistant", "📖 Medical Glossary"])
    
    results = pipeline.extracted_results
    
    # --- TAB 1: RESULTS DASHBOARD ---
    with tab1:
        if results:
            # Metric Card Section
            st.subheader("🧪 Key Indicators")
            g1, g2, g3, g4 = st.columns(4)
            
            gauge_tests = ["Glucose", "Total Cholesterol", "Hemoglobin", "Sodium"]
            cols = [g1, g2, g3, g4]
            
            for test_name, col in zip(gauge_tests, cols):
                match = next((r for r in results if r['test_name'] == test_name), None)
                with col:
                    if match:
                        val = match['value']
                        status = match['status']
                        st.metric(label=test_name, value=f"{val} {match['unit']}", delta=status, delta_color="inverse" if status=="High" else "normal")
                    else:
                        st.caption(f"{test_name}: Not Found")

            st.markdown("---")
            
            # Sectioned Results Table
            sections = {}
            for res in results:
                sec = NORMAL_RANGES.get(res['test_name'], {}).get('section', 'OTHER TESTS')
                if sec not in sections:
                    sections[sec] = []
                sections[sec].append(res)
                
            for sec_name, sec_results in sections.items():
                with st.expander(f"📋 {sec_name}", expanded=True):
                    df = pd.DataFrame(sec_results)
                    df['status_display'] = df['status'].apply(lambda x: f"{STATUS_ICONS.get(x, '')} {x}")
                    display_df = df[["test_name", "value", "unit", "min", "max", "status_display"]]
                    display_df.columns = ["Test Name", "Result", "Unit", "Min", "Max", "Status"]
                    
                    def highlight_status(val):
                        if "High" in str(val): return 'color: #ff4b4b; font-weight: bold'
                        if "Low" in str(val): return 'color: #3b82f6; font-weight: bold'
                        return 'color: #10b981'
                    
                    st.dataframe(display_df.style.map(highlight_status, subset=['Status']), use_container_width=True)
            
            # Summary & Download
            st.markdown("---")
            ca, cb = st.columns([3, 1])
            with ca:
                if st.button("✨ Auto-Generate AI Analysis", type="primary"):
                    with st.spinner(f"Generating summary in {language}..."):
                        summary, _ = pipeline.auto_analyze(language=language)
                        st.session_state.current_summary = summary
                        st.rerun()
                
                if st.session_state.current_summary:
                    st.info(f"### AI Insight ({language})")
                    st.write(st.session_state.current_summary)
            
            with cb:
                if st.session_state.current_summary:
                    pdf_buffer = generate_medical_summary_pdf(results, st.session_state.current_summary)
                    st.download_button("📥 Download PDF Report", pdf_buffer, file_name="Medical_Summary.pdf", mime="application/pdf")
        else:
            st.warning("No tabular lab data detected. Please use the AI Assistant tab to ask questions.")

    # --- TAB 2: AI ASSISTANT ---
    with tab2:
        c_a, c_b = st.columns([1, 4])
        with c_a:
            if st.button("🗑️ Clear All", use_container_width=True, type="secondary"):
                st.session_state.messages = []
                st.rerun()
        with c_b:
            st.subheader("💬 Patient-AI Consultation")
        
        # Chat container
        chat_container = st.container()
        
        # Display messages in pairs with deletion option
        with chat_container:
            # Group messages into user-assistant pairs
            msgs = st.session_state.messages
            for i in range(0, len(msgs), 2):
                user_msg = msgs[i]
                assistant_msg = msgs[i+1] if (i+1) < len(msgs) else None
                
                # Display User Message
                with st.chat_message("user"):
                    st.markdown(user_msg["content"])
                
                # Display Assistant Message (Delete button lives inside here)
                if assistant_msg:
                    with st.chat_message("assistant"):
                        st.markdown(assistant_msg["content"])
                        if "sources" in assistant_msg:
                            with st.expander("Reference Citations"):
                                for s in assistant_msg["sources"]: st.caption(s)
                        
                        # Compact Delete Button inside the bubble
                        c1, c2 = st.columns([10, 1])
                        with c2:
                            if st.button("🗑️", key=f"del_{i}", help="Delete this exchange", type="secondary"):
                                st.session_state.messages.pop(i) # pop user
                                if i < len(st.session_state.messages):
                                    st.session_state.messages.pop(i)
                                st.rerun()

        # New Input
        if user_query := st.chat_input("Ask about your report..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.spinner("Analyzing context..."):
                answer, sources = pipeline.answer_question(user_query, language=language)
                st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
            st.rerun()

    # --- TAB 3: MEDICAL GLOSSARY ---
    with tab3:
        st.subheader("📖 Personalized Glossary")
        st.write("Understand the medical terms found in your specific laboratory report.")
        
        if st.button("🔍 Create Glossary", type="primary"):
            with st.spinner("Compiling definitions..."):
                glossary, _ = pipeline.generate_glossary(language=language)
                st.session_state.current_glossary = glossary
                st.rerun()

        if st.session_state.current_glossary:
            st.markdown(st.session_state.current_glossary)
        else:
            st.info("Click the button above to define all terms found in this report.")

else:
    st.info("👋 **Welcome to Medical Report Hub.** Please upload your laboratory results (PDF) to begin.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed for educational purposes. Always consult a physician for medical diagnosis.</div>", unsafe_allow_html=True)
