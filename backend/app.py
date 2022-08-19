from flask import Flask, jsonify, request
import pickle
import pandas as pd

# init app
app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, "rb") as modelfile:
        model = pickle.load(modelfile)
    return model

def iris_inference(data, model):
    """
    input : list with length 4 --> [sepal_length, sepal_width, petal_length, petal_width]
    output : predicted class : (idx, label)
    """
    LABEL = ('Setosa', 'Versicolor', 'Virginica')
    res = model.predict([data])
    return res[0], LABEL[res[0]]

def titanic_inference(data, model):
    """
    input : list with length 6 --> ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    output : predicted class : (idx, label)
    """
    LABEL = ["Not Survived", "Survived"]
    columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    data = pd.DataFrame([data])
    data.columns = columns
    res = model.predict(data)
    return res[0], LABEL[res[0]]

model_iris = open_model("iris_pipeline.pkl")
model_titanic = open_model("titanic_pipeline.pkl")

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/predict/iris")
def iris_predict():
    args = request.args
    sl = args.get("sl", type=float, default=0)
    sw = args.get("sw", type=float, default=0)
    pl = args.get("pl", type=float, default=0)
    pw = args.get("pw", type=float, default=0)
    new_data = [sl, sw, pl, pw]
    idx, label = iris_inference(new_data, model_iris)
    response = jsonify(result=str(idx), label_names=label)
    return response

@app.route("/predict/titanic", methods=['POST'])
def titanic_predict():
    args = request.json
    passenger_class = args.get('passenger_class')
    gender = args.get('gender')
    age = args.get('age')
    sibling_spouse = args.get('sibling_spouse')
    parent_children = args.get('parent_children')
    fare = args.get('fare')
    new_data = [passenger_class, gender, age, sibling_spouse, parent_children, fare]
    idx, label = titanic_inference(new_data, model_titanic)
    response = jsonify(result=str(idx), label_names=label)
    return response

# jika deploy ke heroku, komen baris dibawah
# app.run(debug=True)