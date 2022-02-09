import streamlit as st
import requests

URL = "https://backend-model-deployment-afif.herokuapp.com/predict"


st.title("Aplikasi Pedeteksi Bunga Iris")
sl = st.number_input("Sepal Length")
sw = st.number_input("Sepal Width")
pl = st.number_input("Petal Length")
pw = st.number_input("Petal Width")

# param input
# URL = URL + f"?sl={sl}&sw={sw}&pl={pl}&pw={pw}"
data = {'sl':sl,
        'sw':sw,
        'pl':pl,
        'pw':pw}

# komunikasi
r = requests.post(URL, json=data)

res = r.json()

st.write(f"Hasil Prediksi : {res['data']['result']}")