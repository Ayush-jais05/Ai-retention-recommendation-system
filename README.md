# 🎬 AI Customer Retention & Recommendation System

An end-to-end Machine Learning system that predicts user churn on a streaming platform and provides personalized movie recommendations with explainable AI insights.

---

## 🚀 Project Overview

This project simulates a real-world streaming platform (like Netflix/Hotstar) where:

- 📉 Users at risk of churn are identified using ML
- 🎬 Personalized recommendations are generated
- 🔍 Explainable AI (SHAP) provides reasons behind predictions
- 💡 Retention strategies are suggested based on risk level

---

## 🧠 Key Features

- Predicts churn probability using user behavior
- Classifies users into High / Medium / Low risk
- Provides reasons for churn prediction (Explainable AI)
- Recommends movies using collaborative filtering
- Handles cold-start users with fallback recommendations
- Interactive UI built with Streamlit

---

## 📊 Dataset

### 🔹 Churn Dataset (Synthetic but Realistic)

A behavior-driven dataset was created to simulate streaming platform users.

### Features:
- `watch_time_per_day`
- `last_login_days`
- `genres_watched`
- `skip_rate`
- `engagement_score` (derived)
- `binge_factor` (derived)

### Target:
- `Churn` (0 = No, 1 = Yes)

### Logic:
Churn is influenced by:
- Low watch time
- High inactivity
- High skip rate
- Low engagement

---

### 🔹 Recommendation Dataset

- MovieLens dataset (ratings + movies)
- Used for collaborative filtering

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Plotly
- SHAP (Explainable AI)
- Joblib

---

## 🧠 Machine Learning Pipeline

1. Data preprocessing & feature engineering
2. Train-test split
3. Feature scaling (StandardScaler)
4. Model training (Logistic Regression)
5. Model evaluation:
   - Accuracy
   - ROC-AUC
   - Confusion Matrix
6. Model interpretability using SHAP
7. Model saving for deployment

---

## 📈 Model Insights

- High skip rate strongly increases churn probability
- Users inactive for longer periods are more likely to churn
- Higher engagement reduces churn risk
- Watch time has moderate influence on retention

---

## 🎬 Recommendation System

- Item-based collaborative filtering
- Cosine similarity between movies
- Weighted scoring based on user preferences
- Fallback to trending movies for new users

---

## 📁 Project Structure

project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│ ├── churn_model.pkl
│ ├── scaler.pkl
│ ├── feature_columns.pkl
│
├── churn/
│ └── churn_logic.py
│
├── recommender/
│ └── recommender.py
│
├── data/
│ ├── movies.csv
│ ├── ratings.csv


---

## ▶️ How to Run

### Clone Repository

```bash
1. git clone https://github.com/your-username/AI-Retention-System.git
cd AI-Retention-System

2. Install Dependencies
pip install -r requirements.txt

3. Run App
streamlit run app.py


💡 Retention Strategy Logic

🔥 High Risk → Offer discounts + personalized recommendations

⚡ Medium Risk → Send notifications & targeted content

✅ Low Risk → Maintain engagement

🔍 Explainable AI (SHAP)

The model explains predictions by identifying:

Which features increase churn

Which features reduce churn

This improves transparency and trust in ML decisions.

🚀 Future Improvements

Deploy using cloud (Streamlit Cloud / AWS)

Add user segmentation (clustering)

Improve recommendation with deep learning

Real-time user tracking

👨‍💻 Author

Ayush Raj

⭐ Support

If you like this project, give it a ⭐ on GitHub!
