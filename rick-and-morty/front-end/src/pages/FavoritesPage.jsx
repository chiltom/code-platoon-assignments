import { useOutletContext } from "react-router-dom";
import CharacterCard from "../components/CharacterCard";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const FavoritesPage = () => {
  const { favorites } = useOutletContext();

  return (
    <>
      <Container>
        <h1 className="text-center text-3xl font-bold">Favorites</h1>
        <h2 className="text-center mb-6 italic">You can only have 4!</h2>
        <Row className="flex flex-row items-center" id="favorites-container">
          {favorites.map((char) => (
            <Col key={char.id}>
              <CharacterCard char={char} key={char.id} />
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
};

export default FavoritesPage;
