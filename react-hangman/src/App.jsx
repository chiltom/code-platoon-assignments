import { useState, useEffect } from 'react'
import words from './assets/words.jsx'
import './App.css'
import Guess from './Guess.jsx'

function App() {
  const [puzzle, setPuzzle] = useState("");
  const [guessedLetters, setGuessedLetters] = useState([]);

  useEffect(() => {
    setPuzzle(words[Math.floor(Math.random() * words.length)]);
  }, []);

  const handleGuess = e => setGuessedLetters([...guessedLetters, e.target.value]);

  const handleSubmission = (e) => {
    return e.target.value
  };

  return (
    <>
      <h1>Hangman</h1>
      <div id='puzzleCont'>
        <p id='puzzleWord'>{puzzle}</p>
        <p id='guessedLetters'></p>
      </div>
      <div id='inputCont'>
        <form onSubmit={handleSubmission}>
          <input type='text' name='guess' value={""} onChange={handleGuess}/>
          <input type='submit'/>
        </form>
      </div>

    </>
  )
}

export default App
