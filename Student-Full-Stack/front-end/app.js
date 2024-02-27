/**
 * Helper functions
 */
const removeListElements = () => {
    const lists = document.querySelectorAll('ul');
    for (let list of lists) {
        while (list.firstChild) {
            list.removeChild(list.lastChild);
        }
    }
}

/**
 * First container of 3 cards: Get all students, get student names, get student ages
 */
const containerOne = document.createElement('div');
containerOne.id = 'containerOne';
const transbox = document.getElementById('transbox')
transbox.appendChild(containerOne);

// GET ALL STUDENTS
// Container to hold button and list of all students
const getAllStudsCont = document.createElement('div');
getAllStudsCont.id = 'getAllStudsCont';
containerOne.appendChild(getAllStudsCont);

// Create button and append to container
const getAllStudsBtn = document.createElement('button');
getAllStudsBtn.id = 'getStudBtn';
getAllStudsBtn.textContent = 'Get Students';
getAllStudsBtn.addEventListener("click", (e) => {
    e.preventDefault();
    removeListElements();
    getAllStudents();
})
getAllStudsCont.appendChild(getAllStudsBtn);

// Create list to hold student entries
const studentList = document.createElement('ul');
studentList.id = 'studentList'
getAllStudsCont.appendChild(studentList);

// Function to fetch all students and map data to list components to student list
const getAllStudents = async() => {
    let response = await fetch('http://127.0.0.1:8000/students/');
    let students = await response.json();

    students.map((stud) => {
        const li = document.createElement('li');
        li.id = stud.id;
        li.textContent = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Grade: ${stud.grade}`;
        studentList.appendChild(li);
    })
}

// GET STUDENT NAMES
// Second container to append inside of container one
const getStudentNamesCont = document.createElement('div');
getStudentNamesCont.id = 'getStudentNamesCont';
containerOne.appendChild(getStudentNamesCont);

const getStudNamesBtn = document.createElement('button');
getStudNamesBtn.id = 'getStudNamesBtn';
getStudNamesBtn.textContent = 'Get Student Names';
getStudNamesBtn.addEventListener('click', (e) => {
    e.preventDefault();
    removeListElements();
    getStudentNames();
})
getStudentNamesCont.appendChild(getStudNamesBtn);

const studNameList = document.createElement('ul');
studNameList.id = 'studNameList';
getStudentNamesCont.appendChild(studNameList);

const getStudentNames = async() => {
    let response = await fetch('http://127.0.0.1:8000/student_names/');
    let students = await response.json();

    students.map((stud) => {
        const li = document.createElement('li');
        li.textContent = `Name: ${stud.first_name} ${stud.last_name}`;
        studNameList.appendChild(li);
    })
}

// GET STUDENT AGES
// Third container for container one
const studAgeCont = document.createElement('div');
studAgeCont.id = 'studAgeCont';
containerOne.appendChild(studAgeCont);

// Button for student ages
const studAgeBtn = document.createElement('button');
studAgeBtn.id = 'studAgeBtn';
studAgeBtn.textContent = 'Get Student Ages';
studAgeBtn.addEventListener('click', (e) => {
    e.preventDefault();
    removeListElements();
    getStudentAges();
})
studAgeCont.appendChild(studAgeBtn);

const studAgeList = document.createElement('ul');
studAgeList.id = 'studAgeList';
studAgeCont.appendChild(studAgeList);

const getStudentAges = async() => {
    let response = await fetch('http://127.0.0.1:8000/student_ages/');
    let students = await response.json();

    students.map((stud) => {
        const li = document.createElement('li');
        li.textContent = `Name: ${stud.name} | Age: ${stud.age}`;
        studAgeList.appendChild(li);
    })
}

/**
 * Second container of three cards: get old students, get young students, get advance students
 */
const containerTwo = document.createElement('div');
containerTwo.id = 'containerTwo';
transbox.appendChild(containerTwo);

// GET OLD STUDENTS
// Container
const getOldStudsCont = document.createElement('div');
getOldStudsCont.id = 'getOldStudsCont';
containerTwo.appendChild(getOldStudsCont);

// Button
const getOldStudsBtn = document.createElement('button');
getOldStudsBtn.id = 'getOldStudsBtn';
getOldStudsBtn.textContent = "Get Old Students";
getOldStudsBtn.addEventListener('click', (e) => {
    e.preventDefault();
    removeListElements();
    getOldStuds();
})
getOldStudsCont.appendChild(getOldStudsBtn);

// List
const getOldStudsList = document.createElement('ul');
getOldStudsList.id = 'oldStudsList';
getOldStudsCont.appendChild(getOldStudsList);

// Function
const getOldStuds = async() => {
    let response = await fetch('http://127.0.0.1:8000/old_students/');
    let students = await response.json();

    students.map((stud) => {
        const li = document.createElement('li');
        li.id = stud.id;
        li.textContent = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Grade: ${stud.grade}`;
        getOldStudsList.appendChild(li);
    })
}

// GET YOUNG STUDENTS
// Container
const youngStudsCont = document.createElement('div');
youngStudsCont.id = 'youngStudsCont';
containerTwo.appendChild(youngStudsCont);

// Button
const youngStudsBtn = document.createElement('button');
youngStudsBtn.id = 'youngStudsBtn';
youngStudsBtn.textContent = 'Get Young Students';
youngStudsBtn.addEventListener('click', (e) => {
    e.preventDefault();
    removeListElements();
    getYoungStuds();
})
youngStudsCont.appendChild(youngStudsBtn);

// List
const youngStudsList = document.createElement('ul');
youngStudsList.id = 'youngStudsList';
youngStudsCont.appendChild(youngStudsList);

// Function
const getYoungStuds = async() => {
    let response = await fetch('http://127.0.0.1:8000/young_students/');
    let students = await response.json();
    
    students.map((stud) => {
        const li = document.createElement('li');
        li.id = stud.id;
        li.textContent = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Grade: ${stud.grade}`;
        youngStudsList.appendChild(li);
    })
}

// GET ADVANCE STUDENTS
// Container
const advStudCont = document.createElement('div');
advStudCont.id = 'advStudCont';
containerTwo.appendChild(advStudCont);

// Button
const advStudBtn = document.createElement('button');
advStudBtn.id = 'advStudBtn';
advStudBtn.textContent = 'Get Advance Students';
advStudBtn.addEventListener('click', (e) => {
    e.preventDefault();
    removeListElements();
    getAdvanceStudents();
})
advStudCont.appendChild(advStudBtn);

// List
const advStudList = document.createElement('ul');
advStudList.id = 'advStudList';
advStudCont.appendChild(advStudList);

// Function
const getAdvanceStudents = async() => {
    let response = await fetch('http://127.0.0.1:8000/advance_students/');
    let students = await response.json();

    students.map((stud) => {
        const li = document.createElement('li');
        li.id = stud.id;
        li.textContent = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Grade: ${stud.grade}`;
        advStudList.appendChild(li);
    })
}

/**
 * Final container for a button to clear entire page
 */

// Container
const containerThree = document.createElement('div');
containerThree.id = 'containerThree';
transbox.appendChild(containerThree);

// Button
const resetButton = document.createElement('button');
resetButton.id = 'resetButton';
resetButton.textContent = 'Reset';
resetButton.addEventListener('click', (e) => {
    removeListElements();
})
containerThree.appendChild(resetButton);