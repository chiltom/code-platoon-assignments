// Create function to make random number and store it
function getNum() {return Math.floor(Math.random() * 100) + 1};
let randNum = getNum();
console.log(randNum);

// Function to compare guess to random number
const compareNums = (num) => {
    if (num === randNum) {
        return `${num} was correct! You win!`;
    } else if (num < randNum) {
        return `${num} was too low. Try again.`;
    } else {
        return `${num} was too high. Try again.`;
    }
}

// Create game container
const gameContainer = document.createElement('div');
gameContainer.id = 'gameContainer';
document.body.appendChild(gameContainer);

// Create form for game container
const form = document.createElement('form');
form.id = 'userGuess';
gameContainer.appendChild(form);

// Create inputs for form
const numField = document.createElement('input');
numField.name = 'guess';
numField.type = 'number';
numField.placeholder = 'Enter a guess: ';

const submitButton = document.createElement('input');
submitButton.type = 'submit';

form.appendChild(numField);
form.appendChild(submitButton);

// Create guess history list as log
const guessLog = document.createElement('ul');
guessLog.id = 'guessHistory';
gameContainer.appendChild(guessLog);

// Create reset button for use after game win
const reset = document.createElement('button');
reset.id = 'resetButton';
reset.textContent = 'Reset';
reset.addEventListener('click', (e) => {
    // Prevent any default behavior
    e.preventDefault();
    // Remove children from guess log
    while (guessLog.firstChild) {
        guessLog.removeChild(guessLog.lastChild);
    }
    // Reset randNum
    randNum = getNum();
    console.log(randNum);
    // Replace form on screen
    gameContainer.appendChild(form);
    // Remove this button
    gameContainer.removeChild(reset);
})

// Counter to keep track of how many guesses the user has made
let guessNum = 0;

// Add event listener to form to grab input and run compare nums function
form.addEventListener("submit", (e) => {
    // Prevent default action from happening with submission (refresh)
    e.preventDefault();
    // Increment guess counter
    guessNum += 1;
    // Grab data from form with FormData and create an object from it
    const data = new FormData(e.target);
    const formattedData = Object.fromEntries(data);
    // Clear num field
    numField.value = null;
    // Add ID to formattedData
    formattedData['id'] = guessNum;
    // Create element to hold guess data and append it to output list
    const li = document.createElement('li');
    li.id = formattedData.id;
    li.textContent = compareNums(Number(formattedData.guess));
    guessLog.appendChild(li); 
    // Check if input matches randNum and, if so, remove it
    if (li.textContent === compareNums(randNum)) {
        gameContainer.removeChild(form);
        gameContainer.appendChild(reset);
    }
});