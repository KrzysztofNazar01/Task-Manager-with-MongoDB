# Task Manager with MongoDB
## The goal of the project

The goal of the project was to implement Flask web application which is a tool to manage task and save them in a database.
The manager allows performing CRUD operations on tasks, and displays them in user-friendly way.
This project is based on this [YouTube tutorial](https://www.youtube.com/playlist?list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT).

[//]: # (## Live demo)

[//]: # (Use [**this link**]&#40;https://taskmanagerbykn.pythonanywhere.com/&#41; to check the demo of this application hosted by [Pythonanywhere.com]&#40;https://pythonanywhere.com&#41;.)


## Project Setup

1. Create virtual environment

```bash
#Linux and Mac
python -m venv venv

#Windows
python -m venv c:\path\to\myenv
```

2. Activate the virtual environment

```bash
#Linux and Mac
source venv/bin/activate

#Windows
\venv\Scripts\activate.bat
```

3. Install project dependencies

```bash
pip install flask Flask-PyMongo Flask-WTF

python -m pip install "pymongo[srv]
```

4. Set up the mongoDB cluster

Firstly, [sign up for MongoDB cloud](https://account.mongodb.com/account/login).
Then, follow [this tutorial](https://nixfaq.org/2021/10/how-to-connect-python-flask-with-mongodb.html).

# What I learned during this project?

- Setting up database connection using [mongoDB cloud](https://account.mongodb.com/account/login)
- Creating Flask forms using [Flask-WTF extension](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html)
- Using AJAX queries to update objects in the database
- Implement user-friendly alerts using [Flash](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
- Creating a calendar using [FullCalendar](https://fullcalendar.io/)
- Setting up __init__.py file with project configurations
