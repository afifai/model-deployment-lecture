import streamlit as st
import requests


st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.selectbox("Passenger Class", [1, 2, 3])
fare = st.number_input("Fare")
age = st.number_input("Age")
sibsp = st.number_input("Sibling / Spouse")
parch = st.number_input("Parent / Children")
sex = st.selectbox("Gender", ['male', 'female'])
# inference
data = {'passenger_class':pclass,
        'fare':fare,
        'age': age,
        'sibling_spouse':sibsp,
        'parent_children':parch,
        'gender':sex}

URL = "https://h8-model-deployment-backend.herokuapp.com/titanic"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result']['classes'])