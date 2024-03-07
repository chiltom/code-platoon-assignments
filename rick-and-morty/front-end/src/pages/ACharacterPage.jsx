import { useState, useEffect } from "react";
import { useParams, useOutletContext } from "react-router-dom";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";

const ACharacterPage = () => {
  const [character, setCharacter] = useState({});
  const { id } = useParams();
  const { addFavorites, removeFavorites, checkIsFavorite } = useOutletContext();
  const isFavorite = checkIsFavorite(character.id);

  useEffect(() => {
    const getCharacter = async () => {
      const { data } = await axios.get(
        `https://rickandmortyapi.com/api/character/${id}`
      );
      setCharacter({
        id: data.id,
        image: data.image,
        name: data.name,
        species: data.species,
        status: data.status,
        origin: data.origin.name,
        location: data.location.name,
        created: data.created,
      });
    };
    getCharacter();
  }, []);

  useEffect(() => {
    console.log(character);
  }, [character]);

  const handleAddToFavorites = () => {
    addFavorites(character);
  };

  const handleRemoveFromFavorites = () => {
    removeFavorites(character);
  };

  const renderButton = () => {
    if (isFavorite) {
      return (
        <Button
          variant="primary"
          size="sm"
          className="bg-blue-500"
          onClick={(e) => {
            e.preventDefault();
            handleRemoveFromFavorites();
          }}
        >
          Remove Favorite
        </Button>
      );
    } else {
      return (
        <Button
          variant="primary"
          size="sm"
          className="bg-blue-500"
          onClick={(e) => {
            e.preventDefault();
            handleAddToFavorites();
          }}
        >
          Add Favorite
        </Button>
      );
    }
  };

  return (
    <>
      <Container>
        <Row>
          <Col>
            <Card key={character.id} style={{ width: "12rem" }}>
              <Card.Img
                variant="top"
                src={character.image}
                alt={`Picture of ${character.name}`}
              />
              <Card.Body>
                <Card.Title>{`${character.name}`}</Card.Title>
                <Card.Text>
                  {`ID: ${character.id}`}
                  <br />
                  {`Species: ${character.species}`}
                  <br />
                  {`Status: ${character.status}`}
                  <br />
                  {`Location: ${character.location}`}
                  <br />
                  {`Origin: ${character.origin}`}
                  <br />
                  {`Created: ${character.created}`}
                  <br />
                </Card.Text>
                {renderButton()}
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default ACharacterPage;
