riley@riley-Lenovo-G50-30:~$ ```mkdir flask_wtforms```

riley@riley-Lenovo-G50-30:~$ ```cd flask_wtforms```

riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```virtualenv venv```

riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```source venv/bin/activate```

(venv) riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```pip install Flask```

(venv) riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```pip install Flask-WTF```

(venv) riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```pip freeze > requirements.txt```

(venv) riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```touch main.py```

(venv) riley@riley-Lenovo-G50-30:~/flask_wtforms$ ```touch README.md```

#### In main.py:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

