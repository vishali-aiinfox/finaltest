from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    a = 45
    b = 54
    result = a + b
    return jsonify({
        'a': a,
        'b': b,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
