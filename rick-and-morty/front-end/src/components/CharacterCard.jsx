import { useState } from "react";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Card from "react-bootstrap/Card";
import PropTypes from "prop-types";

const CharacterCard = ({
  characters,
  favorites,
  addFavorites,
  removeFavorites,
}) => {
  return (
    <>
      {characters
        ? characters.map((char, i) => (
            <Card key={i} style={{ width: "12rem" }}>
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
                <ButtonGroup>
                  <Button
                    variant="primary"
                    size="sm"
                    className="bg-blue-500"
                    onClick={(e) => {
                      e.preventDefault();
                      addFavorites(char.name);
                    }}
                  >
                    Add Favorite
                  </Button>
                  <Button
                    variant="primary"
                    size="sm"
                    className="bg-blue-500"
                    onClick={(e) => {
                      e.preventDefault();
                      removeFavorites(char.name);
                    }}
                  >
                    Remove Favorite
                  </Button>
                </ButtonGroup>
              </Card.Body>
            </Card>
          ))
        : null}
    </>
  );
};

CharacterCard.propTypes = {
  characters: PropTypes.array,
  favorites: PropTypes.array,
  addFavorites: PropTypes.func,
  removeFavorites: PropTypes.func,
};

export default CharacterCard;
