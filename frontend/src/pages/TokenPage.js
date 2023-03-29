import React, { useState } from 'react';
import {useGetToken} from '../hooks/GetToken';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import NavigationBar from '../components/NavigationBar';

function TokenPage() {
    const [email, setEmail] = useState('');
    const [error, getToken] = useGetToken();
  
    function handleSubmit(event) {
      event.preventDefault();
      getToken(email);
    }
  
    return (
      <>
      <NavigationBar/>
      <h1 style={{textAlign: "center"}}>Get Token</h1>  
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '200px'}}>
      
          <form onSubmit={handleSubmit}>
              <Form.Control type="email" placeholder="Email address" value={email} onChange={(event) => setEmail(event.target.value)} />
          </form>
          <Button variant="outline-secondary" type="submit">Get Token</Button>

        </div>
      </>
    );
  };

export default TokenPage;