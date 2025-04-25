import streamlit as st
import pandas as pd
import pickle

# Load your model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict if it's fraud or not.")

# User input form
with st.form("fraud_form"):
    v1 = st.number_input("V1")
    v2 = st.number_input("V2")
    v3 = st.number_input("V3")
    v4 = st.number_input("V4")
    amount = st.number_input("Transaction Amount")
    
    submitted = st.form_submit_button("Predict")

if submitted:
    # Make a prediction
    input_df = pd.DataFrame([[v1, v2, v3, v4, amount]],
                            columns=["V1", "V2", "V3", "V4", "Amount"])
    prediction = model.predict(input_df)[0]
    result = "🚨 Fraud Detected!" if prediction == 1 else "✅ Transaction Safe"

    st.subheader("Prediction Result:")
    st.success(result) if prediction == 0 else st.error(result)
