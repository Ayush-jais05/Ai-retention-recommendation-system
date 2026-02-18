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
# CUSTOM CSS (PREMIUM UI 🔥)
# =========================
st.markdown("""
<style>

/* background */
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* glass cards */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
    transition: all 0.3s ease;
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.6);
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

/* subtle text */
.subtext {
    color: #94a3b8;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION 🔥
# =========================
st.markdown("""
<div style='text-align:center; padding:60px'>
    <h1 style='font-size:56px;'>🎬 AI Movie Intelligence</h1>
    <p class='subtext'>
        Smart platform for movie recommendations & user retention analytics 🚀
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# QUICK NAVIGATION
# =========================
st.markdown("## 🚀 Explore Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📉 Churn Intelligence</h3>
        <p class='subtext'>
        Predict user drop-off using behavioral ML models.
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
        Discover personalized movie suggestions powered by AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Go to Recommendations"):
        st.switch_page("pages/3_Recommendations.py")

st.markdown("---")

# =========================
# FEATURES SECTION
# =========================
st.markdown("## ⚡ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📉 Churn Prediction</h4>
        <p class='subtext'>
        Identify users likely to leave using ML insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🎬 Smart Recommendations</h4>
        <p class='subtext'>
        KNN-based movie suggestions using real user data.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>📊 Analytics Dashboard</h4>
        <p class='subtext'>
        Visualize engagement and user behavior patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# HOW IT WORKS
# =========================
st.markdown("## 🧠 How It Works")

st.markdown("""
<div class="card">

1️⃣ User interaction data is collected  
<br><br>
2️⃣ ML models analyze behavior patterns  
<br><br>
3️⃣ System predicts churn probability  
<br><br>
4️⃣ AI recommends personalized content  

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# FINAL CTA
# =========================
st.success("🚀 Start exploring using the sidebar or buttons above!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>",
    unsafe_allow_html=True
)
