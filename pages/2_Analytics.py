import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# HEADER
# =========================
st.markdown("## 📊 Analytics Dashboard")
st.markdown("Analyze user behavior and churn patterns 📈")

st.markdown("---")

# =========================
# MOCK DATA (for demo)
# =========================
# Later you can replace this with real data
np.random.seed(42)

data = pd.DataFrame({
    "watch_time": np.random.randint(20, 300, 100),
    "last_login": np.random.randint(1, 30, 100),
    "genres": np.random.randint(1, 10, 100),
    "churn": np.random.choice([0, 1], 100)
})

# =========================
# METRICS (TOP ROW)
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👀 Avg Watch Time", f"{int(data['watch_time'].mean())} mins")

with col2:
    churn_rate = data['churn'].mean() * 100
    st.metric("⚠️ Churn Rate", f"{churn_rate:.1f}%")

with col3:
    st.metric("🎬 Avg Genres Watched", int(data['genres'].mean()))

st.markdown("---")

# =========================
# CHART 1: WATCH TIME DISTRIBUTION
# =========================
st.markdown("### 📊 Watch Time Distribution")

fig1 = px.histogram(
    data,
    x="watch_time",
    nbins=20,
    title="Distribution of Watch Time",
    template="plotly_dark"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# CHART 2: CHURN VS LAST LOGIN
# =========================
st.markdown("### ⏳ Churn vs Last Login")

fig2 = px.scatter(
    data,
    x="last_login",
    y="watch_time",
    color="churn",
    title="User Activity vs Churn",
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# CHART 3: GENRE VS CHURN
# =========================
st.markdown("### 🎬 Genres Watched vs Churn")

fig3 = px.box(
    data,
    x="churn",
    y="genres",
    title="Genres vs Churn",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# INSIGHTS SECTION
# =========================
st.markdown("## 🧠 Key Insights")

st.markdown("""
- Users with **low watch time** are more likely to churn  
- **Inactive users (higher last login days)** show higher churn risk  
- More engaged users (watching more genres) tend to stay longer  
""")

st.markdown("---")

# =========================
# FOOTER
# =========================
st.markdown("<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>", unsafe_allow_html=True)
