import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Student } from "../components/Student";
import axios from "axios";

export const AStudentPage = () => {
  const { id } = useParams();
  const [student, setStudent] = useState(null);

  useEffect(() => {
    const getStudent = async () => {
      let response = await axios.get(
        `http://127.0.0.1:8000/api/v1/students/${id}/`
      );
      setStudent(response.data);
    };
    getStudent();
  }, []);
  return <>{student ? <Student student={student} /> : null}</>;
};
