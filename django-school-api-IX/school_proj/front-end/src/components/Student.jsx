import { Link } from "react-router-dom";
import { Subject } from "./Subject";

export const Student = ({ student }) => {
  return (
    <ul>
      <h2><Link to={`/students/${student.id}/`}>{student.name}</Link></h2>
      <li>Student Email: {student.student_email}</li>
      <li>Personal Email: {student.personal_email}</li>
      <li>
        Locker Number: {student.locker_number} <br />
        Locker Combination: {student.locker_combination}
      </li>
      <li>
        <p>
          {student.name}
          {student.good_student ? (
            <>is a good student</>
          ) : (
            <>is a bad student</>
          )}
        </p>
      </li>
      <h5>Subjects</h5>
      {student.subjects.map((subject) => (
        <Subject subject={subject} />
      ))}
    </ul>
  );
};
