import { useState, useEffect } from 'react'
import words from './assets/words.jsx'
import './App.css'
import Game from './Game.jsx'

function App() {
  const [puzzle, setPuzzle] = useState([]);
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    setPuzzle((words[Math.floor(Math.random() * words.length)]).split(""));
  }, []);

  const handleInput = e => setInput(e.target.value);

  const handleSubmission = e => {
    e.preventDefault();
    setGuessedLetters([...guessedLetters, input]);
    setInput("");
  };

  return (
    <>
      <h1>Hangman</h1>
      <div id='puzzleCont'>
        <Game arr={puzzle}/>
        <p id='guessedLetters'>{guessedLetters}</p>
      </div>
      <div id='inputCont'>
        <form onSubmit={handleSubmission}>
          <input type='text' name='guess' value={input} onChange={handleInput}/>
          <input type='submit'/>
        </form>
      </div>

    </>
  )
}

export default App
