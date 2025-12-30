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

🛠️ **Tech Stack**
**Language**: Python 3.9
**Machine Learning**: Scikit-Learn, Imbalanced-Learn (SMOTE)
**Web Framework**: Streamlit
**Containerization**: Docker✨

**Key Features**
**Real-time Detection**: Immediate classification of transactions via web UI.
**Batch Auditing**: Support for CSV uploads to process bulk historical data.
**High Recall Optimization**: Specifically tuned to minimize missed fraud cases (False Negatives).
**Risk Engine**: Provides probability scores rather than just binary labels.

📊 **Performance Metrics**
 **Metric** **Score** **Significance**
   Recall      82%       Captures 82% of all actual fraud attempts.
   Precision   85%       Ensures legitimate users are rarely blocked.
   ROC-AUC     0.96      Excellent distinction between fraud and safe classes.

## 🔒 Data Privacy & PCA Features
Due to confidentiality issues, the original features of the dataset (such as location, merchant category, or cardholder name) are not provided. 

Instead, the dataset contains **28 numerical input variables (V1–V28)**:
* **Principal Components**: These features are the result of a **PCA transformation**, which compresses high-dimensional data while preserving the most important patterns.
* **Non-transformed Features**: Only `Time` and `Amount` remain in their original form.
* **Significance**: Our analysis shows that features like **V14, V4, and V11** carry the highest correlation with fraudulent activity, making them critical for the model's "Risk Engine."

🏗️ **Getting Started**

**Prerequisites**
Python 3.9 or higher
Docker (Optional for containerized run)

**Setup Instructions**
1.*Clone & install*
```bash
   git clone [https://github.com/subhrank09/fraud-detection-system.git](https://github.com/subhrank09/fraud-detection-system.git)
   cd fraud-detection-system
   pip install -r requirements.txt

2.*Run Application*
```bash
   streamlit run app.py

3.*Run Via Docker*
```bash
   docker build -t fraud-app .
   docker run -p 8501:8501 fraud-app

🧪 **Testing Scenarios**

Use these "Cheat Codes" in the app to test the model:
Scenario          Amount   V14   V4   Expected Result
Safe Transaction  100.0    0.0   0.0   ✅ Legitimate
Card Testing      1.00    -15.0  8.0   🚨 FRAUD
High Value Theft 5000.0   -18.0  12.0  🚨 FRAUD

Author: Subhrank Priya
