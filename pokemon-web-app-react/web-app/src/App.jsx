import './App.css'

function App() {
  // const [count, setCount] = useState(0)
  const handleSubmit = e => {
    e.preventDefault();
    console.log(e.target.parentElement);
  }

  return (
    <>
      <div id='headerCont'>
        <h1 className='headerText'>PokeAPI Fetcher<img src='https://showme0-9071.kxcdn.com/files/528810/pictures/thumbs/1189951/last_thumb1382570134.jpg' width='100px' height='100px' id='happyPikachu'></img></h1>
        <p className='headerText'><em>A simple Pokemon data fetcher</em></p>
      </div>
      <div id='inputCont'>
        <form id='userInput' onSubmit={handleSubmit}>
          <input type='text' id='textInput' placeholder="Enter a pokemon's name:"></input>
          <input type='submit'></input>
        </form>
      </div>
    </>
  )
}

export default App
