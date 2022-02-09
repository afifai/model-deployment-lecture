from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
with open("pipeline_iris.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/") # homepage (get)
def model_prediction():
    sl = eval(request.args.get('sl'))
    sw = eval(request.args.get('sw'))
    pl = eval(request.args.get('pl'))
    pw = eval(request.args.get('pw'))
    new_data = [sl, sw, pl, pw]
    res = model.predict([new_data])
    classes = ['setosa', 'versicolor', 'virginica']
    response = {'status':'success',
            'code':200,
            'data':{'result':classes[res[0]]}
            }
    return jsonify(response)

@app.route("/predict", methods=['POST'])
def prediction_post():
    content = request.json
    data = [content['sl'],
            content['sw'],
            content['pl'],
            content['pw']]
    res = model.predict([data])
    classes = ['setosa', 'versicolor', 'virginica']
    response = {'status':'success',
            'code':200,
            'data':{'result':classes[res[0]]}
            }
    return jsonify(response)