import { useState, useEffect } from "react";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

const CharacterForm = () => {
  const [input, setInput] = useState("");

  useEffect(() => {
    console.log(input);
  }, [input]);

  return (
    <>
      <Form className="flex flex-row">
        <ButtonGroup>
          <Button size="sm" className="bg-slate-500" variant="secondary">
            All Characters
          </Button>
          <Button size="sm" className="bg-slate-500" variant="secondary">
            All Locations
          </Button>
          <Button size="sm" className="bg-slate-500" variant="secondary">
            All Episodes
          </Button>
        </ButtonGroup>
        <InputGroup className="flex justify-end">
          <InputGroup.Text>Search Character Name:</InputGroup.Text>
          <Form.Control
            type="text"
            placeholder="Type here:"
            id="inputQuery"
            className="max-w-80"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <Form.Control type="submit" id="submitButton" className="max-w-20" />
        </InputGroup>
      </Form>
    </>
  );
};

export default CharacterForm;
