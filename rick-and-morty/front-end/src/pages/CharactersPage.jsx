import { useEffect, useState } from "react";
import { useOutletContext, useNavigate } from "react-router-dom";
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
    */

  const [characters, setCharacters] = useState({});

  useEffect(() => {
    console.log("Characters:");
    console.log(characters);
  }, [characters]);

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm setCharacters={setCharacters} />
        </Row>
        <Row>
          {characters.results
            ? characters.results.map((char) => (
                <CharacterCard char={char} key={char.id} />
              ))
            : null}
        </Row>
      </Container>
    </>
  );
};

export default CharactersPage;
