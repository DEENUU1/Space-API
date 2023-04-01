import React, { useState } from "react";
import { useMissionsData } from '../hooks/MissionList';
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";


const MissionsPage = () => {
    const missions = useMissionsData();


    return (
        <>
        <NavigationBar/>
        <Background/>
            <div>
                <h1 style={{textAlign: 'center', color: 'white'}}>Missions</h1>
                {missions.map(mission => (
                    <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                        <Card style={{ width: '30rem' }} className="text-center">
                        <Card.Img variant="top" src={mission.image} />
                        <Card.Body>
                            <Card.Title>{mission.name}</Card.Title>
                            <Card.Text>{mission.description}</Card.Text>
                        </Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>Date start: {mission.date_start}</ListGroup.Item>
                            <ListGroup.Item>Date end: {mission.data_end}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </>
    );
};

export default MissionsPage;
