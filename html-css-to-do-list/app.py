from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask server application
app = Flask(__name__)

# Create link from app to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tom@localhost/todo'

# Create db instance from link with SQLAlchemy
db = SQLAlchemy(app)

# Create to-do subclass to model table
class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(50))
    completion_status = db.Column(db.Boolean)