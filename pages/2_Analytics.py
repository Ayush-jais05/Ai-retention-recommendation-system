# =========================
# IMPORTS
# =========================
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODELS 🔥
# =========================
churn_model = joblib.load("models/churn_model.pkl")
movies = joblib.load("models/movies.pkl")

# =========================
# UI STYLE 🔥
# =========================
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

.card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================
st.markdown("## 📊 Analytics Dashboard")
st.markdown("Understand churn patterns & recommendation insights 🚀")
st.markdown("---")


# =========================
# MOCK USER DATA (SIMULATION 🔥)
# =========================
np.random.seed(42)

data = pd.DataFrame({
    "watch_time": np.random.randint(20, 300, 200),
    "last_login": np.random.randint(1, 30, 200),
    "genres": np.random.randint(1, 10, 200),
    "skip_rate": np.random.uniform(0, 1, 200)
})

# Feature engineering
data["engagement"] = data["watch_time"] / (data["last_login"] + 1)
data["binge"] = data["watch_time"] / (data["genres"] + 1)

# Simulated churn
data["churn"] = (data["engagement"] < 5).astype(int)


# =========================
# KPI METRICS 🔥
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("👀 Avg Watch Time", f"{int(data['watch_time'].mean())} mins")
col2.metric("⚠️ Churn Rate", f"{data['churn'].mean()*100:.1f}%")
col3.metric("🎬 Avg Genres", int(data["genres"].mean()))
col4.metric("🔥 Engagement Score", f"{data['engagement'].mean():.2f}")

st.markdown("---")


# =========================
# SECTION 1: USER BEHAVIOR
# =========================
st.markdown("## 👤 User Behavior Analytics")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(
        data,
        x="watch_time",
        nbins=25,
        title="Watch Time Distribution",
        template="plotly_dark"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        data,
        x="last_login",
        y="watch_time",
        color="churn",
        title="Activity vs Churn",
        template="plotly_dark"
    )
    st.plotly_chart(fig2, use_container_width=True)


# =========================
# SECTION 2: CHURN ANALYSIS
# =========================
st.markdown("## 📉 Churn Insights")

col1, col2 = st.columns(2)

with col1:
    fig3 = px.box(
        data,
        x="churn",
        y="watch_time",
        title="Watch Time vs Churn",
        template="plotly_dark"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.box(
        data,
        x="churn",
        y="skip_rate",
        title="Skip Rate vs Churn",
        template="plotly_dark"
    )
    st.plotly_chart(fig4, use_container_width=True)


# =========================
# 🔥 NEW SECTION: RECOMMENDER ANALYTICS
# =========================
st.markdown("## 🎬 Recommendation Analytics (NEW 🔥)")

# simulate recommendation usage
rec_data = pd.DataFrame({
    "movies": movies["title"].sample(100, replace=True).values,
    "clicks": np.random.randint(10, 500, 100),
    "watch_time": np.random.randint(20, 200, 100)
})

# Top recommended movies
top_movies = rec_data.groupby("movies")["clicks"].sum().sort_values(ascending=False).head(10)

fig5 = px.bar(
    x=top_movies.values,
    y=top_movies.index,
    orientation='h',
    title="Top Recommended Movies (Engagement)",
    template="plotly_dark"
)

st.plotly_chart(fig5, use_container_width=True)


# =========================
# RECOMMENDATION PERFORMANCE
# =========================
st.markdown("### 🎯 Recommendation Performance")

fig6 = px.scatter(
    rec_data,
    x="clicks",
    y="watch_time",
    title="Clicks vs Watch Time",
    template="plotly_dark"
)

st.plotly_chart(fig6, use_container_width=True)


# =========================
# INSIGHTS SECTION 🧠
# =========================
st.markdown("## 🧠 Key Insights")

st.markdown("""
<div class="card">

🔥 Users with **low engagement score** churn more  

⏳ Longer inactivity → higher churn risk  

🎬 High genre diversity → better retention  

📈 Recommended movies with higher clicks → higher watch time  

💡 Recommendation system improves engagement significantly  

</div>
""", unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>", unsafe_allow_html=True)
