# pip install Flask-User<0.7
from datetime import datetime
from flask import Flask, render_template, url_for,  flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/dev_db'
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False # change to True later
db = SQLAlchemy(app)

class UserAccount(db.Model, UserMixin):
    __tablename__ = 'user_account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')


db_adapter = SQLAlchemyAdapter(db, UserAccount)
user_manager = UserManager(db_adapter, app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.data_posted}')"


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
    return render_template("home.html", posts=posts)


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


@app.route("/login" , methods=['GET', 'POST'])
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