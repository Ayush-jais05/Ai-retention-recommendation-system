import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Movie Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =========================
# PREMIUM CALM UI 🌙
# =========================
st.markdown("""
<style>

/* Background (soft dark gradient) */
.main {
    background: linear-gradient(135deg, #020617, #0f172a, #020617);
    color: #e5e7eb;
}

/* Hero Title */
.hero-title {
    font-size: 60px;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #38bdf8;  /* soft cyan */
}

/* Subtitle */
.subtext {
    color: #94a3b8;
    font-size: 17px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.04);
    padding: 28px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.06);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(56,189,248,0.15);
    border: 1px solid rgba(56,189,248,0.3);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #0ea5e9, #22c55e);
    color: white;
    font-size: 15px;
    padding: 12px;
    border: none;
    transition: all 0.25s ease;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 10px rgba(56,189,248,0.4);
}

/* Divider */
hr {
    border: 0.5px solid rgba(255,255,255,0.08);
}

/* Section spacing */
.section {
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO SECTION 🔥
# =========================
st.markdown("""
<div style='text-align:center; padding:80px 20px'>
    <div class='hero-title'>🎬 AI Movie Intelligence</div>
    <p class='subtext'>
        Production-grade ML system for recommendation, churn prediction & user analytics
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# CORE MODULES
# =========================
st.markdown("## 🚀 Core Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🎬 Recommendation Engine</h3>
        <p class='subtext'>
        KNN-based collaborative filtering optimized for large-scale movie data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Recommendations"):
        st.switch_page("pages/3_Recommendations.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>📉 Churn Intelligence</h3>
        <p class='subtext'>
        Predict user retention risk using behavioral ML models.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Churn Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Analytics System</h3>
        <p class='subtext'>
        Segmentation, cohort analysis, and engagement insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Analytics"):
        st.switch_page("pages/2_Analytics.py")

st.markdown("---")

# =========================
# SYSTEM CAPABILITIES
# =========================
st.markdown("## ⚡ System Capabilities")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📉 Churn Prediction</h4>
        <p class='subtext'>Behavior-driven ML classification</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🎯 Personalization</h4>
        <p class='subtext'>Collaborative filtering recommendations</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>👥 User Segmentation</h4>
        <p class='subtext'>Clustering-based grouping</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h4>💡 Strategy Engine</h4>
        <p class='subtext'>Actionable retention insights</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# SYSTEM FLOW
# =========================
st.markdown("## 🧠 System Flow")

st.markdown("""
<div class="card">

1️⃣ User behavior data is collected  
<br><br>
2️⃣ Feature engineering creates engagement signals  
<br><br>
3️⃣ ML model predicts churn probability  
<br><br>
4️⃣ Recommendation engine suggests content  
<br><br>
5️⃣ Analytics layer generates insights & strategies  

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# FINAL CTA
# =========================
st.markdown("""
<div class="card" style="text-align:center">
    <h3>🚀 Explore the Platform</h3>
    <p class='subtext'>
    Navigate through modules to experience ML-powered recommendations and analytics.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888;'>Built by Ayush Raj</p>",
    unsafe_allow_html=True
)
