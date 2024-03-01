# Requirements:

## Part One:
- A component that displays the puzzle word (letters should be separated by spaces):
    - Use state (<wordDisplay/>)
    - Array where each letter in the word is an element, length dependent on word.length
    - Letters that haven't been guessed should be displayed as an underscore
    - Letters that have been guessed should be displayed

## Part Two:
- A component that contains a text input and a button to submit the guessed letter. If the letter submitted has already been guessed, display an `alert()`
    - <letterForm/>
    - if guess is submitted, alert()
    - some state somewhere for guessed letter

## Part Three:
- A component that displays letters that are not part of the puzzle word.
    - <badGuessDisplay/>
    - arr of wrong guesses

## State and where it lives:
- <App/>
    - puzzle
    - guessedLetters

## Stretch:
- Lost if numBadGuesses === 6

### Solution Steps:
- mkdir data
- code words.json, copy in arr of possible words
- import words from './data/words.json'
- make puzzle word state, use arrow function in useState to grab a random word by index and leave it there, never reset (won't ever use the setPuzzleWord method)
- mkdir components
- code WordDisplay.jsx
- render WordDisplay underneath puzzle word
- pass puzzle word into WordDisplay as a prop (destructure object is standard practice) and ensure it renders from WordDisplay
    - look into props validation
- create puzzleWordArr out of str pass in through props
    - map the split str and make an object out of each letter, val: letter, isGuessed: false
- helper function renderLetter, takes letter object as arg
    - const SPACE = " ";
    - const renderLetter = (letter) => letter.isGuessed => letter.isGuessed ? letter.val : SPACE;
- map puzzleWordArr to return element passed up by WordDisplay
    - ensure key is there for each
    - map all letters as spans inside of a div
- go back to App.jsx and make state of guessedLetters as an empty obj initially, keys will be letter guessed and value will be true
- for dev purposes, you can start with hardcoded word and passed in fake data of guessed letters to work with
- pass guessed letters as a prop to WordDisplay
    - after initial map to puzzleWordArr, map again (chain methods) and if guessedLetters[letter.val], return {...letter, isGuessed: true};
    - else, return letter;