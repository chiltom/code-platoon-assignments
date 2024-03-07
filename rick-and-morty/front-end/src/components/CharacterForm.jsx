import { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import PropTypes from "prop-types";
import axios from "axios";

const CharacterForm = ({ setCharacters }) => {
  const [input, setInput] = useState("");
  const [name, setName] = useState("");
  const [isLoading, setLoading] = useState(false);

  useEffect(() => {
    const getData = async () => {
      try {
        const { data } = await axios.get(
          "https://rickandmortyapi.com/api/character"
        );
        setCharacters(data);
      } catch (error) {
        alert(error);
      }
    };
    if (isLoading) {
      getData().then(() => {
        setLoading(false);
      });
    }
  }, [isLoading]);

  useEffect(() => {
    const getData = async () => {
      try {
        const { data } = await axios.get(
          `https://rickandmortyapi.com/api/character/?name=${name.toLowerCase()}`
        );
        setCharacters(data);
      } catch (error) {
        alert(error);
      }
    };
    if (name.length > 0) {
      getData();
    }
  }, [name]);

  const handleAll = (e) => {
    e.preventDefault();
    setLoading(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setName(input);
    setInput("");
  };

  return (
    <>
      <Form>
        <InputGroup className="flex justify-center">
          <Button
            className="bg-slate-500 mr-5"
            variant="secondary"
            size="sm"
            onClick={handleAll}
          >
            {isLoading ? "Loading..." : "Click for All Characters"}
          </Button>
          <InputGroup.Text className="bg-slate-500 text-white">
            Search Character Name:
          </InputGroup.Text>
          <Form.Control
            type="text"
            size="sm"
            placeholder="Type here:"
            id="inputQuery"
            className="max-w-80"
            value={input}
            onChange={(e) => {
              e.preventDefault();
              setInput(e.target.value);
            }}
          />
          <Form.Control
            type="submit"
            size="sm"
            id="submitButton"
            onClick={handleSubmit}
            className="max-w-20 bg-slate-500 text-white"
          />
        </InputGroup>
      </Form>
    </>
  );
};

CharacterForm.propTypes = {
  setCharacters: PropTypes.func,
};

export default CharacterForm;
