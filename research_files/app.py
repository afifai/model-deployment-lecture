from flask import Flask, request, jsonify

app = Flask(__name__)
nama = "Afif"

@app.route("/")
def hello_world():
    return f"<p>Halo {nama}</p>"

@app.route("/ganti", methods=['POST'])
def ganti_nama():
    global nama
    content = request.json
    nama = content['nama']
    response = jsonify(success=True, message=f'Nama sudah diganti menjadi {nama}')
    return response

app.run(debug=True)