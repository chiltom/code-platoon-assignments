from flask import Flask, jsonify
from students import students

# Initialization of Flask server application
app = Flask(__name__)

# RESTful API Endpoints

# Returns old students (21 and over)
@app.route('/old_students/', methods=['GET'])
def get_old_students() -> list:
    lst = []
    for student in students:
        if student['age'] > 20:
            lst.append(student)
    return lst

# Returns young students (20 and under)
@app.route('/young_students/', methods=['GET'])
def get_young_students() -> list:
    lst = []
    for student in students:
        if student['age'] < 21:
            lst.append(student)
    return lst

# Returns advance students (20 and under AND letter grade of A)
@app.route('/advance_students/', methods=['GET'])
def get_advance_students() -> list:
    lst = []
    for student in students:
        if student['age'] < 21 and student['grade'] == 'A':
            lst.append(student)
    return lst

# Returns only key: value pairs of student first_name and last_name
@app.route('/student_names/', methods=['GET'])
def get_student_names() -> list:
    lst = []
    for student in students:
        lst.append({'first_name': student['first_name'], 'last_name': student['last_name']})
    return lst

# Returns students key: value pairs of student first_name and last_name combined as student_name
# and age as another key: value pair
@app.route('/student_ages/', methods=['GET'])
def get_student_ages() -> list:
    lst = []
    for student in students:
        lst.append({'student_name': student['first_name'] + " " + student['last_name'], 'age': student['age']})
    return lst

# Returns all students available
@app.route('/students/', methods=['GET'])
def get_students() -> list:
    return students

if __name__ == "__main__":
    app.run(debug=True)