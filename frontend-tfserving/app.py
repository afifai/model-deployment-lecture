import json
import pandas as pd
import pickle
import streamlit as st
import requests

# load pipeline
pipe = pickle.load(open("model/preprocess_titanic.pkl", "rb"))

st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.selectbox("Passenger Class", [1, 2, 3])
fare = st.number_input("Fare")
age = st.number_input("Age")
sibsp = st.number_input("Sibling Spouse")
parch = st.number_input("Parent Children")
gender = st.selectbox("Gender", ["male", "female"])

new_data = {'Pclass': pclass,
         'Sex': gender,
         'Age' : age,
         'SibSp' :sibsp,
         'Parch' : parch,
         'Fare' : fare}
new_data = pd.DataFrame([new_data])

# build feature
new_data = pipe.transform(new_data)
new_data = new_data.tolist()

# inference
URL = "http://tfserving-ftds013.herokuapp.com/v1/models/titanic_model:predict"
param = json.dumps({
        "signature_name":"serving_default",
        "instances":new_data
    })
r = requests.post(URL, data=param)

if r.status_code == 200:
    res = r.json()
    if res['predictions'][0][0] > 0.5:
        st.title("Survived")
    else:
        st.title("Not Survived")
else:
    st.title("Unexpected Error")