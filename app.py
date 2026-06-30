import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>📊 Customer Churn Prediction Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# =====================================================
# 🔧 MANUAL INPUT (SCROLL SELECT)
# =====================================================
st.sidebar.header("🔧 Manual Input (Scroll Select)")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 5)
monthly_charges = st.sidebar.slider("Monthly Charges", 0.0, 200.0, 120.0)

st.subheader("🔮 Manual Prediction Result")

if st.sidebar.button("Predict Churn"):

    # ✅ correct input dataframe
    input_df = pd.DataFrame(
        [[tenure, monthly_charges]],
        columns=model.feature_names_in_
    )

    # ✅ probability-based decision
    churn_prob = model.predict_proba(input_df)[0][1]

    st.write(f"Churn Probability: **{churn_prob:.2f}**")

    if churn_prob > 0.3:   # 👈 threshold lowered
        st.error(f"🔴 Customer WILL CHURN ({churn_prob*100:.1f}%)")
    else:
        st.success(f"🟢 Customer will NOT churn ({(1-churn_prob)*100:.1f}%)")

st.markdown("---")

# =====================================================
# 📁 CSV UPLOAD & BULK PREDICTION
# =====================================================
st.subheader("📁 Upload CSV for Bulk Prediction")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Original CSV Preview", df.head())

    # ✅ keep only training features
    required_features = list(model.feature_names_in_)
    df_model = df[required_features]

    # predictions
    df["Churn_Prediction"] = model.predict(df_model)

    st.success("✅ Prediction completed")

    # ---------------- CHARTS ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Churn Distribution")
        fig, ax = plt.subplots()
        df["Churn_Prediction"].value_counts().plot(
            kind="bar", ax=ax, color=["green", "red"]
        )
        ax.set_xticklabels(["Not Churn", "Churn"], rotation=0)
        st.pyplot(fig)

    with col2:
        st.subheader("📈 Monthly Charges vs Churn")
        fig, ax = plt.subplots()
        sns.boxplot(x="Churn_Prediction", y="MonthlyCharges", data=df, ax=ax)
        st.pyplot(fig)

    # ---------------- DOWNLOAD ----------------
    st.markdown("### ⬇ Download Results")
    st.download_button(
        "Download CSV with Predictions",
        df.to_csv(index=False),
        file_name="churn_predictions.csv",
        mime="text/csv"
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with Streamlit | Customer Churn ML Project</p>",
    unsafe_allow_html=True
)