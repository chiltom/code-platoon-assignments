import { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import CharacterForm from "../components/CharacterForm";

const CharactersPage = () => {
  const [characters, setCharacters] = useState({});

  useEffect(() => {
    console.log(characters);
  }, [characters]);

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm setCharacters={setCharacters} />
        </Row>
      </Container>
    </>
  );
};

export default CharactersPage;
