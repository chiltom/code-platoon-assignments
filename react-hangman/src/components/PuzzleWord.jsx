function PuzzleWord({ word, guessedLetters }) {
    const arr = word.split("").map(letter => {
        const isGuessed = guessedLetters[letter] || false;
        return { val: letter, isGuessed}
    });

    const SPACE = "_";
    const renderLetter = letter => letter.isGuessed ? letter.val : SPACE;

    return (
        <>
            <div>
                {arr.map((letter, i) => (
                    <span key={i}>{renderLetter(letter)}</span>
                ))}
            </div>
        </>
    );
}

export default PuzzleWord;