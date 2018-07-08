
[Organizing your project](http://exploreflask.com/en/latest/organizing.html)

## Single module

```
project_directory/
	|--app.py
	|--config.py
	|--requirements.txt
	|--static/
	|--templates/
```

## Package

```
project_directory/
	|--config.py
	|--requirements.txt
	|--run.py
	|--instance/
	|   |--config.py
	|--yourapp/
	    |--__init__.py
	    |--views.py
	    |--models.py
	    |--forms.py
	    |--static/
	    |--templates/
```

## Blueprints

[Blueprints](http://exploreflask.com/en/latest/blueprints.html)

**Functional structure**

```
project_directory/
	|--__init__.py
	|--static/
	|--templates/
	|      home/
	|      control_panel/
	|      admin/
	|--views/
	|      __init__.py
	|      home.py
	|      control_panel.py
	|      admin.py
	|--models.py
```

**Divisional structure**

```
project_directory/
    |--__init__.py
    |--admin/
    |	|--__init__.py
    |   |--views.py
    |   |--static/
    |   |--templates/
    |--home/
    |	|--__init__.py
    |	|--views.py
    |	|--static/
    |	|--templates/
    |--control_panel/
    |	|--__init__.py
    |	|--views.py
    |	|--static/
    |	|--templates/
    |--models.py
```