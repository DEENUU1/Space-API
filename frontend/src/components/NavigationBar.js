import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import 'bootstrap/dist/css/bootstrap.css';

function NavigationBar() {
  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/">Space API</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="http://127.0.0.1:8000/api/swagger/">Docs</Nav.Link>
            <NavDropdown title="Links" id="collasible-nav-dropdown">
              <NavDropdown.Item href="https://github.com/DEENUU1/">GitHub</NavDropdown.Item>
              <NavDropdown.Item href="https://www.linkedin.com/in/kacper-wlodarczyk/">LinkedIn</NavDropdown.Item>
            </NavDropdown>
          </Nav>
          <Nav>
            <Nav.Link href="http://127.0.0.1:3000/token">Get your API KEY</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;