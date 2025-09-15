# Comparative Performance of Logistic Regression vs. XGBoost in Loan Approval Prediction

## Overview
This project predicts loan approval status and compares two models:

1. **Logistic Regression** – fast and interpretable.
2. **XGBoost** – gradient-boosted trees for higher accuracy.

## Dataset
Kaggle “Loan Prediction” dataset  
Features: applicant/co-applicant income, loan amount & term, credit history, employment, education, marital status, property area  
Target: `Loan_Status` (Approved/Denied)

## Workflow
1. **EDA** – distributions, missing values, correlations, class balance  
2. **Preprocessing** – handle nulls, encode categoricals, scale numerics, address imbalance  
3. **Modeling**  
   - Logistic Regression with hyperparameter tuning & cross‑validation  
   - XGBoost with grid search and early stopping  
4. **Evaluation** – Accuracy, Precision, Recall, F1, ROC‑AUC, confusion matrix  
5. **Interpretability**  
   - LR coefficients/odds ratios  
   - XGBoost feature importance & SHAP values

## Usage
1. Install Python dependencies (scikit-learn, xgboost, pandas, numpy, seaborn, shap).  
2. Run the notebook or script:
   ```bash
   jupyter notebook Loan_Approval_Model_Comparison.ipynb
