import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import PropTypes from "prop-types";
import axios from "axios";

const CharacterForm = ({ setCharacters }) => {
  const [input, setInput] = useState("");
  const [name, setName] = useState("");
  const navigate = useNavigate();

  const backToAll = () => {
    navigate("/characters");
  };

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
    getData();
  }, []);

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

  const handleSubmit = (e) => {
    if (input) {
      e.preventDefault();
      setName(input);
      setInput("");
    } else {
      e.preventDefault();
      backToAll();
    }
  };

  return (
    <>
      <Form>
        <InputGroup className="flex justify-center">
          <InputGroup.Text className="bg-slate-500 text-white">
            Search Character Name:
          </InputGroup.Text>
          <Form.Control
            type="text"
            size="sm"
            placeholder="Type ' ' to return to all characters:"
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
