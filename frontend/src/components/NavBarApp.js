import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { loginUrl } from './pages/utils/spotifyUtils';

// Basic NavBar using react-bootstrap

function NavBarApp() {
  return (
    <Navbar variant="dark" bg="black" expand="lg">
        <Container>
            <Navbar.Brand href='/'>
              <img src="./rekofyLogoLight.png" alt="Rekofy" height={30} />
            </Navbar.Brand>
        </Container>
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className='justify-content-end'>
                <Nav.Link href='/'>Home</Nav.Link>
                <Nav.Link href='/about'>About</Nav.Link>
                <Nav.Link href={loginUrl}>Login</Nav.Link>
            </Nav>
        </Navbar.Collapse>
    </Navbar>
  );
}

export default NavBarApp;