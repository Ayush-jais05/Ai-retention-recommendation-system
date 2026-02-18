# =========================
# IMPORTS
# =========================
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide",
    page_icon="📊"
)

# =========================
# LOAD MODELS
# =========================
churn_model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
movies = joblib.load("models/movies.pkl")

# =========================
# HEADER
# =========================
st.title("📊 Analytics Dashboard")
st.caption("Model-driven churn, segmentation & recommendation insights")
st.markdown("---")

# =========================
# CREATE USER DATA
# =========================
np.random.seed(42)

n_users = 300

data = pd.DataFrame({
    "watch_time_per_day": np.random.randint(30, 250, n_users),
    "last_login_days": np.random.randint(1, 30, n_users),
    "genres_watched": np.random.randint(1, 8, n_users),
    "skip_rate": np.random.uniform(0.1, 0.9, n_users)
})

# =========================
# FEATURE ENGINEERING
# =========================
data["engagement_score"] = data["watch_time_per_day"] / (data["last_login_days"] + 1)
data["binge_factor"] = data["watch_time_per_day"] / (data["genres_watched"] + 1)

# =========================
# APPLY MODEL
# =========================
X = data[feature_columns]
X_scaled = scaler.transform(X)

data["churn_prob"] = churn_model.predict_proba(X_scaled)[:, 1]
data["churn"] = (data["churn_prob"] > 0.5).astype(int)

# =========================
# SEGMENTATION
# =========================
seg_features = data[["watch_time_per_day", "engagement_score"]]
seg_scaled = StandardScaler().fit_transform(seg_features)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data["segment"] = kmeans.fit_predict(seg_scaled)

centroids = kmeans.cluster_centers_
order = np.argsort(centroids[:, 0])

labels = {
    order[0]: "Low Engagement",
    order[1]: "Casual Users",
    order[2]: "Binge Watchers"
}

data["segment_label"] = data["segment"].map(labels)

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
st.subheader("👥 User Segmentation")

fig_seg = px.scatter(
    data,
    x="watch_time_per_day",
    y="engagement_score",
    color="segment_label",
    template="plotly_dark"
)

st.plotly_chart(fig_seg, use_container_width=True)

st.markdown("### 📌 Insights")
st.markdown("""
- Users are segmented into **Low Engagement, Casual Users, and Binge Watchers**  
- Binge watchers show **highest engagement and retention potential**  
- Low engagement users are **most likely to churn and require intervention**  
""")

# =========================
# RETENTION COHORT
# =========================
st.subheader("📅 Retention Cohorts")

data["cohort"] = pd.cut(
    data["last_login_days"],
    bins=[0, 5, 10, 20, 30],
    labels=["0-5d", "5-10d", "10-20d", "20-30d"]
)

cohort = data.groupby("cohort")["churn"].mean().reset_index()

fig_cohort = px.bar(
    cohort,
    x="cohort",
    y="churn",
    template="plotly_dark"
)

st.plotly_chart(fig_cohort, use_container_width=True)

st.markdown("### 📌 Insights")
st.markdown("""
- Users inactive for **10+ days show significantly higher churn**  
- Recently active users have **lowest churn probability**  
- Re-engagement strategies should target **inactive users quickly**  
""")

# =========================
# CHURN ANALYSIS
# =========================
st.subheader("📉 Churn Analysis")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        px.box(data, x="churn", y="watch_time_per_day", template="plotly_dark"),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        px.box(data, x="churn", y="skip_rate", template="plotly_dark"),
        use_container_width=True
    )

st.markdown("### 📌 Insights")
st.markdown("""
- Lower watch time strongly correlates with **higher churn**  
- Higher skip rate indicates **low content satisfaction → churn risk**  
- Improving recommendations can **reduce churn significantly**  
""")

# =========================
# RECOMMENDER ANALYTICS
# =========================
st.subheader("🎬 Recommendation Analytics")

top_movies = movies["title"].value_counts().head(10)

fig_rec = px.bar(
    x=top_movies.values,
    y=top_movies.index,
    orientation='h',
    template="plotly_dark"
)

st.plotly_chart(fig_rec, use_container_width=True)

st.markdown("### 📌 Insights")
st.markdown("""
- Frequently occurring movies indicate **high engagement content**  
- These can be used for **trending sections and homepage boosts**  
- Popular content improves **user session time and retention**  
""")

# =========================
# STRATEGY ENGINE
# =========================
st.subheader("💡 Strategy Engine")

def strategy(row):
    if row["churn"] == 1 and row["segment_label"] == "Low Engagement":
        return "High Risk: Offer discounts + strong recommendations"
    elif row["segment_label"] == "Binge Watchers":
        return "Upsell premium content"
    else:
        return "Send personalized notifications"

data["strategy"] = data.apply(strategy, axis=1)

strategy_df = data["strategy"].value_counts().reset_index()
strategy_df.columns = ["Strategy", "Users"]

st.plotly_chart(
    px.bar(strategy_df, x="Strategy", y="Users", template="plotly_dark"),
    use_container_width=True
)

st.markdown("### 📌 Insights")
st.markdown("""
- High-risk users require **discounts and strong personalization**  
- Binge watchers are ideal for **premium upselling strategies**  
- Casual users benefit from **targeted notifications and recommendations**  
""")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built by Ayush Raj")
