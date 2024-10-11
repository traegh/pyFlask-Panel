from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    option = data['option']
    text = data['text']
    print(f"{option}: {text}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=False)