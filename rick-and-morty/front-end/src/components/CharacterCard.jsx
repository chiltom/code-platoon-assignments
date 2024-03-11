import { useOutletContext, useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Card from "react-bootstrap/Card";
import PropTypes from "prop-types";

const CharacterCard = ({ char, key }) => {
  const { favorites, addFavorites, removeFavorites, checkIsFavorite } =
    useOutletContext();
  const navigate = useNavigate();

  const isFavorite = checkIsFavorite(char.id);

  const handleAddToFavorites = () => {
    if (favorites.length < 4) {
      addFavorites(char);
    } else {
      alert("Too many favorites, you can only have four!");
    }
  };

  const handleRemoveFromFavorites = () => {
    removeFavorites(char);
  };

  const goToCharacter = () => {
    navigate(`/character/${char.id}`);
  };

  const renderButton = () => {
    if (isFavorite) {
      return (
        <Button
          variant="primary"
          size="sm"
          className="bg-blue-500 unfavorite"
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
          className="bg-blue-500 favorite"
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
      <Card key={key} id={char.id} style={{ width: "12rem" }}>
        <Card.Img
          variant="top"
          src={char.image}
          alt={`Picture of ${char.name}`}
        />
        <Card.Body className="flex flex-col justify-evenly">
          <Card.Title>{`${char.name}`}</Card.Title>
          <Card.Text className="mb-3">
            {`Species: ${char.species}`}
            <br />
            {`Status: ${char.status}`}
          </Card.Text>
          <ButtonGroup>
            <Button
              variant="primary"
              size="sm"
              className="bg-blue-500 see-details"
              onClick={(e) => {
                e.preventDefault();
                goToCharacter();
              }}
            >
              See Details
            </Button>
            {renderButton()}
          </ButtonGroup>
        </Card.Body>
      </Card>
    </>
  );
};

CharacterCard.propTypes = {
  char: PropTypes.object,
  key: PropTypes.number,
};

export default CharacterCard;
