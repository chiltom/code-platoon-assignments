// Guessing game logic
// Create function to make random number and store it
function getNum() {return Math.floor(Math.random() * 100) + 1};
const randNum = getNum();
console.log(randNum);

// Grab elements for input data and guess history from document
const input = document.getElementById("userGuess");
const output = document.getElementById("guessHistory");

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

// Counter to keep track of how many guesses the user has made
let guessNum = 0;

// Add event listener to form to grab input and run compare nums function
console.log(input);
input.addEventListener("submit", (e) => {
    // Prevent default action from happening with submission (refresh)
    e.preventDefault();

    // Increment guess counter
    guessNum += 1;

    // Grab data from form with FormData and create an object from it
    const data = new FormData(e.target);
    const formattedData = Object.fromEntries(data);

    // Add ID to formattedData
    formattedData['id'] = guessNum;

    // Create element to hold guess data and append it to output list
    const li = document.createElement('li');
    li.id = formattedData.id;
    li.textContent = compareNums(Number(formattedData.guess));
    output.appendChild(li);
    
    // Check if input matches randNum and, if so, remove it
    if (li.textContent === compareNums(randNum)) {
        const container = document.getElementById("gameContainer");
        container.removeChild(input);
    }
});