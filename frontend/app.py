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
        'siblingspouse':sibsp,
        'parentchildren':parch,
        'gender':sex}

URL = "https://model-deployment9-backend.herokuapp.com/predict"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result']['description'])
else:
    st.write("Mohon maaf terjadi kesalahan")
    st.write(f"keterangan : {res['result']['error_msg']}")