from flask import Flask,  jsonify, request

app = Flask(__name__)
@app.route("/api/data")
def get_data():
    data = {
        'nome': 'wagner',
        'idaade': 33,
        'profissao': 'desempregado'
    }
    
    return jsonify(data)

@app.route("/api/data", methods=['POST'])
def process_data():
    data = request.get_json()
    
    response = {'status':'success'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)