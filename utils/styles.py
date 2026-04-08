import streamlit as st

def apply_custom_styles():
    """
    Inject custom CSS for a professional medical-grade UI.
    Fixed to the "Medical Light" theme with high-contrast chat bubbles.
    """
    # Theme Palette (Medical Light)
    bg_main = "#ffffff"          # White
    bg_card = "#ffffff"          # White
    bg_secondary = "#f8fafc"     # Light Slate
    border_col = "#e2e8f0"       # Light Gray
    text_primary = "#1e293b"     # Dark Slate
    text_secondary = "#64748b"   # Muted Slate
    metric_val = "#2563eb"       # Medical Blue
    chat_user = "#eff6ff"        # Light Blue
    chat_bot = "#f1f5f9"         # Light Gray (slightly more distinct)
    tab_bg = "#f8fafc"
    tab_active = "#ffffff"

    st.markdown(f"""
        <style>
        :root {{
            --bg-main: {bg_main};
            --bg-card: {bg_card};
            --bg-secondary: {bg_secondary};
            --border-col: {border_col};
            --text-primary: {text_primary};
            --text-secondary: {text_secondary};
            --metric-val: {metric_val};
            --chat-user: {chat_user};
            --chat-bot: {chat_bot};
            --tab-bg: {tab_bg};
            --tab-active: {tab_active};
        }}

        /* Main Layout Adjustments */
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 5rem;
            background-color: var(--bg-main) !important;
        }}

        /* Metric Card Styling */
        [data-testid="stMetricValue"] {{
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--metric-val) !important;
        }}
        
        [data-testid="stMetricLabel"] {{
            font-size: 1rem;
            color: var(--text-secondary) !important;
            font-weight: 500;
        }}

        /* Custom Card Container (Results / Expanders) */
        [data-testid="stExpander"] {{
            border: 1px solid var(--border-col) !important;
            border-radius: 12px !important;
            background-color: var(--bg-card) !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
            margin-bottom: 1rem !important;
        }}

        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 12px;
            background-color: transparent;
            border-bottom: 1px solid var(--border-col);
            padding-bottom: 4px;
        }}

        .stTabs [data-baseweb="tab"] {{
            height: 42px;
            white-space: pre-wrap;
            background-color: var(--tab-bg);
            border-radius: 8px 8px 0 0;
            color: var(--text-secondary);
            padding: 0 24px;
            border: 1px solid var(--border-col);
            border-bottom: none;
            font-weight: 500;
        }}

        .stTabs [aria-selected="true"] {{
            background-color: var(--tab-active) !important;
            color: var(--metric-val) !important;
            border-top: 2px solid var(--metric-val) !important;
            font-weight: 600 !important;
        }}

        /* --- AGGRESSIVE CHAT UI REFINEMENTS --- */
        .stChatMessage {{
            border-radius: 15px !important;
            border: 1px solid var(--border-col) !important;
            margin-bottom: 1.5rem !important;
            padding: 1.2rem !important;
        }}

        /* Force backgrounds for AI and User bubbles */
        [data-testid="stChatMessage"]:nth-child(even) {{
            background-color: var(--chat-bot) !important; 
        }}

        [data-testid="stChatMessage"]:nth-child(odd) {{
            background-color: var(--chat-user) !important;
            border-left: 4px solid var(--metric-val) !important;
        }}

        /* FORCE TEXT CONTRAST IN CHAT */
        .stChatMessage p, 
        .stChatMessage span, 
        .stChatMessage div, 
        .stChatMessage li, 
        .stChatMessage code {{
            color: var(--text-primary) !important;
        }}

        .stChatMessage h1, 
        .stChatMessage h2, 
        .stChatMessage h3 {{
            color: var(--metric-val) !important;
        }}

        /* Target expanders and nested cards INSIDE chat bubbles */
        .stChatMessage [data-testid="stExpander"] {{
            background-color: var(--bg-main) !important;
            border: 1px solid var(--border-col) !important;
        }}
        
        .stChatMessage [data-testid="stExpander"] * {{
            color: var(--text-primary) !important;
        }}

        /* Success/Warning/Info Boxes */
        .stAlert {{
            border-radius: 12px;
            border: 1px solid var(--border-col);
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            background-color: var(--bg-card) !important;
        }}

        /* Download & Primary Button Styling */
        .stDownloadButton button, .stButton > button[kind="primary"] {{
            width: 100%;
            background-color: #2563eb !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            padding: 0.6rem 1rem !important;
            transition: all 0.2s ease;
        }}

        .stDownloadButton button:hover, .stButton > button[kind="primary"]:hover {{
            background-color: #1d4ed8 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
            transform: translateY(-1px);
        }}

        /* Secondary/Reset Button Styling */
        .stButton > button[kind="secondary"] {{
            width: 100%;
            background-color: var(--bg-card) !important;
            color: var(--text-secondary) !important;
            border: 1px solid var(--border-col) !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
        }}

        .stButton > button[kind="secondary"]:hover {{
            background-color: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
            border-color: #cbd5e1 !important;
        }}

        /* Dataframe styling */
        .stDataFrame {{
            border: 1px solid var(--border-col);
            border-radius: 8px;
            background-color: var(--bg-card);
        }}

        /* Specifically target metric values division */
        [data-testid="stMetricValue"] > div {{
            color: var(--metric-val) !important;
        }}

        </style>
    """, unsafe_allow_html=True)
