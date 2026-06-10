"""
AI Multilingual Translator - Modern SaaS Application
A professional, feature-rich language translation tool powered by AI.
Built with Streamlit, Deep-Translator, and advanced UI/UX design.

Author: CodeAlpha AI Internship
Date: 2026
"""

import streamlit as st
from deep_translator import GoogleTranslator
from datetime import datetime
import pandas as pd
import io

# ======================== PAGE CONFIGURATION ========================
st.set_page_config(
    page_title="AI Multilingual Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ======================== PREMIUM CUSTOM CSS STYLING ========================
custom_css = """
<style>
    /* ---- GLOBAL STYLING ---- */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body {
        background: linear-gradient(135deg, #0f172a 0%, #1a2847 100%);
        color: #1a1a1a;
    }

    /* ---- MAIN CONTAINER ---- */
    .main {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
        padding: 0;
    }

    /* ======================== HERO SECTION ======================== */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-attachment: fixed;
        padding: 3.5rem 2rem;
        border-radius: 0;
        color: white;
        text-align: center;
        margin-bottom: 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.2), transparent 50%);
        pointer-events: none;
    }

    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 800px;
        margin: 0 auto;
    }

    .hero-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 1rem;
        text-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        opacity: 0.98;
        font-weight: 300;
        letter-spacing: 0.3px;
        line-height: 1.6;
        margin-bottom: 0;
    }

    /* ======================== CARD STYLES (GLASSMORPHISM) ======================== */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 40px rgba(31, 38, 135, 0.25);
        border-color: rgba(102, 126, 234, 0.4);
    }

    /* ======================== TRANSLATOR PANEL ======================== */
    .translator-panel {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9));
        backdrop-filter: blur(10px);
        border: 1.5px solid rgba(102, 126, 234, 0.2);
        padding: 2.5rem;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(31, 38, 135, 0.1);
        margin-bottom: 2rem;
        margin-top: -1.5rem;
    }

    /* ======================== INPUT/OUTPUT STYLING ======================== */
    .stTextArea > div > div > textarea {
        border-radius: 14px !important;
        border: 2px solid #e2e8f0 !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        transition: all 0.3s ease !important;
        background: white !important;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.15) !important;
        background: #f8fafc !important;
    }

    /* Ensure textarea text is dark/visible */
    .stTextArea > div > div > textarea,
    .stTextArea textarea,
    div[data-testid="stTextArea"] textarea,
    div[role="textbox"] {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* Ensure disabled textarea text is also dark */
    .stTextArea > div > div > textarea:disabled,
    .stTextArea textarea:disabled,
    div[data-testid="stTextArea"] textarea:disabled,
    div[role="textbox"]:disabled {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    .stTextArea label {
        font-weight: 700 !important;
        color: #1a1a1a !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ======================== SELECTBOX STYLING ======================== */
    .stSelectbox > div > div {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        background: white !important;
    }

    .stSelectbox label {
        font-weight: 700 !important;
        color: #1a1a1a !important;
        font-size: 0.95rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ======================== BUTTON STYLING ======================== */
    .stButton > button {
        width: 100%;
        padding: 0.85rem 1.5rem !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ======================== METRIC CARDS ======================== */
    .metric-container {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1));
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(102, 126, 234, 0.2);
        text-align: center;
        transition: all 0.3s ease;
    }

    .metric-container:hover {
        transform: translateY(-3px);
        border-color: rgba(102, 126, 234, 0.4);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.15);
    }

    .metric-value {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }

    .metric-label {
        color: #64748b;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    /* ======================== MESSAGES ======================== */
    .success-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46;
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #10b981;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }

    .error-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        color: #7f1d1d;
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #ef4444;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }

    .warning-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        color: #78350f;
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #f59e0b;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }

    /* ======================== SECTION TITLES ======================== */
    .section-title {
        font-size: 1.8rem;
        font-weight: 900;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
        margin-top: 2.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }

    .section-subtitle {
        font-size: 0.95rem;
        color: #64748b;
        margin-bottom: 1.5rem;
        font-weight: 500;
    }

    /* ======================== LANGUAGE CARDS ======================== */
    .language-card {
        background: linear-gradient(135deg, white, #f8fafc);
        padding: 1rem;
        border-radius: 12px;
        border: 1.5px solid #e2e8f0;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .language-card:hover {
        transform: translateY(-4px);
        border-color: #667eea;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.15);
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    }

    .language-name {
        font-weight: 700;
        color: #1a1a1a;
        font-size: 0.9rem;
    }

    /* ======================== FEATURE CARDS ======================== */
    .feature-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(240, 147, 251, 0.05));
        padding: 2rem;
        border-radius: 16px;
        border: 1.5px solid rgba(102, 126, 234, 0.2);
        text-align: center;
        transition: all 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-8px);
        border-color: #667eea;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }

    .feature-desc {
        font-size: 0.9rem;
        color: #64748b;
        line-height: 1.6;
    }

    /* ======================== TABLE STYLING ======================== */
    .stDataFrame {
        border-radius: 12px !important;
    }

    /* ======================== FOOTER ======================== */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        text-align: center;
        margin-top: 3rem;
        border-radius: 0;
    }

    .footer-title {
        font-size: 1.3rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }

    .footer-text {
        font-size: 0.95rem;
        opacity: 0.95;
        line-height: 1.8;
        margin-bottom: 1rem;
    }

    .footer-credit {
        font-size: 0.85rem;
        opacity: 0.85;
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* ======================== DIVIDER ======================== */
    .divider {
        height: 1.5px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }

    /* ======================== RESPONSIVE DESIGN ======================== */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 1.8rem;
        }

        .hero-subtitle {
            font-size: 1rem;
        }

        .hero-icon {
            font-size: 3rem;
        }

        .section-title {
            font-size: 1.4rem;
        }

        .translator-panel {
            padding: 1.5rem;
        }
    }

    /* ======================== LOADING ANIMATION ======================== */
    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    .spinner {
        animation: spin 1s linear infinite;
        display: inline-block;
    }

    /* ======================== SMOOTH TRANSITIONS ======================== */
    .smooth-transition {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ======================== PLACEHOLDER & INPUT TEXT STYLING ======================== */
    /* Textarea placeholder text */
    .stTextArea > div > div > textarea::placeholder {
        color: #a8adc4 !important;
        opacity: 0.7 !important;
    }

    /* Input text color */
    .stTextArea > div > div > textarea,
    .stTextArea textarea,
    div[data-testid="stTextArea"] textarea,
    div[role="textbox"],
    .stTextArea [role="textbox"],
    .stTextArea [contenteditable="true"] {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        opacity: 1 !important;
        visibility: visible !important;
        background-color: #ffffff !important;
    }

    /* Selectbox text color */
    .stSelectbox > div > div > div {
        color: #1a1a1a !important;
    }

    /* Selectbox input text */
    .stSelectbox input {
        color: #1a1a1a !important;
    }

    /* Selectbox placeholder */
    .stSelectbox input::placeholder {
        color: #a8adc4 !important;
        opacity: 0.7 !important;
    }

    /* Selectbox option text */
    .stSelectbox [data-baseweb="select"] {
        color: #1a1a1a !important;
    }

    /* Labels - make them white for better visibility */
    .stTextArea > label,
    .stSelectbox > label,
    .stNumberInput > label,
    .stSlider > label {
        color: white !important;
        font-weight: 700 !important;
    }

    /* Ensure text in all input-like elements is visible */
    input[type="text"],
    input[type="email"],
    input[type="password"],
    textarea {
        color: #1a1a1a !important;
    }

    /* Disabled and output textarea text should be fully visible */
    textarea:disabled,
    textarea[disabled],
    .stTextArea textarea:disabled,
    .stTextArea textarea[disabled],
    .stTextArea > div > div > textarea:disabled,
    .stTextArea > div > div > textarea[disabled],
    div[data-testid="stTextArea"] textarea:disabled,
    div[data-testid="stTextArea"] textarea[disabled],
    div[role="textbox"]:disabled,
    .stTextArea [role="textbox"]:disabled,
    .stTextArea [contenteditable="true"]:disabled {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        opacity: 1 !important;
        visibility: visible !important;
        background-color: #ffffff !important;
    }

    /* Placeholder styling for all inputs */
    input::placeholder,
    textarea::placeholder {
        color: #a8adc4 !important;
        opacity: 0.7 !important;
    }

    /* Dark mode support - ensure selectbox text is readable */
    .stSelectbox [role="button"] {
        color: #1a1a1a !important;
    }

    /* Ensure dropdown menu items are readable */
    [data-baseweb="menu"] {
        color: #1a1a1a !important;
    }

    [data-baseweb="menu"] li {
        color: #1a1a1a !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ======================== LANGUAGE DICTIONARY (35+ Languages) ========================
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Bengali": "bn",
    "Telugu": "te",
    "Tamil": "ta",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Polish": "pl",
    "Dutch": "nl",
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Finnish": "fi",
    "Greek": "el",
    "Turkish": "tr",
    "Arabic": "ar",
    "Hebrew": "he",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "fil",
    "Afrikaans": "af",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Slovak": "sk",
    "Ukrainian": "uk",
}

# ======================== SESSION STATE INITIALIZATION ========================
if "translation_history" not in st.session_state:
    st.session_state.translation_history = []

if "total_characters" not in st.session_state:
    st.session_state.total_characters = 0

if "total_words" not in st.session_state:
    st.session_state.total_words = 0

if "languages_used" not in st.session_state:
    st.session_state.languages_used = set()

# ======================== UTILITY FUNCTIONS ========================
def save_translation_history(source_lang, target_lang, input_text, output_text):
    """Save translation to history with timestamp."""
    translation_record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_language": source_lang,
        "target_language": target_lang,
        "input_text": input_text,
        "output_text": output_text,
        "char_count": len(input_text),
        "word_count": len(input_text.split()),
    }
    st.session_state.translation_history.append(translation_record)
    
    # Update statistics
    st.session_state.total_characters += len(input_text)
    st.session_state.total_words += len(input_text.split())
    st.session_state.languages_used.add(source_lang)
    st.session_state.languages_used.add(target_lang)
    
    # Keep only last 50 translations in memory
    if len(st.session_state.translation_history) > 50:
        st.session_state.translation_history.pop(0)


def detect_language(text):
    """Auto-detect language of input text."""
    try:
        detected = GoogleTranslator(source="auto", target="en").detect(text)
        return detected if detected else "en"
    except:
        return "Unknown"


def count_words(text):
    """Count words in text."""
    return len(text.split()) if text.strip() else 0


def count_characters(text):
    """Count characters (excluding spaces) in text."""
    return len(text.replace(" ", ""))


def get_csv_download(history):
    """Generate CSV data from translation history."""
    df = pd.DataFrame(history)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()


# ======================== PREMIUM HERO SECTION ========================
st.markdown(
    """
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-icon">🌍</div>
            <h1 class="hero-title">AI Multilingual Translator</h1>
            <p class="hero-subtitle">
                Translate across 35+ languages instantly using AI-powered language processing
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================== MAIN TRANSLATOR SECTION ========================
st.markdown(
    '<div class="translator-panel">',
    unsafe_allow_html=True
)

# Language Selection Row
col_lang1, col_lang2, col_swap = st.columns([1, 1, 0.5])

with col_lang1:
    source_language = st.selectbox(
        "📤 Source Language",
        options=list(LANGUAGES.keys()),
        index=0,
        key="source_lang"
    )

with col_lang2:
    target_language = st.selectbox(
        "📥 Target Language",
        options=list(LANGUAGES.keys()),
        index=1,
        key="target_lang"
    )

with col_swap:
    if st.button("⇄ Swap", help="Swap source and target languages", use_container_width=True):
        temp_source = st.session_state.source_lang
        temp_target = st.session_state.target_lang
        st.session_state.source_lang = temp_target
        st.session_state.target_lang = temp_source
        st.rerun()

# Input Text Area
input_text = st.text_area(
    "✍️ Enter Text to Translate",
    placeholder="Type or paste your text here...",
    height=180,
    key="input_text"
)

# Character and Word Count Display
if input_text:
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    
    with col_stat1:
        st.markdown(
            f"""
            <div class="metric-container">
                <div class="metric-value">{count_characters(input_text)}</div>
                <div class="metric-label">Characters</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col_stat2:
        st.markdown(
            f"""
            <div class="metric-container">
                <div class="metric-value">{count_words(input_text)}</div>
                <div class="metric-label">Words</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col_stat3:
        detected_lang = detect_language(input_text)
        st.markdown(
            f"""
            <div class="metric-container">
                <div class="metric-value">{detected_lang}</div>
                <div class="metric-label">Detected</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Action Buttons
button_col1, button_col2, button_col3 = st.columns([1, 1, 1])

with button_col1:
    translate_button = st.button("🚀 Translate", use_container_width=True, key="translate_btn")

with button_col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True, key="clear_btn")

with button_col3:
    st.write("")  # Placeholder for alignment

if clear_button:
    st.session_state.input_text = ""
    st.rerun()

# ======================== TRANSLATION LOGIC ========================
translated_text = None

if translate_button:
    if not input_text.strip():
        st.markdown(
            """
            <div class="warning-box">
                ⚠️ <strong>Empty Input!</strong> Please enter some text to translate.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        try:
            with st.spinner("🔄 Translating your text using AI... "):
                translator = GoogleTranslator(
                    source=LANGUAGES[source_language],
                    target=LANGUAGES[target_language]
                )
                translated_text = translator.translate(input_text)

            # Save to history
            save_translation_history(
                source_language,
                target_language,
                input_text,
                translated_text
            )
            
            # Success message
            st.markdown(
                """
                <div class="success-box">
                    ✅ <strong>Translation Complete!</strong> Your text has been successfully translated.
                </div>
                """,
                unsafe_allow_html=True
            )

            # DEBUG: confirm translation variable value
            st.write("DEBUG:", translated_text)
            
            # Output Text Area
            st.text_area(
                "📤 Translated Text",
                value=translated_text,
                height=180,
                disabled=True,
                key="output_text"
            )
            
            # Output Action Buttons
            out_col1, out_col2, out_col3, out_col4 = st.columns(4)
            
            with out_col1:
                if st.button("📋 Copy", use_container_width=True, key="copy_btn"):
                    st.info("✅ Text copied! Ready to paste anywhere.")
            
            with out_col2:
                csv_data = get_csv_download([{
                    "Source": source_language,
                    "Target": target_language,
                    "Input": input_text[:100],
                    "Output": translated_text[:100],
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }])
                st.download_button(
                    label="📥 Download",
                    data=translated_text.encode("utf-8"),
                    file_name=f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with out_col3:
                if st.button("🔄 Reverse", use_container_width=True, key="reverse_btn"):
                    st.session_state.source_lang = st.session_state.target_lang
                    st.session_state.target_lang = 0  # Reset to English
                    st.session_state.input_text = translated_text
                    st.rerun()
        
        except Exception as e:
            st.markdown(
                f"""
                <div class="error-box">
                    ❌ <strong>Translation Error!</strong> {str(e)}
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown('</div>', unsafe_allow_html=True)

# ======================== STATISTICS DASHBOARD ========================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<h2 class="section-title">📊 Statistics Dashboard</h2>',
    unsafe_allow_html=True
)

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.markdown(
        f"""
        <div class="metric-container">
            <div class="metric-value">{len(st.session_state.translation_history)}</div>
            <div class="metric-label">Total Translations</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat_col2:
    st.markdown(
        f"""
        <div class="metric-container">
            <div class="metric-value">{st.session_state.total_characters:,}</div>
            <div class="metric-label">Characters Translated</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat_col3:
    st.markdown(
        f"""
        <div class="metric-container">
            <div class="metric-value">{st.session_state.total_words:,}</div>
            <div class="metric-label">Words Translated</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat_col4:
    st.markdown(
        f"""
        <div class="metric-container">
            <div class="metric-value">{len(st.session_state.languages_used)}</div>
            <div class="metric-label">Languages Used</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================== RECENT TRANSLATION HISTORY ========================
if st.session_state.translation_history:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown(
        '<h2 class="section-title">📜 Recent Translation History</h2>',
        unsafe_allow_html=True
    )
    
    # Display history as table
    history_data = []
    for record in reversed(st.session_state.translation_history[-15:]):
        history_data.append({
            "🕐 Time": record["timestamp"],
            "🔤 From": record["source_language"],
            "🎯 To": record["target_language"],
            "📊 Length": f"{record['char_count']} chars",
            "📝 Preview": record["input_text"][:40] + "..." if len(record["input_text"]) > 40 else record["input_text"],
        })
    
    if history_data:
        st.dataframe(
            history_data,
            use_container_width=True,
            hide_index=True
        )
    
    # Download and Clear Buttons
    hist_col1, hist_col2, hist_col3 = st.columns([1, 1, 2])
    
    with hist_col1:
        if st.button("📥 Download History (CSV)", use_container_width=True):
            csv_data = get_csv_download(st.session_state.translation_history)
            st.download_button(
                label="📥 Download CSV",
                data=csv_data,
                file_name=f"translation_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    with hist_col2:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.translation_history = []
            st.session_state.total_characters = 0
            st.session_state.total_words = 0
            st.session_state.languages_used = set()
            st.rerun()

# ======================== SUPPORTED LANGUAGES SECTION ========================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<h2 class="section-title">🌐 Supported Languages (35+)</h2>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="section-subtitle">Seamlessly translate between any of these languages</p>',
    unsafe_allow_html=True
)

# Display languages in grid
lang_cols = st.columns(7)
for i, lang_name in enumerate(list(LANGUAGES.keys())):
    with lang_cols[i % 7]:
        st.markdown(
            f"""
            <div class="language-card">
                <div class="language-name">{lang_name}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ======================== FEATURES SECTION ========================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<h2 class="section-title">✨ Why Choose Our Translator?</h2>',
    unsafe_allow_html=True
)

feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)

with feat_col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-desc">Get instant translations powered by cutting-edge AI</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feat_col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🌍</div>
            <div class="feature-title">Multi-Language</div>
            <div class="feature-desc">Support for 35+ languages worldwide</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feat_col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Powered</div>
            <div class="feature-desc">Advanced neural machine translation</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feat_col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Secure & Private</div>
            <div class="feature-desc">Your data is processed securely</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================== PROFESSIONAL FOOTER ========================
st.markdown(
    """
    <div class="footer">
        <div class="footer-title">🌍 AI Multilingual Translator</div>
        <div class="footer-text">
            <strong>Developed by:</strong> Lumbini Devi<br>
            B.Tech CSE Student | AI & UPSC Aspirant<br><br>
            <strong>Project Type:</strong> CodeAlpha Artificial Intelligence Internship Project
        </div>
        <div class="footer-credit">
            Powered by Deep-Translator & Google Translate API | Built with Streamlit | © 2026 All Rights Reserved
        </div>
    </div>
    """,
    unsafe_allow_html=True
)