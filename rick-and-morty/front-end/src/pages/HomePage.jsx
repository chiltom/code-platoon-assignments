import { NavDropdown } from 'react-bootstrap';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

const HomePage = () => {

    return (
        <>
            <Navbar expand="lg" className='bg-body-tertiary'>
                <Navbar.Brand className='ml-10' href='/'>Rick and Morty</Navbar.Brand>
                <Navbar.Toggle aria-controls='basic-navbar-nav' />
                <Navbar.Collapse id='basic-navbar-nav'>
                    <Nav className='me-auto'>
                        <Nav.Link className='ml-10' href='/'>Home</Nav.Link>
                        <NavDropdown className='ml-10' title="Dropdown" id="basic-nav-dropdown">
                            <NavDropdown.Item href='/'>Home again</NavDropdown.Item>
                            <NavDropdown.Item href='/'>Home again x2</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href='/'>We're going home again?</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>
    )
}

export default HomePage;