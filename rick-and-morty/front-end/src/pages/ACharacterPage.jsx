import { useState, useEffect } from "react";
import { useParams, useOutletContext, useNavigate } from "react-router-dom";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";

const ACharacterPage = () => {
  const [character, setCharacter] = useState({});
  const { id } = useParams();
  const { favorites, addFavorites, removeFavorites, checkIsFavorite } =
    useOutletContext();
  const navigate = useNavigate();
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

  const handleAddToFavorites = () => {
    if (favorites.length < 4) {
      addFavorites(character);
    } else {
      alert("Too many favorites, you can only have four!");
    }
  };

  const handleRemoveFromFavorites = () => {
    removeFavorites(character);
  };

  const goToChars = () => {
    navigate("/characters");
  };

  const renderButton = () => {
    if (isFavorite) {
      return (
        <Button
          variant="primary"
          size="sm"
          className="bg-blue-500 mt-3"
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
          className="bg-blue-500 mt-3"
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
          <Col className="flex justify-center mt-24">
            <Card key={character.id} style={{ width: "12rem" }}>
              <Card.Img
                variant="top"
                src={character.image}
                alt={`Picture of ${character.name}`}
              />
              <Card.Body className="flex flex-col justify-evenly">
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
        <div className="flex flex-row justify-center mt-6">
          <Button
            size="sm"
            variant="secondary"
            className="bg-slate-500"
            onClick={() => goToChars()}
          >
            Return to Characters
          </Button>
        </div>
      </Container>
    </>
  );
};

export default ACharacterPage;
