import { useState } from "react";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import CharacterForm from "../components/CharacterForm";

const CharactersPage = () => {
  const [data, setData] = useState("");

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm />
        </Row>
      </Container>
    </>
  );
};

export default CharactersPage;
