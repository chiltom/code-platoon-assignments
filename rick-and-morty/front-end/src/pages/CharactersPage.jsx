import { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import CharacterForm from "../components/CharacterForm";
import CharacterCard from "../components/CharacterCard";
import PageButtons from "../components/PageButtons";

const CharactersPage = () => {
  const [characters, setCharacters] = useState({});
  const [nextPage, setNextPage] = useState("");
  const [prevPage, setPrevPage] = useState("");

  useEffect(() => {
    console.log("Characters:");
    console.log(characters);
    if (characters.info) {
      if (characters.info.next) {
        setNextPage(characters.info.next);
      } else {
        setNextPage("");
      }
      if (characters.info.prev) {
        setPrevPage(characters.info.prev);
      } else {
        setPrevPage("");
      }
    }
  }, [characters]);

  useEffect(() => {
    console.log(nextPage, prevPage);
  }, [nextPage, prevPage]);

  return (
    <>
      <Container fluid>
        <Row>
          <CharacterForm setCharacters={setCharacters} />
        </Row>
        <Row>
          {characters.results
            ? characters.results.map((char) => (
                <CharacterCard char={char} key={char.id} />
              ))
            : null}
        </Row>
        <PageButtons
          nextPage={nextPage}
          prevPage={prevPage}
          setCharacters={setCharacters}
        />
      </Container>
    </>
  );
};

export default CharactersPage;
