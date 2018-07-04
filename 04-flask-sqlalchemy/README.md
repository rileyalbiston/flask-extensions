
```mkdir flask_sqlalchemy_sqlite```

```cd flask_sqlalchemy_sqlite```

```virtualenv venv```

```source venv/bin/activate```

```pip install Flask```

```pip install Flask-SQLAlchemy```

```pip freeze > requirements.txt```

```touch main.py```


## Create Database From Terminal

```
python3
>>> from main import db
>>> db.create_all()
```

## using sqlite3 in the terminal

```$ sudo apt install sqlite3```

```
riley@riley-Lenovo-G50-30:~$ cd '/home/riley/flask_sqlalchemy_sqlite'
riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ sqlite3 test.db
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite> .tables
test
sqlite>
```

## Install Sqlite Browser

sudo apt-get install sqlitebrowser

launch:
sqlitebrowser

## Test Insert in Terminal

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import Test
>>> from main import db
>>> new = Test(1, 'First Entry')
>>> db.session.add(new)
>>> db.session.commit()
```

## Test Update in Terminal

```
>>> update = Test.query.filter_by(id=1).first()
>>> update.data = 'Updated entry'
>>> db.session.commit()
```

## Test Delete in Terminal

```
>>> delete = Test.query.filter_by(id=1).first()
>>> db.session.delete(delete)
>>> db.session.commit()
```

## create one-to-many relationships 

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import db
>>> db.create_all()
>>> db.session.commit()
```

#### create data for the new tables

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import db
>>> from main import Owner, Motorcycle
>>> owner_one = Owner(name='Riley')
>>> owner_two = Owner(name='Marcus')
>>> db.session.add(owner_one)
>>> db.session.add(owner_two)
>>> db.session.commit()
# add motorcycles with owner relationship
>>> motorcycle_one = Motorcycle(make='XR650R', owner=owner_one)
>>> db.session.commit()
>>> motorcycle_two = Motorcycle(make='DR650', owner=owner_two)
>>> motorcycle_three = Motorcycle(make='NC700', owner=owner_two)
>>> db.session.commit()
```

#### Query the One-To-Many Relationship in the Terminal

```
>>> r = Owner.query.filter_by(name='Riley').first()
>>> r.name
'Riley'
>>> r.motorcycles
<sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x7f0fd8101978>
>>> r.motorcycles.all()
[<Motorcycle 1>]
>>> for bike in r.motorcycles.all():
...     print(bike.make)
... 
XR650R

>>> r2 = Owner.query.filter_by(name='Marcus').first()
>>> r2.name
'Marcus'
>>> for bike in r2.motorcycles.all():
...     print(bike.make)
... 
DR650
NC700
```

```
>>> rv = Motorcycle.query.filter_by(owner_id=2).first()
>>> rv
<Motorcycle 2>
>>> rv.make
'DR650'
>>> rv = Motorcycle.query.filter_by(owner_id=2).all()
>>> rv
[<Motorcycle 2>, <Motorcycle 3>]
>>> for i in rv:
...     print(i.make)
... 
DR650
NC700 
```

## SQLAlchemy Migrations with Flask-Migrate

```pip install flask-migrate```

```pip install Flask-Script```

```pip freeze > requirements.txt```


##### Setup and Run Migration

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3 main.py db init

(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3 main.py db migrate

(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3 main.py db upgrade
```

#### Modify a table by adding a column

After changing model class run:

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3 main.py db migrate

(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3 main.py db upgrade
```

## Many-to_Many Relationships

Run migration

```
(venv) riley@riley-Lenovo-G50-30:~/flask_sqlalchemy_sqlite$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import *
```

create some data

```
>>> auth1 = Author(name='Bob')
>>> auth2 = Author(name='Frank')
>>> db.session.add_all([auth1, auth2])
>>> db.session.commit()
>>> book1 = Book(title='First Book')
>>> book2 = Book(title='Second Book')
>>> book3 = Book(title='Third Book')
>>> db.session.add_all([book1, book2, book3])
>>> db.session.commit()
```

create relation with back reference

```
>>> book1.writers.append(auth1)
>>> db.session.commit()
>>> book3.writers.append(auth2)
>>> db.session.commit()
>>> book2.writers.append(auth1)
>>> book2.writers.append(auth2)
>>> db.session.commit()
```

Query the many-to-many relationship

```
>>> for auth in book2.writers:
...     print(auth.name)
... 
Bob
Frank
>>> 
```








