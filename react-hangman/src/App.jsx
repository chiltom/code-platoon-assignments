import { useState } from 'react'
import PuzzleWord from './components/PuzzleWord';
import Form from './components/Form';
import DisplayLetters from './components/DisplayLetters';
import words from './assets/words.json'
import './App.css'

function App() {
  const [puzzle, setPuzzle] = useState(words[Math.floor(Math.random() * words.length)]);
  const [guessedLetters, setGuessedLetters] = useState({});

  const handleGuess = letter => {
    if (guessedLetters.hasOwnProperty(letter)) {
      alert('Letter already guessed!');
    } else {
      const updated = {...guessedLetters};
      if (puzzle.includes(letter)) {
        updated[letter] = true;
      } else {
        updated[letter] = false;
      }
      setGuessedLetters(updated);
    }
  }

  const NUM_ALLOWED_GUESSES = 6;

  const getBadLetters = () => {
    const letters = Object.keys(guessedLetters);
    return letters.filter(l => !guessedLetters[l]);
  }

  const calculateNumGuessesLeft = () => {
    const numBadGuesses = getBadLetters().length;
    return NUM_ALLOWED_GUESSES - numBadGuesses;
  }

  const renderWinMessage = () => {
    const lettersLeftToGuess = puzzle.split("").filter(l => {
      if (guessedLetters[l] === true) {
        return false;
      }
      return true;
    });

    if (lettersLeftToGuess.length === 0) {
      return <h2>You Won!</h2>
    }

    return null
  }

  const renderLoseMessage = () => {
    if(calculateNumGuessesLeft() === 0) {
      return <h2>You Lost!</h2>
    }

    return null;
  }

  return (
    <>
      <h1>Hangman</h1>
      {renderWinMessage()}
      {renderLoseMessage()}
      <PuzzleWord word={puzzle} guessedLetters={guessedLetters}/>
      <DisplayLetters guessedLetters={guessedLetters} />
      <Form handleGuess={handleGuess} />
    </>
  )
}

export default App
