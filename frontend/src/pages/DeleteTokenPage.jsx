import React, { useState } from 'react';
import {useDeleteToken} from '../hooks/DeleteToken';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import NavigationBar from '../components/NavigationBar';
import Background from "../components/Background";

function DeleteTokenPage() {
    const [email, setEmail] = useState('');
    const [token, setToken] = useState('');
    const [isSuccess, setIsSuccess] = useState('');
    const [isError, setIsError] = useState('');
    const [error, getToken] = useDeleteToken();
  
    function handleSubmit(event) {
      event.preventDefault();

      if (!email || !token) {
        setIsError(true);
        return;
      }

      getToken(email, token)
        .then(() => setIsSuccess(true))
        .catch((error) => (true));
    }
    
    function handleFormReset() {
      setEmail('');
      setToken('');
      setIsSuccess(false);
    }

    return (
      <>
      <NavigationBar/>
      <Background/>
      <h1 style={{textAlign: "center"}}>Delete your Token</h1>  
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '200px'}}>

        {isSuccess ? (

          <div style={{textAlign: "center"}}>
          <h3 style={{fontSize: "30px"}}>Form submitted successfully!</h3>
          <p style={{fontSize: "20px"}}>Your api key has been deleted</p>
          </div>

        ) : (

          <Form onSubmit={handleSubmit} onReset={handleFormReset}>
          <Form.Group style={{width: "300px"}}>
              <Form.Control type="email" placeholder="Email address" value={email} onChange={(event) => setEmail(event.target.value)} />
              <Form.Control type="tect" placeholder="Your token" value={token} onChange={(event) => setToken(event.target.value)} />
              <Button variant="outline-secondary" type="submit">Delete your token</Button>
          </Form.Group>
          </Form>
        )}  
        </div>
        {isError && (
        <div style={{textAlign: "center"}}>
          <h3 style={{fontSize: "30px"}}>Error!</h3>
          <p style={{fontSize: "20px"}}>There was an error submitting the form. Please try again.</p>
        </div>
        )}
      </>
    );
  };

export default DeleteTokenPage;