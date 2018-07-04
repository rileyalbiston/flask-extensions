# Start a Basic Flask App

Flask is a microframework meaning it comes with minimal components which makes it super simple to setup and get started. Extensions are added as required. 

To install Flask (you will need the python pip package manager) open a terminal and type:

```
pip install Flask
```

To get started create a project directory and a file within called ```main.py``` (it can be called whatever you want but I like main because it's easy to remember). Then in the ```main.py``` type:

```
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
	app.run(debug=True, port=5000)
```

Then to start open a terminal at the project directory and type:

```
python main.py
```

Now open a browser and visit:

<http://127.0.0.1:5000/>


Flask uses ```routes``` to create new pages. To add another page to the app change the ```main.py``` file to:

```
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/page-1")
def about():
    return "<h1>Hello Page 1</h1>"


if __name__ == '__main__':
	app.run(debug=True, port=5000)
```

When you save the file the sever should restart. If the page doesn't load check the terminal to make sure the server is still running. If not it should display any errors. Fix these and restart using ```python main.py```.

To visit the new page visit:

<http://127.0.0.1:5000/page-1>

Done! Setting up a basic app in Flask is that easy. Now to make it done anything more useful you'll probably need to add extensions. It is this flexibility and modularity which makes Flask easy to work with, particularly for smaller projects.

