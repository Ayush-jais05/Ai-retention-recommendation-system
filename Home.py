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
# NETFLIX STYLE UI 🔥
# =========================
st.markdown("""
<style>

/* Background (Netflix Red-Black Gradient) */
.main {
    background: linear-gradient(135deg, #000000, #0b0b0b, #1a0000);
    color: white;
}

/* Hero Title */
.hero-title {
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #e50914;
    text-shadow: 0 0 20px rgba(229, 9, 20, 0.4);
}

/* Subtitle */
.subtext {
    color: #b3b3b3;
    font-size: 18px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.04);
    padding: 28px;
    border-radius: 20px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 25px rgba(229, 9, 20, 0.3);
    border: 1px solid rgba(229, 9, 20, 0.4);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #e50914, #b20710);
    color: white;
    font-size: 15px;
    padding: 12px;
    border: none;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 15px rgba(229, 9, 20, 0.6);
}

/* Section spacing */
.section {
    margin-top: 30px;
}

/* Divider */
hr {
    border: 0.5px solid rgba(255,255,255,0.1);
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
