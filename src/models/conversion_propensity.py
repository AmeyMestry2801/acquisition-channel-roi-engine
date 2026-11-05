from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
import xgboost as xgb
from src.utils.logger import app_logger
import pickle
import os

def train_logistic_regression(X, y):
    """Train baseline logistic regression"""
    app_logger.info("🤖 Training Logistic Regression...")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)
    
    app_logger.info(f"✅ Logistic Regression AUC-ROC: {auc:.4f}")
    
    print(f"\n🎯 LOGISTIC REGRESSION REPORT:")
    print(classification_report(y_test, model.predict(X_test)))
    
    return model, X_test, y_test, auc

def train_xgboost(X, y):
    """Train XGBoost model"""
    app_logger.info("🚀 Training XGBoost...")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBClassifier(
        n_estimators=100,
        random_state=42,
        early_stopping_rounds=10,
        eval_metric='logloss'
    )
    model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        verbose=False
    )
    
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)
    
    app_logger.info(f"✅ XGBoost AUC-ROC: {auc:.4f}")
    
    print(f"\n🎯 XGBOOST REPORT:")
    print(classification_report(y_test, model.predict(X_test)))
    
    return model, X_test, y_test, auc

def save_model(model, filename):
    """Save trained model"""
    os.makedirs('models', exist_ok=True)
    with open(f'models/{filename}.pkl', 'wb') as f:
        pickle.dump(model, f)
    app_logger.info(f"✅ Model saved: models/{filename}.pkl")
