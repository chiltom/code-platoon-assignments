import { useState } from "react";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Card from "react-bootstrap/Card";
import PropTypes from "prop-types";

const CharacterCard = ({ char, addFavorites, removeFavorites, key }) => {
  /* 
    TODO: Make a "See Details" button that changes the card to a more details
    card (separate component?) that shows more details about the character
    - Maybe make take the creation date and origin and species from here and
      throw it in there
    TODO: Change addFavorites and removeFavorites parameters from char.name
    to char.id to set favorites with IDs for later API calls for favorites
    page
      */

  const [isFavorite, setIsFavorite] = useState(false);

  return (
    <>
      <Card key={key} style={{ width: "12rem" }}>
        <Card.Img
          variant="top"
          src={char.image}
          alt={`Picture of ${char.name}`}
        />
        <Card.Body>
          <Card.Title>{`${char.name}`}</Card.Title>
          <Card.Text>
            {`ID: ${char.id}`}
            <br />
            {`Species: ${char.species}`}
            <br />
            {`Status: ${char.status}`}
            <br />
            {`Origin: ${char.origin.name}`}
            <br />
            {`Created: ${char.created}`}
            <br />
          </Card.Text>
          {isFavorite ? (
            <Button
              variant="primary"
              size="sm"
              className="bg-blue-500"
              onClick={(e) => {
                e.preventDefault();
                removeFavorites(char.name);
                setIsFavorite(false);
              }}
            >
              Remove Favorite
            </Button>
          ) : (
            <Button
              variant="primary"
              size="sm"
              className="bg-blue-500"
              onClick={(e) => {
                e.preventDefault();
                addFavorites(char.name);
                setIsFavorite(true);
              }}
            >
              Add Favorite
            </Button>
          )}
        </Card.Body>
      </Card>
    </>
  );
};

CharacterCard.propTypes = {
  char: PropTypes.object,
  addFavorites: PropTypes.func,
  removeFavorites: PropTypes.func,
  key: PropTypes.number,
};

export default CharacterCard;
