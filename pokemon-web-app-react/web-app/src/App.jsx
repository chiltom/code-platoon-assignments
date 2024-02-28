import { useState } from 'react';
import axios from 'axios';
import './App.css'

function App() {
  const [pokeName, setPokeName] = useState("");
  const [pokeData, setPokeData] = useState(null);
  const handlePokeNameChange = e => setPokeName(e.target.value);
  // const handlePokeDataChange = e => setPokeData(e.target.value);

  const getPokemon = async (target) => {
    try {
      const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${target}`);
      setPokeData(response.data);
    } catch(error) {
      setPokeData(`${error.response.status}: ${error.response.data}`);
    }
  }

  const handleSubmit = e => {
    e.preventDefault();
    
    getPokemon(pokeName);
    console.log(pokeData);
    
    const outputCont = document.getElementById('outputCont');
    const card = document.createElement('div');
    card.className = 'card';
    outputCont.appendChild(card);

    const cardData = document.createElement('p');
    cardData.className = 'cardData'
    cardData.textContent = pokeData;
    card.appendChild(cardData);
  }

  return (
    <>
      <div id='headerCont'>
        <h1 className='headerText'>PokeAPI Fetcher<img src='https://showme0-9071.kxcdn.com/files/528810/pictures/thumbs/1189951/last_thumb1382570134.jpg' width='100px' height='100px' id='happyPikachu'></img></h1>
        <p className='headerText'><em>A simple Pokemon data fetcher</em></p>
      </div>
      <div id='inputCont'>
        <form id='userInput' onSubmit={handleSubmit}>
          <input type='text' name='pokeName' placeholder="Enter a pokemon's name:" value={pokeName} onChange={handlePokeNameChange}></input>
          <input type='submit'></input>
        </form>
      </div>
      <div id='outputCont'>
        <div className='card'>
          <p>Charizard</p>
        </div>
      </div>
    </>
  )
}

export default App
