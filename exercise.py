from flask import Flask, request, jsonify

URL = "https://www.learningconainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

def import():
        get = URL
        return

app = Flask(__name__)

@app/route('/func', methods=['GET', 'POST'])
def func():
    data = request.json
    return jsonify(data)
    
