import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import { Home } from "./pages/HomePage";
import { AStudentPage } from "./pages/AStudentPage";
import { ASubjectPage } from "./pages/ASubjectPage";
import { StudentsPage } from "./pages/StudentsPage";
import { SubjectsPage } from "./pages/SubjectsPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "students/",
        element: <StudentsPage />,
      },
      {
        path: "students/:id/",
        element: <AStudentPage />,
      },
      {
        path: "subjects/",
        element: <SubjectsPage />,
      },
      {
        path: "subjects/:name/",
        element: <ASubjectPage />,
      },
    ],
  },
]);

export default router;
