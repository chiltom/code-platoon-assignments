import { useState, useEffect } from "react";

function Game(arr) {
    const [game, setGame] = useState([]);
    useEffect(() => {
        for (let char of arr) {
            setGame([...game, char]);
        }
    }, [game, arr]);
    return <p>{game}</p>;
}

export default Game;