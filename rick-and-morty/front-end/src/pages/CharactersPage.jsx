import { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CharacterForm from "../components/CharacterForm";
import CharacterCard from "../components/CharacterCard";

const CharactersPage = () => {
  /*
    TODO: Make buttons on the bottom of the page for next page (if exists)
    and previous page (if exists)
        - TODO: Make functionality for grabbing next API calls from the url
        supplied in the object returned from search response
    TODO: Pass favorites the char.id instead of char.name so that another
    API call can be made with the char IDs and a favorites page can be made
    */

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
    console.log("Characters:");
    console.log(characters);
  }, [characters]);

  useEffect(() => {
    console.log(`Favorites: ${favorites}`);
  }, [favorites]);

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm setCharacters={setCharacters} />
        </Row>
        <Row>
          {characters.results
            ? characters.results.map((char) => (
                <CharacterCard
                  char={char}
                  addFavorites={addFavorites}
                  removeFavorites={removeFavorites}
                  key={char.id}
                />
              ))
            : null}
        </Row>
      </Container>
    </>
  );
};

export default CharactersPage;
