# dashboard.py
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# --- Data Loading & Model Training ---
# This section is copied from your analyze_data.py script
@st.cache_data
def load_data_and_train_model():
    # Load the JSON file
    df_raw = pd.read_json('sensor_data.json')
    data = [item['fields'] for item in df_raw.to_dict('records')]
    df_processed = pd.DataFrame(data)
    df_processed['timestamp'] = pd.to_datetime(df_processed['timestamp'])
    
    # Pivot and fill missing values
    df_wide = df_processed.pivot_table(
        index=pd.Grouper(key='timestamp', freq='min'),
        columns='reading_type',
        values='reading_value',
        aggfunc='mean'
    ).reset_index()
    df_wide = df_wide.fillna(0)

    # Manually add a clear failure case to the DataFrame
    failure_case = pd.DataFrame({
        'timestamp': [pd.Timestamp('2025-08-03 12:30:00+00:00')],
        'current': [10.5],
        'temperature': [40.2],
        'vibration': [2.1],
        'voltage': [220.0]
    })
    df_wide = pd.concat([df_wide, failure_case], ignore_index=True)

    # Create the target variable
    df_wide['failure'] = (df_wide['temperature'] > 35).astype(int)

    # Separate features and target
    X = df_wide.drop(['timestamp', 'failure'], axis=1)
    y = df_wide['failure']

    # Train the model on the full dataset
    model = DecisionTreeClassifier()
    model.fit(X, y)
    
    return df_wide, model, X.columns

# Load data and train model
df_wide, model, feature_names = load_data_and_train_model()

# --- Dashboard UI ---
st.title("Smart Grid Sensor Dashboard")
st.markdown("Monitor real-time sensor data and get predictive failure alerts.")

# Display the data table
st.subheader("Raw Sensor Data (Last 5 Minutes)")
st.dataframe(df_wide.tail(5))

# Create a section for live predictions
st.subheader("Predictive Failure Alert")
col1, col2, col3, col4 = st.columns(4)

with col1:
    current = st.slider("Current", 0.0, 15.0, 2.8)
with col2:
    temperature = st.slider("Temperature", 0.0, 50.0, 36.0)
with col3:
    vibration = st.slider("Vibration", 0.0, 5.0, 0.45)
with col4:
    voltage = st.slider("Voltage", 200.0, 240.0, 220.0)

if st.button("Predict Failure"):
    new_data_point = pd.DataFrame([[current, temperature, vibration, voltage]], columns=feature_names)
    prediction = model.predict(new_data_point)[0]
    
    if prediction == 1:
        st.error("🚨 **ALERT!** Predictive Failure Detected!")
    else:
        st.success("✅ **STATUS:** System Operating Normally.")

# Display the temperature plot
st.subheader("Temperature Readings Over Time")
st.line_chart(df_wide.set_index('timestamp')['temperature'])