import { Link } from "react-router-dom";
export const Subject = ({ subject }) => {
  return (
    <ol>
      <li><Link to={`/subjects/${subject.subject_name}/`}>Name: {subject.subject_name}</Link></li>
      <li>Professor: {subject.professor}</li>
      <li>Total Number of students: {subject.students}</li>
      <li>Grade Average: {subject.grade_average}</li>
    </ol>
  );
};
