from flask import Flask, request, jsonify

URL = "https://www.learningconainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

def import():
        get = URL
        return

app = Flask(__name__)

@app.route('/func', methods=['GET',])
def func():
    data = request.json
    return jsonify(data)
    
@app.route('/manage_file', methods=['POST'])
def func2():
        if payload = request.get_json()
        else: status error
        return

def func3():
        if payload['action'] == 'read':
                return flask.jsonify 200
        else:
                return flask.jsonify 500
        
        
