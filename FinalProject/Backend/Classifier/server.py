from flask import Flask, request, Blueprint, jsonify
import string
import random
from flask_cors import CORS,cross_origin
from run import predict

app = Flask(__name__)
cors = CORS(app)

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route('/all', methods=['POST'])
@cross_origin()
def full_process():
    # return "Hello World from Flask"
    try:
        if request.method == 'POST':
            recived_json = request.get_json()
            print(f"{recived_json=}")
            if recived_json:
                s = recived_json['data']
            else:
                return "Invalid Input"
            result = predict(s)
            print('result',result)
            print(type(result))
            return result
        else:
            return False

    except Exception as e:
        print(e)
        return str(e)

# @app.route('/train-model', methods=['POST'])
# def train():
#     try:
#         if request.method == 'POST':
#             result = train_model()
#             print('result',result)
#             return str(result)
#         else:
#             return "False"

#     except Exception as e:
#         print(e)
#         return e

@app.route('/predict', methods=['POST'])
def predict_taxonomy():
    try:
        if request.method == 'POST':
            # f = request.files['file']
            # random_file_name = 'received_files/'+randomString()+'.pdf'
            # f.save(random_file_name)
            recived_json = request.get_json()
            if recived_json:
                s = recived_json['data']
            else:
                return "Invalid Input"
            result = predict(s)
            print('result',result)
            return result
        else:
            return False

    except Exception as e:
        print(e)
        return e

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True,port="3100")