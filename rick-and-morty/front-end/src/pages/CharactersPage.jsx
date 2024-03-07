import { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CharacterForm from "../components/CharacterForm";
import CharacterCard from "../components/CharacterCard";

const CharactersPage = () => {
  const [characters, setCharacters] = useState({});
  const [favorites, setFavorites] = useState([]);

  const addFavorites = (newName) => {
    setFavorites([...favorites, newName]);
  };

  const removeFavorites = (name) => {
    setFavorites(
      favorites.filter((char) => {
        return char !== name;
      })
    );
  };

  useEffect(() => {
    console.log(characters);
  }, [characters]);

  useEffect(() => {
    console.log(favorites);
  }, [favorites]);

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm setCharacters={setCharacters} />
        </Row>
        <Row>
          {characters.results
            ? characters.results.map((char, i) => (
                <CharacterCard
                  char={char}
                  addFavorites={addFavorites}
                  removeFavorites={removeFavorites}
                  key={i}
                />
              ))
            : null}
        </Row>
      </Container>
    </>
  );
};

export default CharactersPage;
