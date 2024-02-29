import { useState } from 'react'
import './App.css'

function App() {
  const [on, setOn] = useState(true);

  const toggleImg = (e) => setOn(on => !on);

  return (
    <>
      <img src={on ? './assets/on.svg' : './assets/off.svg'} onClick={toggleImg}/>
    </>
  )
}

export default App
