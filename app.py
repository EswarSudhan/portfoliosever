from flask import Flask, render_template

app = Flask(__name__)
x="innum illa"
@app.route('/', methods=['GET'])
def index():
    return x
@app.route('/mapla', methods=['GET'])
def mapla():
    return "Maja mapla"
@app.route('/post', methods=['POST'])
def maplapost():
    x="post aiduchu"
    return "post aiduchu"


if __name__ == '__main__':
    app.run(debug=True)
