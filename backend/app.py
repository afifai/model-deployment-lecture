from flask import Flask, request, jsonify
import pickle
import pandas as pd

# init
app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model

model_iris = open_model("pipeline_iris.pkl")
model_titanic = open_model("titanic_pipe.pkl")

def iris_inference(data, model=model_iris):
    """
    input : list with length 4 --> [sepal_length, sepal_width,
                                    petal_length, petal_width]
    output : predicted class : (idx, label)
    """
    LABEL = ["Setosa", "Versicolor", "Virginica"]
    res = model.predict([data])
    return res[0], LABEL[res[0]]

def titanic_inference(data, model=model_titanic):
    """
    input : list with length 6 --> ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    output : predicted class : (idx, label)
    """
    LABEL = ["Not Survived", "Survived"]
    columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res[0], LABEL[res[0]]

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/iris")
def iris_predict():
    args = request.args
    sl = args.get("sl", type=float, default=0)
    sw = args.get("sw", type=float, default=0)
    pl = args.get("pl", type=float, default=0)
    pw = args.get("pw", type=float, default=0)
    new_data = [sl, sw, pl, pw]
    idx, label = iris_inference(new_data)
    response = jsonify(result=str(idx), label_names=label)
    return response

@app.route("/titanic", methods=['POST'])
def titanic_predict():
    args = request.json
    passenger_class = args.get("passenger_class")
    gender = args.get("gender")
    age = args.get("age")
    sibling_spouse = args.get("sibling_spouse")
    parent_children = args.get("parent_children")
    fare = args.get("fare")
    new_data = [passenger_class, gender, age, sibling_spouse,
                parent_children, fare]
    idx, label = titanic_inference(new_data)
    response = jsonify(result=str(idx), label_names=label)
    return response

# test kode di local
# jika ingin deploy heroku, comment kode dibawah
# app.run(debug=True)