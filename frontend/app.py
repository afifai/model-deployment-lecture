import streamlit as st
import requests

st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.selectbox("Passenger Class", [1, 2, 3])
fare = st.number_input("Fare")
age = st.number_input("Age")
sibsp = st.number_input("Sibling Spouse")
parch = st.number_input("Parent Children")
gender = st.selectbox("Gender", ["male", "female"])

# inference
URL = "https://backend-model-deployment.herokuapp.com/predict/titanic"
param = {'passenger_class': pclass,
         'gender': gender,
         'age' : age,
         'sibling_spouse' :sibsp,
         'parent_children' : parch,
         'fare' : fare}
r = requests.post(URL, json=param)

if r.status_code == 200:
    res = r.json()
    st.title(res['label_names'])
else:
    st.title("Unexpected Error")