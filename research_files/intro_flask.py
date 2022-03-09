from flask import Flask, jsonify, request

app = Flask(__name__)

my_dict = {'nama':'Afif',
           'usia': 18,
           'pekerjaan':'data_scientist'}

@app.route("/") # home page
def hello_world():
    return jsonify(my_dict)

@app.route('/input', methods=['POST'])
def input_data():
    global my_dict
    content = request.json
    my_dict['nama'] = content['nama']
    my_dict['usia'] = content['usia']
    my_dict['pekerjaan'] = content['pekerjaan']

app.run()