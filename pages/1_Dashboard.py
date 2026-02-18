# =========================
# IMPORTS
# =========================
import streamlit as st

st.set_page_config(
    page_title="Churn Intelligence Dashboard",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from churn.churn_logic import predict_churn


# =========================
# PREMIUM UI 🔥
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
    border-radius: 18px;
    margin-bottom: 20px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.center { text-align: center; }

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    font-size: 18px;
    padding: 12px;
}

.metric-card {
    text-align:center;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class='center' style='padding:30px'>
    <h1 style='font-size:44px;'>📉 Churn Intelligence Dashboard</h1>
    <p style='font-size:18px; color:#94a3b8;'>
        Predict churn, understand behavior & boost retention 🚀
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.markdown("## 🎛️ User Behavior Inputs")
st.sidebar.markdown("---")

watch_time = st.sidebar.slider("🎬 Watch Time (mins/day)", 10, 300, 120)
last_login = st.sidebar.slider("📅 Days Since Last Login", 1, 30, 5)
genres = st.sidebar.slider("🎭 Genres Watched", 1, 10, 3)
skip_rate = st.sidebar.slider("⏭️ Skip Rate", 0.0, 1.0, 0.3)


# =========================
# FEATURE ENGINEERING
# =========================
engagement_score = watch_time / (last_login + 1)
binge_factor = watch_time / (genres + 1)

input_data = pd.DataFrame([{
    "watch_time_per_day": watch_time,
    "last_login_days": last_login,
    "genres_watched": genres,
    "skip_rate": skip_rate,
    "engagement_score": engagement_score,
    "binge_factor": binge_factor
}])


# =========================
# LIVE INSIGHTS (NEW 🔥)
# =========================
st.markdown("## ⚡ Quick Insights")

col1, col2, col3 = st.columns(3)

col1.metric("🔥 Engagement Score", f"{engagement_score:.2f}")
col2.metric("📺 Binge Factor", f"{binge_factor:.2f}")
col3.metric("⚠️ Risk Signal", "High" if skip_rate > 0.5 else "Normal")


# =========================
# MAIN BUTTON
# =========================
if st.button("🚀 Analyze User"):

    with st.spinner("Analyzing user behavior... 🤖"):

        try:
            prob, risk, reasons = predict_churn(input_data)
            prob = float(prob)

            # =========================
            # RESULT HEADER
            # =========================
            st.markdown("## 📉 Churn Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.metric("Churn Probability", f"{prob:.2%}")
                st.progress(prob)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                if risk == "High":
                    st.error("🔴 High Risk User")
                elif risk == "Medium":
                    st.warning("🟡 Medium Risk User")
                else:
                    st.success("🟢 Low Risk User")

                st.markdown('</div>', unsafe_allow_html=True)

            # =========================
            # GAUGE CHART 🔥
            # =========================
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                title={'text': "Churn Risk"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#6366f1"},
                    'steps': [
                        {'range': [0, 40], 'color': "#22c55e"},
                        {'range': [40, 70], 'color': "#facc15"},
                        {'range': [70, 100], 'color': "#ef4444"}
                    ]
                }
            ))

            st.plotly_chart(fig, use_container_width=True)


            # =========================
            # REASONS
            # =========================
            st.markdown("## 🧠 Why this prediction?")

            st.markdown('<div class="card">', unsafe_allow_html=True)
            for r in reasons:
                st.info(r)
            st.markdown('</div>', unsafe_allow_html=True)


            # =========================
            # USER BEHAVIOR CHART
            # =========================
            st.markdown("## 📊 User Behavior Insights")

            df_viz = pd.DataFrame({
                "Feature": ["Watch Time", "Last Login", "Genres", "Skip Rate"],
                "Value": [watch_time, last_login, genres, skip_rate]
            })

            fig = px.bar(
                df_viz,
                x="Feature",
                y="Value",
                color="Value",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)


            # =========================
            # RETENTION STRATEGY 🔥
            # =========================
            st.markdown("## 💡 Retention Strategy")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            if risk == "High":
                st.toast("🔥 High churn risk detected!", icon="⚠️")
                st.error("Offer discounts + aggressive re-engagement campaigns")
                st.markdown("👉 Send push notifications\n👉 Offer premium trial\n👉 Recommend trending content")

            elif risk == "Medium":
                st.warning("User needs engagement boost")
                st.markdown("👉 Improve recommendations\n👉 Send reminders\n👉 Highlight new releases")

            else:
                st.success("User is healthy 🎉")
                st.markdown("👉 Maintain experience\n👉 Introduce personalization")

            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("<p class='center'>Built with ❤️ by Ayush Raj</p>", unsafe_allow_html=True)
