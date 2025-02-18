from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message='This is running Pythons Flask for backend')

if __name__ == '__main__':
    app.run(port=5000)