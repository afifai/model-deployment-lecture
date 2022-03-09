# model deployment using all in one method

import streamlit as st
import pickle
import pandas as pd

with open("final_pipe.pkl", "rb") as model_file:
    model = pickle.load(model_file)

columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
label = ['Not Survived', 'Survived']

st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.number_input("Passenger Class")
age = st.number_input("Age")
sibsp = st.number_input("Sibling / Spouse")
parch = st.number_input("Parent / Children")
sex = st.selectbox("Gender", ['male', 'female'])
# sex = st.text_input("Gender")
# inference
new_data = [pclass, sex, age, sibsp, parch]
new_data = pd.DataFrame([new_data], columns=columns)
res = model.predict(new_data)
st.title(label[res[0]])