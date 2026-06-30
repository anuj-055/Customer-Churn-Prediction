# Customer-Churn-Prediction
# customer-churn-prediction
# 📊 Customer Churn Prediction Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive Machine Learning dashboard that predicts whether a customer is likely to **churn** or **not** based on customer tenure and monthly charges.

This project demonstrates data preprocessing, machine learning prediction, and visualization using a user-friendly **Streamlit** interface.

---

## 📸 Application Screenshots

### 🏠 Dashboard
Main dashboard showing manual input sliders, prediction result, and charts.

![Dashboard](dashboard1.png)

---

### 🔮 Manual Churn Prediction
Prediction result displayed with **Red (Churn)** and **Green (No Churn)** indicators.

![Prediction](prediction1.png)

---

### 📊 CSV Upload & Results
Bulk churn prediction using CSV upload with visual charts.

![CSV Results](csv_results1.png)
![CSV Results](csv_results2.png)


---

## 🌐 Live Demo

*Application:*  
https://customer-churn-prediction-cypvymrrt3nzmchr3awezy.streamlit.app/

---

## 🧠 Model Details

- Algorithm: **Random Forest Classifier**
- Input Features:
  - `tenure`
  - `MonthlyCharges`
- Output:
  - `1` → Customer WILL churn
  - `0` → Customer will NOT churn

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
