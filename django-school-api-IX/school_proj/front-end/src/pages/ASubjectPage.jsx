import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import { Subject } from "../components/Subject";

export const ASubjectPage = () => {
  const [subject, setSubject] = useState(null);
  const { name } = useParams();

  useEffect(() => {
    const getSubject = async () => {
      let response = await axios.get(
        `http://127.0.0.1:8000/api/v1/subjects/${name}/`
      );
      setSubject(response.data);
    };
    getSubject();
  }, []);

  return <>{subject ? <Subject subject={subject} /> : null}</>;
};
