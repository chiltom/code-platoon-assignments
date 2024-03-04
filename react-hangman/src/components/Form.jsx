import { useState } from "react";

function Form({ handleGuess }) {
    const [input, setInput] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault()
        handleGuess(input);
        setInput("");
    }

    return (
        <>
            <h2>Guess a Letter!</h2>
            <input 
                value={input}
                onChange={e => setInput(e.target.value)}
                placeholder="Enter a letter here"
            />
            <input type="submit" onClick={handleSubmit}/>
        </>
    )
}

export default Form;