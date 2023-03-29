import React from "react";
import { usePlanetsData } from '../hooks/PlanetList'
import NagationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'

const PlanetsPage = () => {
    const planets = usePlanetsData();
    
    return (
        <div>
        <NagationBar/>
            <div>
                <h1 style={{textAlign: 'center'}}>Planets</h1>
                {planets.map(planet => (
                    <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                        <Card style={{ width: '30rem' }} className="text-center">
                        <Card.Img variant="top" src={planet.image} />
                        <Card.Body>
                            <Card.Title>{planet.name}</Card.Title>
                            <Card.Text>{planet.description}</Card.Text>
                        </Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>Age: {planet.age}</ListGroup.Item>
                            <ListGroup.Item>Star: {planet.star}</ListGroup.Item>
                            <ListGroup.Item>Number of stars: {planet.number_of_stars}</ListGroup.Item>
                            <ListGroup.Item>Orbital period: {planet.orbital_period}</ListGroup.Item>
                            <ListGroup.Item>Satellites: {planet.setellites}</ListGroup.Item>
                            <ListGroup.Item>Mean radius: {planet.mean_radius}</ListGroup.Item>
                            <ListGroup.Item>Mass: {planet.mass}</ListGroup.Item>
                            <ListGroup.Item>Gravity on surface: {planet.surface_gravity}</ListGroup.Item>
                            <ListGroup.Item>Min temp: {planet.surface_temp_min}</ListGroup.Item>
                            <ListGroup.Item>Max temp: {planet.surface_temp_max}</ListGroup.Item>
                            <ListGroup.Item>Mean temp: {planet.surface_temp_mean}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </div>
    );
};

export default PlanetsPage;
