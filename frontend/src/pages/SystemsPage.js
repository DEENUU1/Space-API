import React from "react";
import { useGalaxysData, usePlanetsData, useSystemsData } from '../hooks/SystemList'
import NagationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'

const GalaxiesPage = () => {
    const systems = useSystemsData();
    
    return (
        <div>
        <NagationBar/>
            <div>
                <h1 style={{textAlign: 'center'}}>Systems</h1>
                {systems.map(system => (
                    <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                        <Card style={{ width: '30rem' }} className="text-center">
                        <Card.Img variant="top" src={system.image} />
                        <Card.Body>
                            <Card.Title>{system.name}</Card.Title>
                            <Card.Text>{system.description}</Card.Text>
                        </Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>Age: {system.age}</ListGroup.Item>
                            <ListGroup.Item>Star: {system.star}</ListGroup.Item>
                            <ListGroup.Item>Number of stars: {system.number_of_stars}</ListGroup.Item>
                            <ListGroup.Item>Orbital period: {system.orbital_period}</ListGroup.Item>
                            <ListGroup.Item>Satellites: {system.setellites}</ListGroup.Item>
                            <ListGroup.Item>Number of satellites: {system.satellites}</ListGroup.Item>
                            <ListGroup.Item>Mass: {system.mass}</ListGroup.Item>
                            <ListGroup.Item>Mean temp: {system.surface_temp_mean}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </div>
    );
};

export default GalaxiesPage;
