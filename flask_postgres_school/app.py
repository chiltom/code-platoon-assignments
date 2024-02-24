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
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    # students = db.relationship('students', backref='subject', lazy=True)
    # teachers = db.relationship('teachers', backref='subjects', lazy=True)

# Establish relationships between subject in students and teachers with subject.id
class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    # subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.Column(db.Integer)

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    # subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.Column(db.Integer)


# RESTful API Endpoints

# Return a list of students along with their class names and the teacher of their class, in JSON format
@app.route('/students/', methods=['GET'])
def get_students() -> list:
    # REQUEST all data from all tables for comparison and pushing
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    # Initialize list to hold student dictionaries
    student_list = []
    # Iterate over each student
    for student in students:
        # Create class dictionary to hold class info
        class_dict = {}
        # Iterate over subjects and find which subject student is enrolled in, update class dict with name once found
        for subject in subjects:
            if student.subject == subject.id:
                class_dict["subject"] = subject.subject
        # Iterate over teachers and find which teacher is the student's update class dict with teacher's name
        for teacher in teachers:
            if teacher.subject == student.subject:
                class_dict['teacher'] = f"{teacher.first_name} {teacher.last_name}"
        # Append student dictionary with class info to student_list
        student_list.append({'id': student.id, 'first_name': student.first_name,
                            'last_name': student.last_name, 'age': student.age, 'class': class_dict})
    # Return student list in JSON format
    return jsonify(student_list)

# Return a list of teachers, the subjects they teach, and the students within each subject
@app.route('/teachers/', methods=['GET'])
def get_teachers() -> list:
    # REQUEST all data from all tables for comparison and pushing
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    # Initialize list to hold teacher dictionaries
    teacher_list = []
    # Iterate over each teacher
    for teacher in teachers:
        # Create subject dictionary to hold subject name and student list
        subject_dict = {}
        # Iterate over subjects and find teacher's subject, update subject dictionary with name once found
        for subject in subjects:
            if teacher.subject == subject.id:
                subject_dict['subject'] = subject.subject
        # Create student list to hold each student in the subject
        student_list = []
        # Iterate over students and append each student enrolled in the teacher's subject to the list
        for student in students:
            if teacher.subject == student.subject:
                student_list.append(
                    f"{student.first_name} {student.last_name}")
        # Update subject dictionary with list of students
        subject_dict['students'] = student_list
        # Append teacher dictionary with class info and students to teacher_list
        teacher_list.append({'first_name': teacher.first_name,
                            'last_name': teacher.last_name, 'age': teacher.age, 'subject': subject_dict})
    # Return teacher_list in JSON format
    return jsonify(teacher_list)

# Returns a list of dictionaries with the students enrolled in each class and the teacher who teaches each subject
@app.route('/subjects/', methods=['GET'])
def get_subjects() -> list:
    # REQUEST all data from all tables for comparison and pushing
    students = Students.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    # Initialize list to hold subject dictionaries
    subject_list = []
    # Iterate over each subject
    for subject in subjects:
        # Create subject dictionary that holds all info, starting with id and subject name
        subject_dict = {'id': subject.id, 'name': subject.subject}
        # Iterate over teachers and find subject teacher, update dictionary with their name
        for teacher in teachers:
            if subject.id == teacher.subject:
                subject_dict['teacher'] = f"{teacher.first_name} {teacher.last_name}"
        # Create student list to append all students enrolled in that subject
        student_list = []
        # Iterate over students and append their names to the list
        for student in students:
            if subject.id == student.subject:
                student_list.append(
                    f"{student.first_name} {student.last_name}")
        # Update subject dictionary with student names list
        subject_dict['students'] = student_list
        # Append subject dictionary to total subject_list
        subject_list.append(subject_dict)
    # Return subject_list in JSON format
    return jsonify(subject_list)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
