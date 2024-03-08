/* eslint-disable  */

import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

const MyNavbar = () => {
  return (
    <Navbar expand="lg" className="bg-gray-400 flex flex-row items-center">
      <Navbar.Brand className="ml-6 inline-flex items-center">
        <img
          src="https://i.pinimg.com/474x/f4/93/59/f49359cb388713901955962e6eb075af.jpg"
          width="50px"
          height="50px"
          className="d-inline-block align-top mr-3"
        />
        <Link className="hover:drop-shadow" to="/">
          Rick and Morty
        </Link>
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto ml-6">
          <Nav.Item>
            <Link
              className="hover:drop-shadow mr-2"
              to="/about/"
              id="aboutLink"
            >
              About
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link
              className="hover:drop-shadow mr-2"
              to="/characters/"
              id="charactersLink"
            >
              Characters
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link
              className="hover:drop-shadow mr-2"
              to="/favorites/"
              id="favoritesLink"
            >
              Favorites
            </Link>
          </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default MyNavbar;
