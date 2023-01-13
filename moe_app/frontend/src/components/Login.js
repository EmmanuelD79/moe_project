import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState, useRef, useContext } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../utils/context";


const Login = () => {

  const navigate = useNavigate()
  const email = useRef("");
  const password = useRef("");
  const {login}= useContext(AuthContext);
  const [ msg, setMsg] = useState("");
  

  const onSubmit = async () => {
    let payload = {
      email: email.current.value,
      password: password.current.value
    };
    try {
        await login(payload);
        navigate('/contact');

    } catch (e) {
        setMsg(e.response.data.msg);
    } 
  };

  const alertmsg = msg !=="" && (<div className='alert alert-danger' role="alert">{msg}</div>);

  
  return (
    <div className='Login-content'>
      <Form onSubmit={onSubmit} className='w-50 p-3 container'>
        {alertmsg}
      <Form.Group className="mb-3 d-flex justify-content-center" controlId="formBasicEmail">
          <Form.Label style={{width: 200}}>Email</Form.Label>
          <Form.Control name='email' ref={email} type="email" placeholder="Enter email" />
      </Form.Group>

      <Form.Group className="mb-3 d-flex justify-content-center"  controlId="formBasicPassword">
          <Form.Label style={{width: 200}}>Mot de passe</Form.Label>
          <Form.Control name='password' ref={password} type="password" placeholder="Password" />
      </Form.Group>
      <Form.Group className="mb-3 d-flex justify-content-center" controlId="formBasicCheckbox">
          <Form.Check type="checkbox" label="Se rappeler de moi" />
      </Form.Group>
      <Button variant="primary" type="button" onClick={onSubmit}>
          Se connecter
      </Button>
    </Form>

    </div>
  );
}

export default Login;