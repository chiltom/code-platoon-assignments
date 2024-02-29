import { useState } from 'react'
import './App.css'
import tasksData from './data/tasks.json';
// Get tasks data from json

// Show the list of tasks

// An input and form so a user can create and add a new task, which we then
// see in the list

function App() {
  const [showHello, setShowHello] = useState(true);
  const [tasks, setTasks] = useState(tasksData);
  const [input, setInput] = useState("");
  
  // console.log('tasks data', tasksData);

  const toggleDisplayMessage = () => setShowHello(!showHello);

  const handleInput = e => setInput(e.target.value);

  const renderTask = (task) => {
    return `ID: ${task.id}, ${task.task}, COMPLETED: ${task.completed ? "Yes" : "No"}`;
  }

  const addTaskHandler = (e) => {
    e.preventDefault();
    const task = {'id': tasks.length + 1, 'task': input, 'completed': false};
    setTasks([ ...tasks, task])
    setInput("");
  };

  return (
    <>
      <h1>{showHello ? "Hello" : "Goodbye"}</h1>
      <button onClick={toggleDisplayMessage}>Change Display Message</button>
      <h1>Tasks App</h1>
      <ul>
        {tasks.map((task, i) => <li key={i}>{renderTask(task)}</li>)}
      </ul>
      <form onSubmit={addTaskHandler}>
        <input type="text" name="newTask" placeholder="Enter a new task" value={input} onChange={handleInput}/>
        <input type='submit'/>
      </form>
    </>
  )
}

export default App
