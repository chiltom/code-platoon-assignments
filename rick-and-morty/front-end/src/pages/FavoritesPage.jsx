import { useOutletContext } from "react-router-dom";
import CharacterCard from "../components/CharacterCard";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";

const FavoritesPage = () => {
  const { favorites } = useOutletContext();

  return (
    <>
      <Container>
        <h1 className="text-center text-3xl font-bold mb-6">Favorites</h1>
        <Row className="flex flex-row justify-center">
          {favorites.map((char) => (
            <CharacterCard char={char} key={char.id} />
          ))}
        </Row>
      </Container>
    </>
  );
};

export default FavoritesPage;
