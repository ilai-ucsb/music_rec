import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

// Basic NavBar using react-bootstrap

function NavBarApp() {
  return (
    <Navbar variant="dark" bg="dark" expand="lg">
        <Container>
            <Navbar.Brand href='/'>Music Recommendation App</Navbar.Brand>
        </Container>
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className='justify-content-end'>
                <Nav.Link href='/'>Home</Nav.Link>
                <Nav.Link href='/about'>About</Nav.Link>
                <Nav.Link href='/login'>Login</Nav.Link>
            </Nav>
        </Navbar.Collapse>
    </Navbar>
  );
}

export default NavBarApp;