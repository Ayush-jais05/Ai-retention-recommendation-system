# 🎬 AI Movie Intelligence Platform

An end-to-end machine learning system that combines **churn prediction, recommendation systems, and user analytics** for a streaming platform use case. The project simulates real-world applications like Netflix or Hotstar by identifying at-risk users and improving engagement through personalized recommendations.

---

## 🚀 Overview

This project is designed as a full-stack ML product with three core modules:

* **Churn Intelligence**: Predicts user churn based on behavioral patterns
* **Recommendation Engine**: Suggests personalized movies using collaborative filtering
* **Analytics Dashboard**: Provides insights into user behavior, segmentation, and retention

The system focuses not only on prediction but also on **business-driven decision making**, including retention strategies and user segmentation.

---

## 🧠 Key Features

* Predicts churn probability using behavioral features
* Classifies users into High, Medium, and Low risk
* Generates personalized movie recommendations (KNN-based)
* Integrates real-time movie posters and trailers using TMDB API
* Performs user segmentation using clustering
* Implements retention cohort analysis
* Includes a personalized strategy engine for user retention
* Interactive multi-page dashboard built with Streamlit

---

## 📊 Dataset

### Churn Dataset (Synthetic)

A simulated dataset representing user behavior on a streaming platform.

**Features:**

* watch_time_per_day
* last_login_days
* genres_watched
* skip_rate
* engagement_score (derived)
* binge_factor (derived)

**Target:**

* churn (0 = retained, 1 = churned)

---

### Recommendation Dataset

* MovieLens dataset (movies + ratings)
* Filtered and optimized for scalability and deployment

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Plotly
* Joblib
* TMDB API

---

## 🧠 Machine Learning Pipeline

### Churn Model

* Data preprocessing and feature engineering
* Model training using Logistic Regression
* Evaluation using accuracy and ROC-AUC
* Feature importance and explainability

### Recommendation System

* KNN-based collaborative filtering
* Movie similarity using user interaction patterns
* Optimized model size for deployment (<100MB)
* Fallback recommendations for cold-start users

---

## 📊 Analytics & Intelligence

The analytics module provides deeper insights into user behavior:

* **User Segmentation**: KMeans clustering to group users based on engagement
* **Retention Cohorts**: Tracks user retention across activity levels
* **Recommendation Analytics**: Measures engagement (clicks vs watch time)
* **Strategy Engine**: Suggests actions based on user behavior

---

## 💡 Retention Strategy Logic

* High Risk → Offer discounts and push personalized content
* Medium Risk → Send targeted notifications and recommendations
* Low Risk → Maintain engagement and upsell premium features

---

## 📁 Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Analytics.py
│   ├── 3_Recommendations.py
│
├── models/
│   ├── churn_model.pkl
│   ├── movie_model.pkl
│   ├── movie_ids.pkl
│   ├── movies.pkl
|   ├── feature_columns.pkl
|   ├── scaler.pkl
│
├── churn/
│   └── churn_logic.py
│
├── recommender/
│   └── recommender.py
│
├── utils/
│   └── poster.py
```

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI-Retention-System.git
cd AI-Retention-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run app.py
```

---

## 📈 Key Insights

* Low engagement is the strongest indicator of churn
* High inactivity significantly increases churn risk
* Users with diverse content consumption show better retention
* Recommendation systems improve watch time and engagement
* Segmentation enables targeted retention strategies

---

## 🚀 Future Improvements

* Deploy using scalable cloud infrastructure (AWS / GCP)
* Add real-time user tracking and feedback loops
* Implement deep learning-based recommendation systems
* Introduce A/B testing for recommendation strategies
* Build API backend using FastAPI

---

## 👨‍💻 Author

Ayush Raj

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

---
