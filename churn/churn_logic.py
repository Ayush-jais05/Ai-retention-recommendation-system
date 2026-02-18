import joblib
import pandas as pd

# =========================
# LOAD ARTIFACTS
# =========================
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


# =========================
# PREPROCESS INPUT
# =========================
def preprocess_input(user_df):
    full_df = pd.DataFrame(columns=feature_columns)
    full_df.loc[0] = 0

    for col in user_df.columns:
        if col in full_df.columns:
            full_df[col] = user_df[col].values[0]

    return full_df


# =========================
# RISK LOGIC
# =========================
def get_risk_level(prob):
    if prob >= 0.7:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"


# =========================
# EXPLANATION
# =========================
def explain_prediction(user_df):
    reasons = []

    if user_df["skip_rate"].values[0] > 0.6:
        reasons.append("High skip rate")

    if user_df["last_login_days"].values[0] > 10:
        reasons.append("Inactive for long time")

    if user_df["watch_time_per_day"].values[0] < 60:
        reasons.append("Low watch time")

    if user_df["engagement_score"].values[0] < 40:
        reasons.append("Low engagement")

    if len(reasons) == 0:
        reasons.append("Healthy user behavior")

    return reasons


# =========================
# MAIN FUNCTION
# =========================
def predict_churn(user_df):

    processed_df = preprocess_input(user_df)

    scaled = scaler.transform(processed_df)

    prob = float(model.predict_proba(scaled)[0][1])  # ✅ ALWAYS FLOAT

    risk = get_risk_level(prob)

    reasons = explain_prediction(user_df)

    return prob, risk, reasons  # ✅ 3 VALUES
