# =========================
# IMPORTS
# =========================
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib
from sklearn.cluster import KMeans

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODELS
# =========================
churn_model = joblib.load("models/churn_model.pkl")
movies = joblib.load("models/movies.pkl")

# =========================
# UI STYLE
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
st.markdown("Understand churn patterns & recommendation intelligence 🚀")
st.markdown("---")

# =========================
# MOCK DATA
# =========================
np.random.seed(42)

data = pd.DataFrame({
    "watch_time": np.random.randint(20, 300, 300),
    "last_login": np.random.randint(1, 30, 300),
    "genres": np.random.randint(1, 10, 300),
    "skip_rate": np.random.uniform(0, 1, 300)
})

# feature engineering
data["engagement"] = data["watch_time"] / (data["last_login"] + 1)
data["binge"] = data["watch_time"] / (data["genres"] + 1)

# churn simulation
data["churn"] = (data["engagement"] < 5).astype(int)

# =========================
# KPI METRICS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("👀 Avg Watch Time", f"{int(data['watch_time'].mean())} mins")
col2.metric("⚠️ Churn Rate", f"{data['churn'].mean()*100:.1f}%")
col3.metric("🎬 Avg Genres", int(data["genres"].mean()))
col4.metric("🔥 Engagement", f"{data['engagement'].mean():.2f}")

st.markdown("---")

# =========================
# USER SEGMENTATION 🔥
# =========================
st.markdown("## 🧠 User Segmentation (Clustering)")

features = data[["watch_time", "last_login", "genres", "skip_rate"]]

kmeans = KMeans(n_clusters=3, random_state=42)
data["segment"] = kmeans.fit_predict(features)

fig_seg = px.scatter(
    data,
    x="watch_time",
    y="engagement",
    color="segment",
    title="User Segments",
    template="plotly_dark"
)

st.plotly_chart(fig_seg, use_container_width=True)

# =========================
# SEGMENT INSIGHTS
# =========================
st.markdown("### 🎯 Segment Meaning")

st.markdown("""
<div class="card">

🟢 Segment 0 → High engagement users (loyal users)  
🟡 Segment 1 → Medium users (can churn soon)  
🔴 Segment 2 → Low engagement users (high risk)  

</div>
""", unsafe_allow_html=True)

# =========================
# RETENTION COHORTS 🔥
# =========================
st.markdown("## ⏳ Retention Cohort Analysis")

data["cohort"] = pd.cut(data["last_login"], bins=[0,5,10,20,30], labels=["Active","Warm","Cold","Lost"])

cohort_data = data.groupby(["cohort", "churn"]).size().reset_index(name="count")

fig_cohort = px.bar(
    cohort_data,
    x="cohort",
    y="count",
    color="churn",
    barmode="group",
    title="Retention Cohorts",
    template="plotly_dark"
)

st.plotly_chart(fig_cohort, use_container_width=True)

# =========================
# RECOMMENDER ANALYTICS
# =========================
st.markdown("## 🎬 Recommendation Analytics")

rec_data = pd.DataFrame({
    "movies": movies["title"].sample(150, replace=True),
    "clicks": np.random.randint(10, 500, 150),
    "watch_time": np.random.randint(20, 200, 150)
})

top_movies = rec_data.groupby("movies")["clicks"].sum().sort_values(ascending=False).head(10)

fig_top = px.bar(
    x=top_movies.values,
    y=top_movies.index,
    orientation='h',
    title="Top Recommended Movies",
    template="plotly_dark"
)

st.plotly_chart(fig_top, use_container_width=True)

# =========================
# PERFORMANCE
# =========================
st.markdown("### 🎯 Recommendation Performance")

fig_perf = px.scatter(
    rec_data,
    x="clicks",
    y="watch_time",
    size="clicks",
    title="Engagement vs Watch Time",
    template="plotly_dark"
)

st.plotly_chart(fig_perf, use_container_width=True)

# =========================
# PERSONALIZED STRATEGY ENGINE 🔥
# =========================
st.markdown("## 💡 Personalized Strategy Engine")

def strategy(row):
    if row["segment"] == 2:
        return "🔥 Offer discounts + strong recommendations"
    elif row["segment"] == 1:
        return "⚡ Send notifications & personalized content"
    else:
        return "✅ Maintain experience"

data["strategy"] = data.apply(strategy, axis=1)

sample_users = data.sample(5)[["watch_time","last_login","segment","strategy"]]

st.dataframe(sample_users)

# =========================
# INSIGHTS
# =========================
st.markdown("## 🧠 Key Insights")

st.markdown("""
<div class="card">

🔥 Low engagement users → highest churn  

📉 High skip rate → bad content matching  

🎯 Personalized recommendations increase retention  

📊 Segmentation helps targeted marketing  

</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>", unsafe_allow_html=True)
