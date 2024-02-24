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
    # students = db.relationship('students', backref='subject', lazy=True)
    # teachers = db.relationship('teachers', backref='subjects', lazy=True)

# Establish relationships between subject in students and teachers with subject.id
class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    # subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.Column(db.Integer)

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    # subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.Column(db.Integer)

# RESTful API Endpoints

# Return a list of students along with their class names and the teeacher of their class, in JSON format
# TODO: Fix reference for teacher of subject
@app.route('/students/', methods=['GET'])
def get_students() -> list:
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    student_list = []
    for student in students:
        class_dict = {}
        for subject in subjects:
            if student.subject == subject.id:
                class_dict["subject"] = subject.subject
        for teacher in teachers:
            if teacher.subject == student.subject:
                class_dict['teacher'] = f"{teacher.first_name} {teacher.last_name}"
        student_list.append({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'class': class_dict})
    return jsonify(student_list)

# Return a list of teachers, the subjects they teach, and the students within each subject
@app.route('/teachers/', methods=['GET'])
def get_teachers() -> list:
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    teacher_list = []
    for teacher in teachers:
        subject_dict = {}
        student_list = []
        for subject in subjects:
            if teacher.subject == subject.id:
                subject_dict['subject'] = subject.subject
        for student in students:
            if teacher.subject == student.subject:
                student_list.append(f"{student.first_name} {student.last_name}")
        subject_dict['students'] = student_list
        teacher_list.append({'first_name': teacher.first_name, 'last_name': teacher.last_name, 'age': teacher.age, 'subject': subject_dict})
    return jsonify(teacher_list)

# Returns a list of dictionaries with the students enrolled in each class and the teacher who teaches each subject
@app.route('/subjects/', methods=['GET'])
def get_subjects() -> list:
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    subject_list = []
    for subject in subjects:
        subject_dict = {'id': subject.id, 'subject': subject.subject}
        student_list = []
        for teacher in teachers:
            if subject.id == teacher.subject:
                subject_dict['teacher'] = f"{teacher.first_name} {teacher.last_name}"
        for student in students:
            if subject.id == student.subject:
                student_list.append(f"{student.first_name} {student.last_name}")
        subject_dict['students'] = student_list
        subject_list.append(subject_dict)
    return jsonify(subject_list)

if __name__ == "__main__":
    app.run(port=8000, debug=True)