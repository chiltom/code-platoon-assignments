import { useEffect, useState } from 'react'
import PuzzleWord from './components/PuzzleWord';
import Form from './components/Form';
import DisplayLetters from './components/DisplayLetters';
import words from './assets/words.json'
import './App.css'

function App() {
  const [puzzle, setPuzzle] = useState(words[Math.floor(Math.random() * words.length)]);
  const [guessedLetters, setGuessedLetters] = useState([]);

  return (
    <>
      <PuzzleWord word={puzzle}/>

    </>
  )
}

export default App
