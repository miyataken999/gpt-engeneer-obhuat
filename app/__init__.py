from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from google.cloud import vision
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@localhost/google_lens_db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

vision_client = vision.ImageAnnotatorClient()
firebase_credentials = credentials.Certificate("firebase_credentials.json")
firebase_app = firebase_admin.initialize_app(firebase_credentials)
firebase_db = firestore.client()