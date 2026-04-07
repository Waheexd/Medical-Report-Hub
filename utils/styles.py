import streamlit as st

def apply_custom_styles():
    """
    Inject custom CSS for a professional medical-grade UI.
    Focuses on layout, chat bubbles, and Metric Cards.
    """
    st.markdown("""
        <style>
        /* Main Layout Adjustments */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        /* Metric Card Styling */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem;
            font-weight: 700;
            color: #00d4ff;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 1.1rem;
            color: #9abed1;
        }

        /* Custom Card Container */
        .st-emotion-cache-1r68d9w {
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 1.5rem;
            background-color: #111827;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background-color: transparent;
        }

        .stTabs [data-baseweb="tab"] {
            height: 45px;
            white-space: pre-wrap;
            background-color: #1f2937;
            border-radius: 8px;
            color: white;
            padding: 0 20px;
            border: none;
        }

        .stTabs [aria-selected="true"] {
            background-color: #3b82f6 !important;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        }

        /* Chat UI Refinements */
        .stChatMessage {
            background-color: #1f2937 !important;
            border-radius: 15px !important;
            border: 1px solid #374151 !important;
            margin-bottom: 1rem !important;
        }

        /* Fixed Footer/Input Area Spacing */
        .stChatInputContainer {
            padding-bottom: 2rem;
        }

        /* Success/Warning/Info Boxes */
        .stAlert {
            border-radius: 10px;
            border: none;
        }

        /* Download & Primary Button Styling */
        .stDownloadButton button, .stButton > button[kind="primary"] {
            width: 100%;
            background-color: #2563eb !important;
            color: white !important;
            border: 1px solid #3b82f6 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease;
        }

        .stDownloadButton button:hover, .stButton > button[kind="primary"]:hover {
            background-color: #1d4ed8 !important;
            border-color: #2563eb !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }

        /* Secondary/Reset Button Styling */
        .stButton > button[kind="secondary"] {
            width: 100%;
            background-color: #374151 !important;
            color: #d1d5db !important;
            border: 1px solid #4b5563 !important;
            border-radius: 8px !important;
        }

        .stButton > button[kind="secondary"]:hover {
            background-color: #4b5563 !important;
            color: white !important;
            border-color: #6b7280 !important;
        }
        </style>
    """, unsafe_allow_html=True)
