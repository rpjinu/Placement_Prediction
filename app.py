import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r'C:\Users\Ranjan kumar pradhan\.vscode\placement_model.pkl')

# Streamlit app
st.title("Placement Prediction App")

# User input form
st.header("Enter Candidate Details:")
iq = st.number_input("IQ", min_value=0.0, step=1.0)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
communication_skill = st.number_input("Communication Skill (1-10)", min_value=1, max_value=10, step=1)
technical_skill = st.number_input("Technical Skill (1-10)", min_value=1, max_value=10, step=1)
extracurricular_activity = st.number_input("Extracurricular Activity (1-10)", min_value=1, max_value=10, step=1)
internship_experience = st.number_input("Internship Experience (1-10)", min_value=1, max_value=10, step=1)
leadership_skill = st.number_input("Leadership Skill (1-10)", min_value=1, max_value=10, step=1)

# Button for prediction
if st.button("Predict Placement"):
    # Prepare the input for prediction
    input_data = np.array([[iq, cgpa, communication_skill, technical_skill, 
                            extracurricular_activity, internship_experience, leadership_skill]])
    
    # Predict the outcome
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.success("The candidate is likely to be get  placement.")
    else:
        st.error("The candidate is not likely to be get placement.")

