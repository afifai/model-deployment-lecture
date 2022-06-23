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

# URL = "http://127.0.0.1:5000/titanic_prediction" # sebelum push backend
URL = "https://model-deployment-backend.herokuapp.com/titanic_prediction" # URL Heroku

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['label_name'])
else:
    st.title("ERROR BOSS")
    st.write(res['message'])