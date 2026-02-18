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
# LOAD MODELS 🔥 (REAL ML)
# =========================
churn_model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
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
st.markdown("Model-driven churn, segmentation & recommendation intelligence")
st.markdown("---")

# =========================
# GENERATE DATA (SIMULATION)
# =========================
np.random.seed(42)

data = pd.DataFrame({
    "watch_time_per_day": np.random.randint(20, 300, 300),
    "last_login_days": np.random.randint(1, 30, 300),
    "genres_watched": np.random.randint(1, 10, 300),
    "skip_rate": np.random.uniform(0, 1, 300)
})

# =========================
# FEATURE ENGINEERING
# =========================
data["engagement_score"] = data["watch_time_per_day"] / (data["last_login_days"] + 1)
data["binge_factor"] = data["watch_time_per_day"] / (data["genres_watched"] + 1)

# =========================
# APPLY SCALER + MODEL 🔥
# =========================
X = data[feature_columns]
X_scaled = scaler.transform(X)

# real predictions
data["churn_prob"] = churn_model.predict_proba(X_scaled)[:, 1]
data["churn"] = (data["churn_prob"] > 0.5).astype(int)

# =========================
# USER SEGMENTATION (SMART LABELING 🔥)
# =========================
kmeans = KMeans(n_clusters=3, random_state=42)
data["segment"] = kmeans.fit_predict(
    data[["watch_time_per_day", "engagement_score"]]
)

# 🔥 dynamic labeling using centroid logic
centroids = kmeans.cluster_centers_

sorted_idx = np.argsort(centroids[:, 0])  # sort by watch_time

segment_names = {}
segment_names[sorted_idx[0]] = "Low Engagement"
segment_names[sorted_idx[1]] = "Casual Users"
segment_names[sorted_idx[2]] = "Binge Watchers"

data["segment_label"] = data["segment"].map(segment_names)

# =========================
# KPI METRICS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Watch Time", f"{int(data['watch_time_per_day'].mean())} mins")
col2.metric("Churn Rate", f"{data['churn'].mean()*100:.1f}%")
col3.metric("Avg Genres", int(data["genres_watched"].mean()))
col4.metric("Avg Engagement", f"{data['engagement_score'].mean():.2f}")

st.markdown("---")

# =========================
# SEGMENTATION VISUAL
# =========================
st.markdown("## 👥 User Segmentation")

fig_seg = px.scatter(
    data,
    x="watch_time_per_day",
    y="engagement_score",
    color="segment_label",
    title="User Segments",
    template="plotly_dark"
)

# 🔥 plot centroids
fig_seg.add_scatter(
    x=centroids[:, 0],
    y=centroids[:, 1],
    mode='markers',
    marker=dict(size=15, color='white', symbol='x'),
    name="Centroids"
)

st.plotly_chart(fig_seg, use_container_width=True)

# =========================
# RETENTION COHORT
# =========================
st.markdown("## 📅 Retention Cohorts")

data["cohort"] = pd.cut(
    data["last_login_days"],
    bins=[0, 5, 10, 20, 30],
    labels=["0-5d", "5-10d", "10-20d", "20-30d"]
)

cohort_data = data.groupby("cohort")["churn"].mean().reset_index()

fig_cohort = px.bar(
    cohort_data,
    x="cohort",
    y="churn",
    title="Churn by Cohort",
    template="plotly_dark"
)

st.plotly_chart(fig_cohort, use_container_width=True)

# =========================
# CHURN ANALYSIS
# =========================
st.markdown("## 📉 Churn Insights")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.box(
        data,
        x="churn",
        y="watch_time_per_day",
        title="Watch Time vs Churn",
        template="plotly_dark"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(
        data,
        x="churn",
        y="skip_rate",
        title="Skip Rate vs Churn",
        template="plotly_dark"
    )
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# RECOMMENDER ANALYTICS
# =========================
st.markdown("## 🎬 Recommendation Analytics")

rec_data = pd.DataFrame({
    "movies": movies["title"].sample(150, replace=True).values,
    "clicks": np.random.randint(10, 500, 150),
    "watch_time": np.random.randint(20, 200, 150)
})

top_movies = rec_data.groupby("movies")["clicks"].sum().sort_values(ascending=False).head(10)

fig3 = px.bar(
    x=top_movies.values,
    y=top_movies.index,
    orientation='h',
    title="Top Recommended Movies",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# STRATEGY ENGINE 🔥
# =========================
st.markdown("## 💡 Personalized Strategy Engine")

def strategy(row):
    if row["churn"] == 1 and row["segment_label"] == "Low Engagement":
        return "Discount + strong recommendations"
    elif row["segment_label"] == "Binge Watchers":
        return "Upsell premium + early releases"
    else:
        return "Push personalized content"

data["strategy"] = data.apply(strategy, axis=1)

strategy_counts = data["strategy"].value_counts().reset_index()
strategy_counts.columns = ["Strategy", "Users"]

fig4 = px.bar(
    strategy_counts,
    x="Strategy",
    y="Users",
    title="Retention Strategies",
    template="plotly_dark"
)

st.plotly_chart(fig4, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built by Ayush Raj</p>", unsafe_allow_html=True)
