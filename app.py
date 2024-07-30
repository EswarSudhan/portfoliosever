from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "success"
@app.route('/mapla', methods=['GET'])
def mapla():
    return "Maja mapla"


if __name__ == '__main__':
    app.run(debug=True)
