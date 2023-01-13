import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { useRef, useState } from "react";
import { Container, Row, Col, Alert } from 'react-bootstrap';
import axiosInstance from "../API";
import { useNavigate } from "react-router-dom";

const Register = () => {

    const navigate = useNavigate()
    const email = useRef("");
    const firstName = useRef("");
    const lastName = useRef("");
    const password = useRef("");
    const password2 = useRef("");

    const [ msg, setMsg] = useState("");

    const register = async (newUser) => {
        await axiosInstance.post("register/", newUser);
      };

    const onSubmit = async () => {
        let newUser = {
            email: email.current.value,
            password: password.current.value,
            first_name: firstName.current.value,
            last_name: lastName.current.value,
            password2: password2.current.value
          };
          try {
            await register(newUser);
            navigate("/");
            } catch (e) {
                console.log(e.response);
            };
      };


    return (
    
        <div className='Login-content' >
            <Container className='my-4 w-75'>
                <Card style={{color:'black', borderColor:'#282c34'}}>
                    <Row>
                        <Col md={5} className='px-0' >
                            <Card.Img 
                                className="d-none d-xl-block img-fluid" 
                                src="https://images.unsplash.com/photo-1509453721491-c3af5961df76?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format" 
                            />
                        </Col>
                        <Col className='ml-0'>
                            <Card.Body>
                                <Card.Title className="mb-5 text-uppercase text-center">
                                    S'inscrire
                                </Card.Title>
                                { msg !=="" && (<Alert variant='danger'>
                                    {msg}
                                </Alert>)}
                                <Form onSubmit={onSubmit} >
                                    <Form.Group as={Col} controlId="formBasicEmail">
                                        <Form.Control className="form-control form-control-lg" ref={email} name='email' type="email"/>
                                        <Form.Label className="form-label">Email</Form.Label>
                                    </Form.Group>
                                    <Form.Group className="row">
                                        <Form.Group as={Col} controlId="formBasicFirstName">
                                            <Form.Control className="form-control form-control-lg" ref={firstName} name='firstName' type="text"/>
                                            <Form.Label className="form-label">Prénom</Form.Label>
                                        </Form.Group>
                                        <Form.Group as={Col} controlId="formBasicLastName">
                                            <Form.Control className="form-control form-control-lg" ref={lastName} name='lastName' type="text"/>
                                            <Form.Label className="form-label">Nom</Form.Label>
                                        </Form.Group>
                                    </Form.Group>
                                    <Form.Group as={Col} controlId="formBasicPassword">
                                        <Form.Control className="form-control form-control-lg" ref={password} name='password' type="password"/>
                                        <Form.Label className="form-label">Mot de passe</Form.Label>
                                    </Form.Group>
                                    <Form.Group as={Col} controlId="formBasicPassword2">
                                        <Form.Control className="form-control form-control-lg" ref={password2} name='password2' type="password"/>
                                        <Form.Label className="form-label">Confirmer le mot de passe</Form.Label>
                                    </Form.Group>
                                    <Form.Group className="d-flex justify-content-end pt-3">
                                        <Button className="btn-lg" variant="light" type="button">
                                            Annuler
                                        </Button>
                                        <Button className="ms-2 btn-lg" variant="warning" type="button" onClick={onSubmit}>
                                            Confirmer
                                        </Button>
                                    </Form.Group>
                                </Form>
                            </Card.Body >
                        </Col>
                    </Row>
                </Card>
            </Container>
      </div>
    )
}

export default Register;