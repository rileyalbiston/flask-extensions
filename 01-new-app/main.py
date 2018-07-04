from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/page-1")
def about():
    return "Hello Page 1"


if __name__ == '__main__':
	app.run(debug=True, port=5000)