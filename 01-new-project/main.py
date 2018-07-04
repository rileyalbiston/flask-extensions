from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Index</h1>"


@app.route("/page-1")
def about():
    return "<h1>Page 1</h1>"


if __name__ == '__main__':
	app.run(debug=True, , port=5000)