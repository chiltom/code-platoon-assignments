function DisplayLetters({ guessedLetters }) {
    const letters = Object.keys(guessedLetters);

    const badLetters = letters.filter(l => !guessedLetters[l]);
    const numBadGuesses = badLetters.length;
    const NUM_ALLOWED_GUESSES = 6;

    return (
        <>
            <h2>Bad Guesses</h2>
            <div>
                {badLetters.map((letter, i) => (
                    <span key={i}>{letter}</span>
                ))}
            </div>
            <h3>{NUM_ALLOWED_GUESSES - numBadGuesses} Guesses Left</h3>
        </>
    )
}

export default DisplayLetters;