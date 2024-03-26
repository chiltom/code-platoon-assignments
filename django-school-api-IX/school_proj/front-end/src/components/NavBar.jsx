import { Link } from "react-router-dom";

export const NavBar = () => {
    return(
    <nav>
        <Link to="/">Home</Link>
        <Link to="/students/">Students</Link>
        <Link to="/subjects/">Subjects</Link>
    </nav>
    )
}