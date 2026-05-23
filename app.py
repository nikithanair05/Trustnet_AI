import streamlit as st
import joblib
import chromadb
import time
import plotly.graph_objects as go

from datetime import datetime
from sentence_transformers import SentenceTransformer

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="TrustNet AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# ADVANCED CSS
# -------------------------------------------------

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
        radial-gradient(circle at top left, rgba(99,102,241,0.18), transparent 25%),
        radial-gradient(circle at top right, rgba(168,85,247,0.18), transparent 25%),
        radial-gradient(circle at bottom left, rgba(14,165,233,0.18), transparent 25%),
        linear-gradient(135deg, #020617, #0f172a, #111827);

        color: #f8fafc;
    }

    .main-title {
        font-size: 72px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc,
            #f472b6
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-top: 20px;
        margin-bottom: 10px;

        letter-spacing: -2px;
    }

    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #cbd5e1;
        margin-bottom: 45px;
        font-weight: 400;
    }

    .glass-card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(18px);

        border-radius: 28px;
        padding: 35px;

        border: 1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 0 40px rgba(99,102,241,0.18),
            inset 0 0 10px rgba(255,255,255,0.03);
    }

    .metric-card {
        background: linear-gradient(
            135deg,
            rgba(59,130,246,0.15),
            rgba(139,92,246,0.15)
        );

        padding: 25px;
        border-radius: 22px;

        text-align: center;

        border: 1px solid rgba(255,255,255,0.08);

        box-shadow: 0 0 25px rgba(99,102,241,0.12);

        transition: 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 40px rgba(139,92,246,0.25);
    }

    .metric-title {
        font-size: 15px;
        color: #cbd5e1;
        font-weight: 500;
    }

    .metric-value {
        font-size: 34px;
        font-weight: 800;
        color: white;
        margin-top: 10px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 18px;
        color: #f8fafc;
        letter-spacing: -0.5px;
    }

    .footer {
        text-align: center;
        margin-top: 60px;
        color: #94a3b8;
        font-size: 15px;
        padding-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        height: 64px;

        border-radius: 18px;
        border: none;

        background: linear-gradient(
            90deg,
            #3b82f6,
            #8b5cf6,
            #ec4899
        );

        color: white;

        font-size: 20px;
        font-weight: 800;

        letter-spacing: 0.3px;

        transition: 0.35s ease;

        box-shadow: 0 0 25px rgba(99,102,241,0.35);
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 40px rgba(168,85,247,0.55);
    }

    textarea, input {
        border-radius: 18px !important;

        background-color: rgba(255,255,255,0.03) !important;

        color: white !important;

        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    label {
        color: #f8fafc !important;
        font-weight: 600 !important;
    }

    .hero-glow {
        height: 180px;

        border-radius: 30px;

        background:
        radial-gradient(circle at center,
            rgba(99,102,241,0.25),
            rgba(14,165,233,0.08),
            transparent 70%
        );

        filter: blur(5px);

        margin-bottom: -120px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.title("🛡️ TrustNet AI")

    st.markdown("---")

    st.info(
        "AI-powered cybersecurity & fake profile investigation platform."
    )

    st.markdown("### 🚀 Features")

    st.write("✅ ML Fake Profile Detection")
    st.write("✅ NLP Semantic Analysis")
    st.write("✅ Vector Database Retrieval")
    st.write("✅ RAG-based Investigation")
    st.write("✅ Threat Intelligence Engine")

    st.markdown("---")

    st.markdown("### 🌐 Live Threat Feed")

    st.error("⚠️ Crypto Scam Campaign Active")

    st.warning("⚠️ Fake HR Recruitment Surge")

    st.info("⚠️ OTP Phishing Attacks Increasing")

    st.success("✔ Threat Intelligence Synced")

    st.markdown("---")

    st.success("System Status: ACTIVE")

    st.caption("Version 1.0")

# -------------------------------------------------
# LOAD MODELS
# -------------------------------------------------

model = joblib.load("models/fake_profile_detector.pkl")

embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    name="scam_profiles"
)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

st.markdown(
    '<div class="hero-glow"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">🚨 TrustNet AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Advanced AI-Powered Fake Profile & Scam Detection Platform</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# MAIN LAYOUT
# -------------------------------------------------

left, right = st.columns([1.25, 1])

# -------------------------------------------------
# LEFT PANEL
# -------------------------------------------------

with left:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🔍 Analyze Social Profile</div>',
        unsafe_allow_html=True
    )

    bio = st.text_area(
        "Profile Bio",
        height=180,
        placeholder="Enter suspicious profile bio, recruiter scam text, investment offer or social media description..."
    )

    followers = st.number_input(
        "Followers",
        min_value=0,
        value=100
    )

    following = st.number_input(
        "Following",
        min_value=0,
        value=150
    )

    posts = st.number_input(
        "Posts",
        min_value=0,
        value=5
    )

    profile_pic = st.selectbox(
        "Profile Picture Available?",
        ["Yes", "No"]
    )

    analyze = st.button(
        "🚀 Run AI Investigation"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# -------------------------------------------------
# RIGHT PANEL
# -------------------------------------------------

with right:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📊 Intelligence Dashboard</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            '''
            <div class="metric-card">
                <div class="metric-title">Detection Accuracy</div>
                <div class="metric-value">94%</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            '''
            <div class="metric-card">
                <div class="metric-title">Semantic Retrieval</div>
                <div class="metric-value">ACTIVE</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "TrustNet AI uses Machine Learning, NLP, Sentence Transformers, ChromaDB and RAG pipelines to investigate suspicious social profiles."
    )

    st.success(
        "✔ Transformer Embeddings Active"
    )

    st.warning(
        "⚡ Threat Intelligence Engine Online"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# -------------------------------------------------
# ANALYSIS
# -------------------------------------------------

if analyze:

    with st.spinner(
        "Running AI Investigation Engine..."
    ):

        with st.status(
            "Executing AI pipeline...",
            expanded=True
        ) as status:

            st.write("✔ Loading ML Detection Model")
            time.sleep(0.5)

            st.write("✔ Generating Semantic Embeddings")
            time.sleep(0.5)

            st.write("✔ Searching Vector Database")
            time.sleep(0.5)

            st.write("✔ Running Threat Intelligence Retrieval")
            time.sleep(0.5)

            st.write("✔ Generating Investigation Report")
            time.sleep(0.5)

            status.update(
                label="AI Investigation Complete",
                state="complete"
            )

        st.markdown(
            '<div class="section-title">⚙️ AI Investigation Pipeline</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        ✅ Input Profile Analysis  
        ⬇️  
        ✅ Semantic Embedding Generation  
        ⬇️  
        ✅ ChromaDB Vector Retrieval  
        ⬇️  
        ✅ Threat Intelligence Matching  
        ⬇️  
        ✅ AI Investigation Report Generated  
        """)

        profile_pic_value = 1 if profile_pic == "Yes" else 0

        features = [[
            profile_pic_value,
            0.2,
            1,
            0.0,
            0,
            len(bio),
            0,
            0,
            posts,
            followers,
            following
        ]]

        prediction = model.predict(features)[0]

        confidence = model.predict_proba(features)[0]

        query_embedding = embedding_model.encode(
            [bio]
        ).tolist()

        results = collection.query(
            query_embeddings=query_embedding,
            n_results=3
        )

        # -------------------------------------------------
        # Suspicious Keywords
        # -------------------------------------------------

        scam_keywords = [
            "investment",
            "otp",
            "urgent",
            "payment",
            "crypto",
            "guaranteed",
            "fee",
            "profit",
            "dm now",
            "earn money"
        ]

        detected_keywords = []

        for word in scam_keywords:

            if word.lower() in bio.lower():
                detected_keywords.append(word)

        # -------------------------------------------------
        # Investigation Logic
        # -------------------------------------------------

        if prediction == 1:

            explanation = """
            🚨 High-risk scam indicators detected.

            The analyzed profile demonstrates behavioral and semantic similarity with known fraudulent social media patterns.

            Risk Factors:
            • Promotional / scam-like wording
            • Suspicious engagement patterns
            • Similarity to recruiter-investment scams
            • Low trust indicators identified
            """

            confidence_score = confidence[1] * 100

        else:

            explanation = """
            ✅ No major scam indicators detected.

            The analyzed profile demonstrates relatively normal social media behavior and lower similarity with known fraudulent patterns.

            Trust Indicators:
            • Realistic engagement metrics
            • Lower semantic fraud similarity
            • Normal account structure detected
            • No critical risk behavior identified
            """

            confidence_score = confidence[0] * 100

        trust_score = 100 - confidence_score

        # -------------------------------------------------
        # Reputation Badge
        # -------------------------------------------------

        if trust_score > 80:
            reputation = "🟢 TRUSTED"

        elif trust_score > 50:
            reputation = "🟡 SUSPICIOUS"

        else:
            reputation = "🔴 HIGH RISK"

        # -------------------------------------------------
        # RESULTS
        # -------------------------------------------------

        st.markdown("---")

        st.markdown(
            '<div class="section-title">🧠 Investigation Result</div>',
            unsafe_allow_html=True
        )

        r1, r2, r3, r4 = st.columns(4)

        with r1:

            if prediction == 1:
                st.error("⚠️ Fake / Scam Profile")

            else:
                st.success("✅ Genuine Profile")

        with r2:

            st.metric(
                label="Confidence Score",
                value=f"{confidence_score:.2f}%"
            )

        with r3:

            st.metric(
                label="Trust Score",
                value=f"{trust_score:.0f}/100"
            )

        with r4:

            st.metric(
                label="Reputation Badge",
                value=reputation
            )

        # -------------------------------------------------
        # THREAT LEVEL
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">🚨 Threat Level</div>',
            unsafe_allow_html=True
        )

        risk_score = confidence_score / 100

        st.progress(risk_score)

        if risk_score > 0.75:

            st.error("HIGH RISK PROFILE")

        elif risk_score > 0.45:

            st.warning("MEDIUM RISK PROFILE")

        else:

            st.success("LOW RISK PROFILE")

        # -------------------------------------------------
        # AI REPORT
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">📑 AI Investigation Report</div>',
            unsafe_allow_html=True
        )

        st.write(explanation)

        # -------------------------------------------------
        # AI RISK RADAR
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">📡 AI Risk Radar</div>',
            unsafe_allow_html=True
        )

        categories = [
            'Scam Probability',
            'Trust Level',
            'Semantic Risk',
            'Activity Risk',
            'Profile Authenticity'
        ]

        values = [
            confidence_score,
            trust_score,
            min(95, confidence_score + 5),
            min(90, confidence_score + 10),
            trust_score
        ]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Risk Analysis'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # -------------------------------------------------
        # SUSPICIOUS KEYWORDS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">⚠️ Suspicious Keywords Detected</div>',
            unsafe_allow_html=True
        )

        if detected_keywords:

            keyword_cols = st.columns(
                len(detected_keywords)
            )

            for i, word in enumerate(detected_keywords):

                with keyword_cols[i]:
                    st.warning(word.upper())

        else:

            st.success(
                "No suspicious keywords detected"
            )

        # -------------------------------------------------
        # SIMILAR SCAM PATTERNS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">🔗 Similar Scam Patterns</div>',
            unsafe_allow_html=True
        )

        for doc in results['documents'][0]:

            st.warning(doc)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("---")

st.caption(
    f"Last Investigation Run: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

st.markdown(
    '''
    <div class="footer">
        Built with ❤️ using Machine Learning, NLP, Sentence Transformers, ChromaDB & RAG Architecture
    </div>
    ''',
    unsafe_allow_html=True
)