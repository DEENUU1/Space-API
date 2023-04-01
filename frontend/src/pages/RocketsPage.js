import React from "react";
import { useRocketsData } from '../hooks/RocketList'
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";

const RocketsPage = () => {
    const rockets = useRocketsData();
    
    return (
        <>
        <NavigationBar/>
        <Background/>
            <div>
                <h1 style={{textAlign: 'center', color: 'white'}}>Rockets</h1>
                {rockets.map(rocket => (
                    <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                        <Card style={{ width: '30rem' }} className="text-center">
                        <Card.Img variant="top" src={rocket.image} />
                        <Card.Body>
                            <Card.Title>{rocket.name}</Card.Title>
                            <Card.Text>{rocket.description}</Card.Text>
                        </Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>Manufacturer: {rocket.manufacturer}</ListGroup.Item>
                            <ListGroup.Item>Height: {rocket.height}</ListGroup.Item>
                            <ListGroup.Item>Mass: {rocket.mass}</ListGroup.Item>
                            <ListGroup.Item>Stages: {rocket.stages}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </>
    );
};

export default RocketsPage;
