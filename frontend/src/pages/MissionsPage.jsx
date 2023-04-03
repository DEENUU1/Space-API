import React, { useState } from "react";
import { useMissionsData } from '../hooks/MissionList';
import { useCreateMission } from '../hooks/CreateMission';
import { useRocketsData } from '../hooks/RocketList';
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";
import Form from 'react-bootstrap/Form';
import Button from "react-bootstrap/Button";

const MissionsPage = () => {
    const missions = useMissionsData();
    const [image, setImage] = useState(null);
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [dateStart, setDateStart] = useState('');
    const [dateEnd, setDateEnd] = useState('');
    const [rocket, setRocket] = useState('');
    const [error, getMission] = useCreateMission();
    const [apiKey, setApiKey] = useState('');
    const rockets = useRocketsData();
    const [isError, setIsError] = useState('');
    const [isSuccess, setIsSuccess] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!apiKey || !name || !description) {
            setIsError(true);
            return;
        }

        await getMission(image, name, description, dateStart, dateEnd, rocket, apiKey)
            .then(() => setIsSuccess(true))
            .catch((error) => (true));
    }

    function handleFormReset() {
        setApiKey('');
        setIsSuccess(false);
    }


    return (
        <>
        <NavigationBar/>
        <Background/>
            <h1 style={{textAlign: "center"}}>Create new mission</h1>
            <div style={{display: "flex", justifyContent: "center", alignItems: "center"}}>

            {isSuccess ? (

            <div style={{textAlign: "center"}}>
            <h3 style={{fontSize: "30px"}}>Form submitted successfully!</h3>
            <p style={{fontSize: "20px"}}>New mission added to the database</p>
            </div>

            ) : (

                <Form onSubmit={handleSubmit}>
            <Form.Group style={{width: "300px"}}>
                <Form.Label htmlFor="name">Name:</Form.Label>
                <Form.Control type="text" id="name" value={name} onChange={(event) => setName(event.target.value)}/>

                <Form.Label htmlFor="description">Description:</Form.Label>
                <Form.Control as="textarea" id="description" value={description} onChange={(event) => setDescription(event.target.value)}/>

                <Form.Label htmlFor="date_start">Start Date:</Form.Label>
                <Form.Control type="date" id="date_start" value={dateStart} onChange={(event) => setDateStart(event.target.value)}/>

                <Form.Label htmlFor="date_end">End Date:</Form.Label>
                <Form.Control type="date"id="date_end" value={dateEnd} onChange={(event) => setDateEnd(event.target.value)}/>

                <Form.Label htmlFor="rocket">Rocket:</Form.Label>
                <Form.Select id="rocket" value={rocket} onChange={(event) => setRocket(event.target.value)}>
                
                    <option value="">Choose a rocket</option>
                    {rockets.map((rocket) => 
                        <option key={rocket.id} value={rocket.id}>
                            {rocket.name}
                        </option>
                    )}

                </Form.Select>
                <Form.Label htmlFor="image">Image:</Form.Label>
                <Form.Control type="file" id="image" onChange={(event) => setImage(event.target.files[0])}/>
                <Form.Label htmlFor="apiKey">Your api key</Form.Label>
                <Form.Control type="text" id="apiKey" onChange={(event) => setApiKey(event.target.value)}/>

            <Button type="submit">Create</Button>
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
                            <ListGroup.Item>Date end: {mission.date_end}</ListGroup.Item>
                        </ListGroup>
                        </Card>
                    </div>  
                ))}  
            </div>
        </>
    );
};

export default MissionsPage;
