import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_recall_fscore_support,
    roc_auc_score, confusion_matrix
)
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

st.title("Loan Approval Model Comparison")

# 1. Data upload
data_file = st.file_uploader("Upload CSV", type="csv")
if data_file:
    df = pd.read_csv(data_file)
else:
    st.stop()

st.write("Dataset Preview", df.head())

# 2. Preprocessing (example)
df = pd.get_dummies(df, drop_first=True)
df = df.dropna()

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"].map({"Y": 1, "N": 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# optional scaling for LR
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model training
lr = LogisticRegression(max_iter=500, solver="liblinear")
lr.fit(X_train_scaled, y_train)

xgb = XGBClassifier(
    objective="binary:logistic", eval_metric="logloss", use_label_encoder=False
)
xgb.fit(X_train, y_train)

# 4. Evaluation
def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    acc = accuracy_score(y_test, preds)
    prec, rec, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary")
    auc = roc_auc_score(y_test, prob)
    cm = confusion_matrix(y_test, preds)
    return acc, prec, rec, f1, auc, cm

metrics_lr = evaluate(lr, X_test_scaled, y_test)
metrics_xgb = evaluate(xgb, X_test, y_test)

st.subheader("Logistic Regression Metrics")
st.write(metrics_lr)

st.subheader("XGBoost Metrics")
st.write(metrics_xgb)

# Compare visually
comparison = pd.DataFrame(
    [metrics_lr[:-1], metrics_xgb[:-1]], 
    columns=["Accuracy", "Precision", "Recall", "F1", "ROC-AUC"],
    index=["Logistic Regression", "XGBoost"]
)
st.bar_chart(comparison.transpose())
