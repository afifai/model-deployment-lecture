from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("pipeline_new.pkl", "rb") as f:
    model = pickle.load(f)

columns = ['Pclass',  'Fare', 'Age', 'SibSp', 'Parch', 'Sex']
classes = ['Not Survived', 'Survived']

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data= [content['passenger_class'],
                   content['fare'],
                   content['age'],
                   content['siblingspouse'],
                   content['parentchildren'],
                   content['gender']]
            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":str(res[0]),
                                   "description":classes[res[0]]}}
            return jsonify(response)
        except Exception as e:
            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Silahkan gunakan method POST untuk mengakses hasil prediksi dari model</p>"