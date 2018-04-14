# Flask-User v0.6 

<https://flask-user.readthedocs.io/en/v0.6/>

<https://flask-user.readthedocs.io/en/v0.6/customization.html>

## Inital Setup

```>``` ```mkdir flask-user```

```>``` ```cd flask-user```

```\flask-user>``` ```git init```

```\flask-user>``` ```echo # Flask Extensions > readme.md```

```\flask-user>``` ```virtualenv venv```

```\flask-user>``` ```venv\scripts\activate```

```(venv) \flask-user>``` ```pip install flask flask-user```

```(venv) \flask-user>``` ```pip freeze > requirements.txt```

```(venv) \flask-user>``` ```echo main program file content > app.py```

Add the following to the app.py file:

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

## Run the Development Server

```flask-user>``` ```python app.py```

```* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```

Visit:

<http://127.0.0.1:5000/>

## Create SQLite Database

```
(venv) \flask-user> python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import db
>>> db.create_all()
>>> exit()
```

## Built in Routes

<http://127.0.0.1:5000/user/register>

<http://127.0.0.1:5000/user/sign-in>

<http://127.0.0.1:5000/user/sign-out>



