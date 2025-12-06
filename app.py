import streamlit as st
import numpy as np
import pandas as pd
import joblib

# --- 1. LOAD MODEL ---
try:
    model = joblib.load('models/random_forest_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please run the notebook to save the model first.")
    st.stop()

st.title("🚨 Credit Card Fraud Detection System")
st.write("Enter transaction details to check for fraud risk.")

# --- 2. INPUTS ---
st.subheader("Transaction Details")

# Amount Input
amount = st.number_input("Transaction Amount ($)", min_value=0.0, max_value=30000.0, value=100.0)

st.write("---")
st.write("**Technical Features (PCA)**")
st.caption("Adjust these parameters. (Tip: Set V14 to around -15.0 to simulate fraud).")

# Use Columns and Number Inputs for precision
col1, col2, col3 = st.columns(3)

with col1:
    v14 = st.number_input("V14 (Neg. Correlation)", min_value=-20.0, max_value=20.0, value=0.0)

with col2:
    v4 = st.number_input("V4 (Pos. Correlation)", min_value=-20.0, max_value=20.0, value=0.0)

with col3:
    v11 = st.number_input("V11 (Pos. Correlation)", min_value=-20.0, max_value=20.0, value=0.0)

# --- 3. PREDICTION LOGIC ---

# Initialize a list of 30 zeros (representing all features set to average)
input_data = [0] * 30 

# Map User Inputs to the Correct Indices
# Index 0: scaled_amount, Index 5: V4, Index 12: V11, Index 15: V14
input_data[0] = amount  
input_data[5] = v4      
input_data[12] = v11    
input_data[15] = v14    

# "Correlation Logic" (The Fix)
# If the user sets V14 to a "Fraud" level (e.g., < -5), we infer that 
# other correlated features (V10, V12, V17) would also be abnormal.
if v14 < -5:
    input_data[11] = -5.0   # V10 usually drops with V14
    input_data[13] = -5.0   # V12 usually drops with V14
    input_data[18] = -5.0   # V17 usually drops with V14

# Debugging: Show the user what is being sent to the model
with st.expander("See Raw Input Data"):
    st.write(f"Input Array: {input_data}")

# Convert to numpy array
features = np.array([input_data])

# --- 4. DETECT FRAUD BUTTON (Enhancement 1: Risk Probability) ---
if st.button("Detect Fraud"):
    
    # Get the PROBABILITY (The confidence score)
    # This returns an array like [0.10, 0.90] -> [Safe%, Fraud%]
    probability = model.predict_proba(features)
    fraud_probability = probability[0][1] * 100 # Convert to percentage

    # Display Logic
    st.write("---")
    st.subheader("Analysis Result")
    
    # Create a progress bar for Risk
    st.write(f"**Fraud Risk Score:** {fraud_probability:.2f}%")
    st.progress(int(fraud_probability))

    # Threshold for Alert (usually 50%, but banks might use lower)
    if fraud_probability > 50:
        st.error(f"🚨 FRAUD DETECTED! (Risk: {fraud_probability:.2f}%)")
        st.write("Reason: High deviation in V14/V4/V11 patterns.")
    else:
        st.success(f"✅ Legitimate Transaction (Risk: {fraud_probability:.2f}%)")
        st.balloons()

# --- 5. BATCH PROCESSING (Enhancement 2: Bank Mode) ---
st.write("---")
st.header("📂 Batch Transaction Processing")
st.write("Upload a CSV file containing transaction data to scan multiple checks at once.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Load the user's CSV
    batch_df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", batch_df.head())
    
    if st.button("Scan All Transactions"):
        try:
            # We need to ensure we drop the 'Class' label if it exists (since we are predicting it)
            if 'Class' in batch_df.columns:
                X_batch = batch_df.drop('Class', axis=1)
            else:
                X_batch = batch_df
            
            # NOTE: In a real app, you would need to ensure the columns align perfectly 
            # with the 30 columns the model expects. For this demo, we assume the CSV is correct.
            
            # Predict
            predictions = model.predict(X_batch)
            batch_df['Fraud_Prediction'] = predictions
            
            # Filter only the Frauds
            frauds = batch_df[batch_df['Fraud_Prediction'] == 1]
            
            if len(frauds) > 0:
                st.error(f"Scan Complete! Found {len(frauds)} suspicious transactions.")
                st.dataframe(frauds) # Show only the bad guys
            else:
                st.success("Scan Complete! No fraudulent transactions found.")
            
        except Exception as e:
            st.error(f"Error processing batch: {e}")
            st.info("Make sure your CSV columns match the training data (V1-V28, Amount, Time).")