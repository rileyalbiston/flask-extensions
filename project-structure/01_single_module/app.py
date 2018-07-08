from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object('config')
app.config["DEBUG"]



@app.route("/")
def home():
    return render_template("home.html", title="Home Page")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == '__main__':
	app.run()