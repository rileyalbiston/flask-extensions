from flask import Flask, render_template
app = Flask(__name__)


posts = [
	{
		'author': 'Bob',
		'title': 'Post 1',
		'content': 'Nulla vitae fringilla elit. Aenean pretium tempus velit at egestas. Cras eget enim dolor.',
		'data_posted': '02-05-2018'
	},
	{
		'author': 'Barry',
		'title': 'Post 2',
		'content': 'Nunc volutpat dolor id bibendum lacinia. In hac habitasse platea dictumst. Etiam tincidunt est eleifend, porta.',
		'data_posted': '24-09-2018'
	}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home Page", posts=posts)


@app.route("/page-1")
def page_1():
    return render_template("page-1.html", title="Page 1", post=posts[0])


if __name__ == '__main__':
	app.run(debug=True)