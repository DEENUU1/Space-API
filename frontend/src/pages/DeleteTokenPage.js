import React, { useState } from 'react';
import {useDeleteToken} from '../hooks/DeleteToken';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import NavigationBar from '../components/NavigationBar';
import Background from "../components/Background";

function DeleteTokenPage() {
    const [email, setEmail] = useState('');
    const [token, setToken] = useState('');
    const [error, getToken] = useDeleteToken();
  
    function handleSubmit(event) {
      event.preventDefault();
      getToken(email, token);
    }
  
    return (
      <>
      <NavigationBar/>
      <Background/>
      <h1 style={{textAlign: "center"}}>Get Token</h1>  
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '200px'}}>
      
          <form onSubmit={handleSubmit}>
              <Form.Control type="email" placeholder="Email address" value={email} onChange={(event) => setEmail(event.target.value)} />
              <Form.Control type="tect" placeholder="Your token" value={token} onChange={(event) => setToken(event.target.value)} />
              <Button variant="outline-secondary" type="submit">Delete your token</Button>
          </form>

        </div>
      </>
    );
  };

export default DeleteTokenPage;