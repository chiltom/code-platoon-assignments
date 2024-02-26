// Guessing game logic
// Create function to make random number and store it
function getNum() {return Math.floor(Math.random() * 100) + 1};
const randNum = getNum();
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

// Counter to keep track of how many guesses the user has made
let guessNum = 0;

// Add event listener to form to grab input and run compare nums function
const input = document.getElementById("userGuess");
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
    // TODO: Make elements to hold guess data
    console.log(formattedData)
    

});