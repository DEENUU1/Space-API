import React, { useState } from 'react';
import { useGetToken } from '../hooks/GetToken';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import NavigationBar from '../components/NavigationBar';
import Background from "../components/Background";

function TokenPage() {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);
  const [error, getToken] = useGetToken();

  function handleSubmit(event) {
    event.preventDefault();
    getToken(email, username)
      .then(() => setIsSuccess(true))
      .catch(() => setIsError(true));
  }

  function handleFormReset() {
    setEmail('');
    setUsername('');
    setIsSuccess(false);
  }

  return (
    <>
      <NavigationBar />
      <Background />
      <h1 style={{ textAlign: "center", marginTop: "50px" }}>Get Token</h1>
      
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '200px' }}>
        {isSuccess ? (

          <div style={{textAlign: "center"}}>
            <h3 style={{fontSize: "30px"}}>Form submitted successfully!</h3>
            <p style={{fontSize: "20px"}}>API key sent to your email address</p>
          </div>

        ) : (
          <Form onSubmit={handleSubmit} onReset={handleFormReset}>
          <Form.Group style={{width: "300px"}}>

            <Form.Control type="email" placeholder="Email address" value={email} onChange={(event) => setEmail(event.target.value)} />
            <Form.Control type='text' placeholder='Username' value={username} onChange={(event) => setUsername(
              event.target.value)} />
            <Button variant="outline-secondary" type="submit">Get Token</Button>
          </Form.Group>
          </Form>
        )}
        </div>
        <div style={{display: "flex", alignItems: "center", justifyContent: "center"}}>
          <a href='/delete-token' >If you want to delete your token. Click here</a>
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

export default TokenPage;
