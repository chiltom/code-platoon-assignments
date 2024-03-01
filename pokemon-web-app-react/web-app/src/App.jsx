import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'

function App() {
  // State hooks and handlers for hooks
  const [pokeName, setPokeName] = useState("");
  const [pokeData, setPokeData] = useState(null);

  const handlePokeNameChange = e => setPokeName(e.target.value);

  // Helper Functions
  // Change a word to title case
  const toTitleCase = (str) => {
    const arr = str.split("");
    arr[0] = arr[0].toUpperCase();
    return arr.join("");
  }
  // Create a string of pokemon types based on their returned list of types
  const typeString = (types) => {
    let output = "Types: ";
    for (let type of types) {
      console.log(type);
      output += `${toTitleCase(type.type.name)} `;
    }
    return output
  }

  useEffect(() => {
    const getPokemonData = async () => {
      try {
        const response = await axios.get(`http://pokeapi.co/api/v2/pokemon/${pokeName}`);
        setPokeData(response.data);
      } catch(error) {
        console.error(error.response.data);
      }
    }
    if (pokeName.length > 0) {
      getPokemonData();
    }
  }, [pokeName]);

  // Handle form submission for pokemon search, make asynchronous to handle response time from api request
  const handleSubmit = (e) => {
    e.preventDefault();
    setPokeName("");
    // Grab output container to hold pokemon "cards"
    const outputCont = document.getElementById('outputCont');
    // Create pokemon "card" to hold data
    const card = document.createElement('div');
    card.className = 'card';
    outputCont.appendChild(card);
    // Create header for card name and append to card
    const cardName = document.createElement('h3');
    cardName.className = 'cardName'
    cardName.textContent = toTitleCase(pokeData.name);
    card.appendChild(cardName);
    // Add pokemon types to card
    const cardTypes = document.createElement('p');
    cardTypes.className = 'cardTypes';
    console.log(pokeData.types);
    cardTypes.textContent = typeString(pokeData.types);
    card.appendChild(cardTypes);
    // Add pokemon picture to card
    const cardImg = document.createElement('img');
    cardImg.className = 'cardImg'
    cardImg.src = pokeData.sprites.front_default;
    card.appendChild(cardImg);
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
        </div>
      </div>
    </>
  )
}

export default App
