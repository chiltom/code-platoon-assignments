from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialization of Flask server application
app = Flask(__name__)

# Link the app with the relevant db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tom@localhost/school'

# Create db instance from link with SQLAlchemy
db = SQLAlchemy(app)

# Create subclasses from db.Model module: all table headers and value types
class Subjects(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(50))
    students = db.relationship('students', backref='subject', lazy=True)
    teachers = db.relationship('teachers', backref='subjects', lazy=True)

# Establish relationships between subject in students and teachers with subject.id
class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

# RESTful API Endpoints

# Return a list of students along with their class names and the teeacher of their class, in JSON format
# TODO: Fix reference for teacher of subject
@app.route('/students/', methods=['GET'])
def get_students() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'class': {}})
    return jsonify(student_list)

if __name__ == "__main__":
    app.run(port=8000, debug=True)