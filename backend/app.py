from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("final_pipe.pkl", "rb") as model_file:
    model = pickle.load(model_file)

columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
classes = ['Not Survived', 'Survived']


@app.route("/") # home page
def hello_world():
    return "<h1>It Works</h1>"

@app.route("/predict", methods=['GET', 'POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        
        try:
            data = [content['passenger_class'],
                    content['gender'],
                    content['age'],
                    content['siblingspouse'],
                    content['parentchildren']]
            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {'code':200,
                        'status':"OK",
                        'data':{'result':{'target':str(res[0]),
                                        'target_names':classes[res[0]]}}}
            return jsonify(response)
        except Exception as e:
            response = {'code':500,
                        'status':"error",
                        'summary': str(e)}
            return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses hasil prediksi dari model"