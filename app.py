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
# CUSTOM CSS 🔥 PREMIUM UI
# =========================
st.markdown("""
<style>

/* background */
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* hero gradient text */
.gradient-text {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* cards */
.card {
    background: rgba(255,255,255,0.07);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
}

/* buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    font-size: 16px;
    padding: 10px;
}

/* subtext */
.subtext {
    color: #94a3b8;
    font-size: 16px;
}

.metric-box {
    text-align: center;
    padding: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION 🔥
# =========================
st.markdown("""
<div style='text-align:center; padding:70px'>
    <h1 class='gradient-text' style='font-size:64px;'>🎬 AI Movie Intelligence</h1>
    <p class='subtext' style='font-size:20px;'>
        ML-powered platform combining recommendation systems & churn prediction 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# STATS SECTION (🔥 RESUME BOOST)
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.markdown("<div class='metric-box'><h2>3000+</h2><p class='subtext'>Movies</p></div>", unsafe_allow_html=True)
col2.markdown("<div class='metric-box'><h2>KNN</h2><p class='subtext'>Model</p></div>", unsafe_allow_html=True)
col3.markdown("<div class='metric-box'><h2>ML</h2><p class='subtext'>Churn Prediction</p></div>", unsafe_allow_html=True)
col4.markdown("<div class='metric-box'><h2>Real-Time</h2><p class='subtext'>TMDB API</p></div>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# MODULE NAVIGATION 🔥
# =========================
st.markdown("## 🚀 Explore Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📉 Churn Intelligence</h3>
        <p class='subtext'>
        Predict user drop-off using ML models and behavioral data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Go to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎬 Recommendation Engine</h3>
        <p class='subtext'>
        KNN-based movie recommendations with real-time posters & trailers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Go to Recommendations"):
        st.switch_page("pages/3_Recommendations.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Analytics Engine</h3>
        <p class='subtext'>
        User segmentation, retention cohorts & recommendation insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Go to Analytics"):
        st.switch_page("pages/2_Analytics.py")

st.markdown("---")

# =========================
# FEATURES 🔥
# =========================
st.markdown("## ⚡ Key Features")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📉 Churn Prediction</h4>
        <p class='subtext'>Predict user retention risk using ML</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🎬 Smart Recommender</h4>
        <p class='subtext'>KNN-based movie similarity engine</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>📊 Analytics</h4>
        <p class='subtext'>Segmentation, cohorts & insights</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h4>🌐 Real-Time API</h4>
        <p class='subtext'>Live posters & trailers via TMDB</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# HOW IT WORKS
# =========================
st.markdown("## 🧠 How It Works")

st.markdown("""
<div class="card">

1️⃣ User behavior is captured  
<br><br>
2️⃣ ML models analyze engagement  
<br><br>
3️⃣ Churn probability is predicted  
<br><br>
4️⃣ Personalized recommendations are delivered  

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# FINAL CTA 🔥
# =========================
st.success("🚀 Ready to explore AI-powered insights? Start from the modules above!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>",
    unsafe_allow_html=True
)
