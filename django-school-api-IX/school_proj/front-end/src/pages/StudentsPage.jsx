import axios from "axios";
import { useState, useEffect } from "react";
import { Student } from "../components/Student";

export const StudentsPage = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    const getStudents = async () => {
      let response = await axios.get("http://127.0.0.1:8000/api/v1/students/");
      setStudents(response.data);
    };
    getStudents();
  }, []);

  return (
    <>
      {students.map((student) => (
        <Student student={student} />
      ))}
    </>
  );
};
