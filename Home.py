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
# PREMIUM UI (CLEAN + MODERN)
# =========================
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* Hero Title */
.hero-title {
    font-size: 60px;
    font-weight: 700;
}

/* Subtitle */
.subtext {
    color: #94a3b8;
    font-size: 18px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.06);
    padding: 28px;
    border-radius: 20px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.5);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    font-size: 15px;
    padding: 12px;
    border: none;
}

/* Section spacing */
.section {
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div style='text-align:center; padding:70px 20px'>
    <div class='hero-title'>AI Movie Intelligence</div>
    <p class='subtext'>
        Production-style ML system combining recommendation, churn prediction, and behavioral analytics
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# CORE MODULES (PRODUCT VIEW)
# =========================
st.markdown("## Core Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Recommendation Engine</h3>
        <p class='subtext'>
        KNN-based collaborative filtering on large-scale movie data with optimized deployment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Recommendations"):
        st.switch_page("pages/3_Recommendations.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>Churn Intelligence</h3>
        <p class='subtext'>
        Predict user retention risk using behavioral features and feature-engineered signals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Churn Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>Analytics System</h3>
        <p class='subtext'>
        User segmentation, cohort tracking, and engagement insights with interactive visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Analytics"):
        st.switch_page("pages/2_Analytics.py")

st.markdown("---")

# =========================
# SYSTEM CAPABILITIES
# =========================
st.markdown("## System Capabilities")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h4>Churn Prediction</h4>
        <p class='subtext'>Behavior-based ML classification</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>Personalization</h4>
        <p class='subtext'>Collaborative filtering recommendations</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>User Segmentation</h4>
        <p class='subtext'>Clustering-based grouping</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h4>Strategy Engine</h4>
        <p class='subtext'>Actionable retention insights</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# HOW SYSTEM WORKS
# =========================
st.markdown("## System Flow")

st.markdown("""
<div class="card">

1. User interaction data is collected and processed  
2. Feature engineering creates engagement signals  
3. ML models predict churn probability  
4. Recommendation engine suggests personalized content  
5. Analytics layer generates insights and strategies  

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# FINAL CTA
# =========================
st.markdown("""
<div class="card" style="text-align:center">
    <h3>Explore the full system</h3>
    <p class='subtext'>Navigate through modules to see predictions, recommendations, and analytics in action.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#94a3b8;'>Built by Ayush Raj</p>",
    unsafe_allow_html=True
)
