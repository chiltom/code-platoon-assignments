from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialization of Flask server application
app = Flask(__name__)

# Set up CORS on Flask application for cross origin requests
CORS(app)

# Link the app with the database that contains relevant data through SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tom@localhost/students' # Make sure this is correct

# Create db instance from link with SQLAlchemy
db = SQLAlchemy(app)

# Create student subclass from db.Model module: all table headers and value types
class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

# RESTful API Endpoints

# Returns old students (21 and over)
@app.route('/old_students/', methods=['GET'])
def get_old_students() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        if student.age > 20:
            student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade})
    return jsonify(student_list)
        

# Returns young students (20 and under)
@app.route('/young_students/', methods=['GET'])
def get_young_students() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        if student.age < 21:
            student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade})
    return jsonify(student_list)

# Returns advance students (20 and under AND letter grade of A)
@app.route('/advance_students/', methods=['GET'])
def get_advance_students() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        if student.age < 21 and student.grade == 'A':
            student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade})
    return jsonify(student_list)

# Returns only key: value pairs of student first_name and last_name
@app.route('/student_names/', methods=['GET'])
def get_student_names() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append({'first_name': student.first_name, 'last_name': student.last_name})
    return jsonify(student_list)

# Returns students key: value pairs of student first_name and last_name combined as student_name
# and age as another key: value pair
@app.route('/student_ages/', methods=['GET'])
def get_student_ages() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append({'name': student.first_name + " " + student.last_name, 'age': student.age})
    return jsonify(student_list)

# Returns all students available
@app.route('/students/', methods=['GET'])
def get_students() -> list:
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade})
    return jsonify(student_list)

# Run file script
if __name__ == "__main__":
    app.run(port=8000, debug=True)
    
# Browser sorts return JSON keys automatically, the auto-sorting is not happening here