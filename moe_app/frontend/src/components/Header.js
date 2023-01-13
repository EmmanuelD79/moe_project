import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import { Navbar, NavDropdown } from 'react-bootstrap';
import AuthContext from "../utils/context";
import { useContext } from 'react';
import { FiLogIn, FiLogOut, FiUser } from 'react-icons/fi';


function Header() {
  const { user, logout } = useContext(AuthContext);

  return (

    <Navbar bg="light" variant="light">
    <Container>
      <Navbar.Brand href="#home">MOE APP</Navbar.Brand>
      <Navbar.Toggle />
      <Nav.Link href="/">Home</Nav.Link>
      <Nav>
        { user && (<Nav.Link href="/dashboard">Dashboard</Nav.Link>)}
        { user && (
          <NavDropdown title="Contact" id="dropdown-contact">
            <NavDropdown.Item href="/contact">Liste des contacts</NavDropdown.Item>
            <NavDropdown.Item href="/addcontact">
              Ajouter un contact
            </NavDropdown.Item>
        </NavDropdown>)}
        { user && (
          <NavDropdown title="Société" id="dropdown-company">
            <NavDropdown.Item href="/company">Liste des société</NavDropdown.Item>
            <NavDropdown.Item href="/addcompany">
              Ajouter une société
            </NavDropdown.Item>
        </NavDropdown>)}
        { user && (
          <NavDropdown title="Projet" id="dropdown-project">
            <NavDropdown.Item href="/project">Liste des projets</NavDropdown.Item>
            <NavDropdown.Item href="/addproject">
              Ajouter un projet
            </NavDropdown.Item>
        </NavDropdown>)}
      </Nav>
      <Navbar.Collapse className="justify-content-end">
          <Nav>
            {!user && (
                <>
                  <Nav.Link href="/register" >
                  < FiUser className='me-1 align-middle'/>
                    <span className='align-middle'>S'inscrire</span>
                  </Nav.Link>
                  <Nav.Link href="/login">
                    < FiLogIn className='me-1 align-middle'/>
                    <span className='align-middle'>Login</span>
                  </Nav.Link>
                </>
              )}
            {user && <Nav.Link href="#">{user?.email}</Nav.Link>}

          </Nav>
          <Nav>
              {user && (
                <Button
                  variant="outline-success"
                  type="button"
                  onClick={() => {
                    logout();
                  }}
                >
                  < FiLogOut className='me-1 align-middle'/>
                  <span className='align-middle'>Logout</span>
                </Button>
              )}
            </Nav>

      </Navbar.Collapse>
    </Container>
  </Navbar>
  );
}

export default Header;