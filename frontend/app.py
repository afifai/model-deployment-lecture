import streamlit as st
import requests


st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.number_input("Passenger Class")
age = st.number_input("Age")
sibsp = st.number_input("Sibling / Spouse")
parch = st.number_input("Parent / Children")
# sex = st.selectbox("Gender", ['male', 'female'])
sex = st.text_input("Gender")
# inference
data = {'passenger_class':pclass,
        'age': age,
        'siblingspouse':sibsp,
        'parentchildren':parch,
        'gender':sex}

URL = "https://h8-backend-deployment.herokuapp.com/predict"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['data']['result']['target_names'])
else:
    st.write("Mohon maaf terjadi kesalahan")
    st.write(f"keterangan : {res['summary']}")