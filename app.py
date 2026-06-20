import streamlit as st

st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter the passenger details below to check the survival prediction:")

# User Inputs
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], help="1 = Upper, 2 = Middle, 3 = Lower")
sex = st.selectbox("Gender", ["male", "female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare Paid (in USD)", min_value=0.0, max_value=600.0, value=32.0)

# Predict Button
if st.button("Predict Survival Status", type="primary"):
    score = 0
    if sex == "female": score += 60
    if pclass == 1: score += 30
    elif pclass == 2: score += 15
    if age < 12: score += 20
    if fare > 50: score += 10
    
    st.markdown("---")
    if score >= 50:
        st.success("### 🎉 Prediction: Passenger Survived!")
        st.balloons()
    else:
        st.error("### ❌ Prediction: Passenger Did Not Survive.")
      
