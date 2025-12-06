# 🚨 Real-Time Credit Card Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red) ![Docker](https://img.shields.io/badge/Docker-Ready-blue) ![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
A machine learning-based application designed to detect fraudulent credit card transactions in real-time. The system handles massive class imbalance (0.17% fraud rate) using **SMOTE** and achieves an **82% Recall rate**, minimizing financial loss while maintaining user experience.

## 🏗️ System Architecture
```mermaid
graph LR
    A[User Input / Batch CSV] -->|Raw Data| B(Preprocessing Phase)
    B -->|Scaling & Encoding| C{Random Forest Model}
    C -->|Probability Score| D[Risk Engine]
    D -- Score > 50% --> E[🚨 FRAUD ALERT]
    D -- Score < 50% --> F[✅ Safe Transaction]
    style E fill:#ff4b4b,stroke:#333,stroke-width:2px,color:white
    style F fill:#00c853,stroke:#333,stroke-width:2px,color:white


## 📊 Key Results
| Metric | Score | Importance |
| :--- | :--- | :--- |
| **Recall (Sensitivity)** | **82%** | Captures 82% of all actual fraud cases. |
| **Precision** | **85%** | Low false alarm rate (innocent users aren't blocked). |
| **ROC-AUC** | **0.96** | Excellent discrimination between Safe vs. Fraud. |

## 🛠️ Tech Stack
* **Core:** Python 3.9
* **ML Engine:** Scikit-Learn (Random Forest), Imbalanced-Learn (SMOTE)
* **Interface:** Streamlit (Web App)
* **Containerization:** Docker

## 🚀 How to Run Locally

### Option 1: Using Python
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt