import React from 'react'
import { Navbar,Nav,Container,Rol,Col,NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

function Headers() {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
            <Container>

              <LinkContainer to='/'>
                <Navbar.Brand>Assesment</Navbar.Brand>
              </LinkContainer>
            
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="ml-auto">
                <LinkContainer to='/cart'>
                  <Nav.Link>Cart</Nav.Link>
                </LinkContainer>
                
                <LinkContainer to='/login'>
                <Nav.Link>Login</Nav.Link>
                </LinkContainer>
                
              </Nav>
            </Navbar.Collapse>
            </Container>
        </Navbar>
      );
}

export default Headers