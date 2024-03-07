import { useOutletContext, useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Card from "react-bootstrap/Card";
import PropTypes from "prop-types";

const CharacterCard = ({ char, key }) => {
  /* 
    TODO: Make a "See Details" button that changes the URL (useNavigate hook)
    to a more details card (ACharacterPage) that shows more details about the
    character (use useParams hook in ACharacterPage by passing ID down through
    navigate hook)
    - Maybe make take the creation date and origin and species from here and
      throw it in there
      */

  const { addFavorites, removeFavorites, checkIsFavorite } = useOutletContext();
  const navigate = useNavigate();

  const isFavorite = checkIsFavorite(char.id);

  const handleAddToFavorites = () => {
    addFavorites(char);
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
          <ButtonGroup>
            <Button
              variant="primary"
              size="sm"
              className="bg-blue-500"
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
  addFavorites: PropTypes.func,
  removeFavorites: PropTypes.func,
  key: PropTypes.number,
};

export default CharacterCard;
