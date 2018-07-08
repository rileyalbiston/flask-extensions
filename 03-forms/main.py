from flask import Flask, render_template, url_for,  flash, redirect
from forms import RegistrationForm, LoginForm, PostsForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '8c1515b90ff4896ec70183b7e5c48b9f'


posts = [
	{
		'author': 'Bob',
		'title': 'Post 1',
		'content': 'Nulla vitae fringilla elit. Aenean pretium tempus velit at egestas. Cras eget enim dolor.'
	},
	{
		'author': 'Barry',
		'title': 'Post 2',
		'content': 'Nunc volutpat dolor id bibendum lacinia. In hac habitasse platea dictumst. Etiam tincidunt est eleifend, porta.'
	}
]


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = PostsForm()
    if form.validate_on_submit():
        posts.append(form.data)
    return render_template("home.html", posts=posts, form=form)


@app.route("/page-1")
def page_1():
    return render_template("page-1.html", title="Page 1")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!')
    	return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	if form.email.data == 'admin@blog.com' and form.password.data == 'password':
    		flash('You have been logged in!')
    		return redirect(url_for('home'))
    	else:
    		flash('Login unsuccsessful')
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
	app.run(debug=True)