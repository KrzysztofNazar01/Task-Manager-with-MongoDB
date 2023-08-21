from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "3f8ce93c602b1778bd658db2bdaa8a72d5cb6cc4"

# MongoDB database URI with SSL options
app.config["MONGO_URI"] = "mongodb+srv://krzysztofnazar01:XyHndrTPRGZlAWiv@clusterfirst.syclphw.mongodb.net/db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

mongodb_client = PyMongo(app)

db = mongodb_client.db

from application import routes
