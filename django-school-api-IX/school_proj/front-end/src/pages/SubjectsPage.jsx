import axios from "axios";
import { useState, useEffect } from "react";
import { Subject } from "../components/Subject";

export const SubjectsPage = () => {
  const [subjects, setSubjects] = useState([]);

  useEffect(() => {
    const getSubjects = async () => {
      let response = await axios.get("http://127.0.0.1:8000/api/v1/subjects/");
      setSubjects(response.data);
    };
    getSubjects();
  }, []);

  return (
    <>
      {subjects.map((subject) => (
        <Subject subject={subject} />
      ))}
    </>
  );
};
