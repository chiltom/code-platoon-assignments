import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Outlet } from 'react-router-dom'
import { NavBar } from './components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>School</h1>
      <NavBar />
      <Outlet />
    </>
  )
}

export default App
