import React from "react";
import { useGalaxysData, usePlanetsData } from '../hooks/GalaxyList'
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'

const GalaxiesPage = () => {
    const galaxies = useGalaxysData();
    
    return (
        <>
        <NavigationBar/>
             <div>
                <h1 style={{textAlign: 'center'}}>Galaxies</h1>
                {galaxies.map(galaxy => (
                    <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                        <Card style={{ width: '30rem' }} className="text-center">
                        <Card.Img variant="top" src={galaxy.image} />
                        <Card.Body>
                            <Card.Title>{galaxy.name}</Card.Title>
                            <Card.Text>{galaxy.description}</Card.Text>
                        </Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>Age: {galaxy.age}</ListGroup.Item>
                            <ListGroup.Item>Constellation: {galaxy.constellation}</ListGroup.Item>
                            <ListGroup.Item>Number of stars: {galaxy.number_of_stars}</ListGroup.Item>
                            <ListGroup.Item>Distance from earth: {galaxy.distance}</ListGroup.Item>
                            <ListGroup.Item>Type: {galaxy.type}</ListGroup.Item>
                            <ListGroup.Item>Number of satellites: {galaxy.satellites}</ListGroup.Item>
                            <ListGroup.Item>Size: {galaxy.size}</ListGroup.Item>
                            <ListGroup.Item>Mass: {galaxy.mass}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </>    
        );
};



export default GalaxiesPage;
