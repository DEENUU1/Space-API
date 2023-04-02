import React from "react";
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";
import ReactDOM from 'react-dom';

const HomePage = () => {
    return (
        <>
        <NavigationBar/>
        <Background/>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px', margin: '10px'}}>
                    <Card style={{width: '30rem' }} className="text-center">
                    <Card.Body>
                        <Card.Title> Planet List </Card.Title>
                        <Card.Text> A list of all planets in our database </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/planets">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px', margin: '10px'}}>
                <Card style={{width: '30rem' }} className="text-center">
                    <Card.Body>
                        <Card.Title> System List </Card.Title>
                        <Card.Text>  A list of all planetary System in our database </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/systems">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px', margin: '10px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Body>
                        <Card.Title> Galaxies List </Card.Title>
                        <Card.Text>  A list of all galaxies in our database </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/galaxies">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px', margin: '10px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Body>
                        <Card.Title> Rockets List </Card.Title>
                        <Card.Text>  A list of all rockets in our database </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/rockets">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px', margin: '10px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Body>
                        <Card.Title> Mission List </Card.Title>
                        <Card.Text>  A list of all missions in our database. If you have a API key you can create a new </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/missions">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
        </>
    )
}

export default HomePage  