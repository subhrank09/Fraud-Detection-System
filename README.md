# 🛡️ Fraud Guard AI

> **A high-precision machine learning system designed to detect and prevent fraudulent transactions in real-time.**

[![Live Demo](https://img.shields.io/badge/demo-live-red?style=for-the-badge)](https://subhrank09-fraud-detection-system-app-sxbdtu.streamlit.app/)

---

## 🚀 Project Overview
Fraud Guard AI is built to tackle the challenges of financial security. It leverages a **Random Forest Classifier** and **SMOTE** oversampling to identify fraudulent patterns within highly imbalanced credit card datasets.

## 🔄 System Workflow
```mermaid
graph LR
    A[User Input / CSV Upload] -->|Raw Data| B(Preprocessing Phase)
    B -->|Scaling & Encoding| C{Random Forest Model}
    C -->|Probability Score| D[Risk Engine]
    D -- Score > 50% --> E[🚨 FRAUD ALERT]
    D -- Score < 50% --> F[✅ Safe Transaction]
    style E fill:#ff4b4b,stroke:#333,stroke-width:2px,color:white
    style F fill:#00c853,stroke:#333,stroke-width:2px,color:white
🛠️ Tech StackLanguage: Python 3.9Machine Learning: Scikit-Learn, Imbalanced-Learn (SMOTE)Web Framework: StreamlitContainerization: Docker✨ Key FeaturesReal-time Detection: Immediate classification of transactions via web UI.Batch Auditing: Support for CSV uploads to process bulk historical data.High Recall Optimization: Specifically tuned to minimize missed fraud cases (False Negatives).Risk Engine: Provides probability scores rather than just binary labels.📊 Performance MetricsMetricScoreSignificanceRecall82%Captures 82% of all actual fraud attempts.Precision85%Ensures legitimate users are rarely blocked.ROC-AUC0.96Excellent distinction between fraud and safe classes.🔒 Data Privacy & PCA FeaturesDue to confidentiality, original features (location, merchant, etc.) are hidden. The dataset contains 28 numerical variables (V1–V28).Principal Components: Features result from a PCA transformation to preserve patterns while anonymizing data.Non-transformed: Only Time and Amount remain in their original form.Significance: Features like V14, V4, and V11 carry the highest correlation with fraudulent activity.🏗️ Getting StartedPrerequisitesPython 3.9 or higherDocker (Optional)Setup InstructionsClone & InstallBashgit clone [https://github.com/subhrank09/fraud-detection-system.git](https://github.com/subhrank09/fraud-detection-system.git)
cd fraud-detection-system
pip install -r requirements.txt
Run ApplicationBashstreamlit run app.py
Run via DockerBashdocker build -t fraud-app .
docker run -p 8501:8501 fraud-app
🧪 Testing ScenariosUse these values in the app to test the model:ScenarioAmountV14V4Expected ResultSafe Transaction100.00.00.0✅ LegitimateCard Testing1.00-15.08.0🚨 FRAUDHigh Value Theft5000.0-18.012.0🚨 FRAUDAuthor: Subhrank Priya
