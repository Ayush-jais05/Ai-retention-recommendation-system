<div align="center">

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
<img src="https://img.shields.io/badge/TMDB_API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" />

<br/>
<br/>

# 🎬 AI Movie Intelligence Platform

**An end-to-end ML system for churn prediction, personalized recommendations, and user analytics — built for streaming platforms.**

[Features](#-features) · [Architecture](#-architecture) · [Installation](#-installation) · [Usage](#-usage) · [Insights](#-key-insights) · [Roadmap](#-roadmap)

</div>

---

## 📌 Overview

The **AI Movie Intelligence Platform** simulates a real-world streaming intelligence system (think Netflix, Hotstar) with three fully integrated ML modules:

| Module | Description |
|---|---|
| 🔴 **Churn Intelligence** | Identifies at-risk users using behavioral signals |
| 🎯 **Recommendation Engine** | Delivers personalized movie suggestions via collaborative filtering |
| 📊 **Analytics Dashboard** | Surfaces retention cohorts, segmentation, and engagement trends |

> Built as a full-stack ML product with business-driven decision-making at its core — not just model outputs.

---

## ✨ Features

- ✅ Churn probability scoring with **High / Medium / Low** risk classification
- ✅ KNN-based collaborative filtering recommendation engine
- ✅ Real-time movie posters and trailers via **TMDB API**
- ✅ User segmentation using **KMeans clustering**
- ✅ Retention cohort analysis by activity level
- ✅ Personalized retention strategy engine
- ✅ Interactive multi-page dashboard built with **Streamlit + Plotly**
- ✅ Cold-start fallback recommendations

---

## 🏗 Architecture

```
project/
│
├── app.py                     # Entry point
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Dashboard.py         # Churn predictions & risk overview
│   ├── 2_Analytics.py         # Segmentation, cohorts, engagement
│   └── 3_Recommendations.py   # Personalized movie suggestions
│
├── models/
│   ├── churn_model.pkl        # Logistic Regression churn model
│   ├── movie_model.pkl        # KNN recommendation model
│   ├── movie_ids.pkl
│   ├── movies.pkl
│   ├── feature_columns.pkl
│   └── scaler.pkl
│
├── churn/
│   └── churn_logic.py         # Feature engineering & prediction logic
│
├── recommender/
│   └── recommender.py         # KNN similarity & recommendation logic
│
└── utils/
    └── poster.py              # TMDB API integration
```

---

## 🧠 ML Pipeline

### Churn Model
- Feature engineering on behavioral signals (`watch_time_per_day`, `last_login_days`, `skip_rate`, etc.)
- Derived features: `engagement_score`, `binge_factor`
- Model: **Logistic Regression** — interpretable, production-ready
- Metrics: Accuracy + ROC-AUC
- Includes feature importance and explainability layer

### Recommendation Engine
- **KNN collaborative filtering** on MovieLens dataset
- Similarity computed from user interaction patterns
- Optimized model size **< 100MB** for lightweight deployment
- Fallback logic handles cold-start users gracefully

---

## 📊 Dataset

### Churn Dataset (Synthetic)

Simulates user behavior on a streaming platform.

| Feature | Description |
|---|---|
| `watch_time_per_day` | Average daily watch time |
| `last_login_days` | Days since last login |
| `genres_watched` | Breadth of genre exploration |
| `skip_rate` | Fraction of content skipped |
| `engagement_score` | Derived composite score |
| `binge_factor` | Binge-watching intensity |
| `churn` | **Target** — 0 (retained) / 1 (churned) |

### Recommendation Dataset
- **MovieLens** (movies + ratings)
- Filtered and optimized for scalable deployment

---

## ⚙️ Installation

### Prerequisites
- Python 3.9+
- TMDB API key ([get one here](https://www.themoviedb.org/settings/api))

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/AI-Movie-Intelligence-Platform.git
cd AI-Movie-Intelligence-Platform

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your TMDB API key
# Set it as an environment variable or in a .env file:
export TMDB_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

### Pages

| Page | What You Can Do |
|---|---|
| **Dashboard** | Input user behavior → get churn risk score + retention strategy |
| **Analytics** | Explore user segments, cohort retention, engagement metrics |
| **Recommendations** | Search a movie → get personalized recommendations with posters |

---

## 💡 Retention Strategy Engine

The platform automatically suggests actions based on churn risk:

| Risk Level | Strategy |
|---|---|
| 🔴 High Risk | Offer discounts · Push personalized content · Trigger re-engagement campaigns |
| 🟡 Medium Risk | Send targeted notifications · Surface relevant recommendations |
| 🟢 Low Risk | Maintain engagement · Upsell premium features |

---

## 📈 Key Insights

- **Low engagement** is the strongest predictor of churn
- **High inactivity** (days since last login) significantly elevates risk
- Users with **diverse genre consumption** show stronger retention
- **Recommendations** improve watch time and overall engagement
- **Segmentation** enables targeted, cost-effective retention strategies

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| ML & Data | Scikit-learn, Pandas, NumPy, Joblib |
| Frontend | Streamlit, Plotly |
| External API | TMDB API |
| Dataset | MovieLens (collaborative filtering) |

---

## 🚀 Roadmap

- [ ] Cloud deployment on AWS / GCP with auto-scaling
- [ ] Real-time user event tracking and feedback loops
- [ ] Deep learning recommendation models (Neural Collaborative Filtering)
- [ ] A/B testing framework for recommendation strategies
- [ ] FastAPI backend for REST API integration
- [ ] Docker containerization for portable deployment

---

## 👨‍💻 Author

**Ayush Raj**  
Built as an end-to-end ML product showcasing churn prediction, recommendation systems, and user intelligence for streaming platforms.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
If you found this project useful, consider giving it a ⭐ on GitHub — it helps a lot!
</div>