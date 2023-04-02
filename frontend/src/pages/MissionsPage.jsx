import React, { useState } from "react";
import { useMissionsData } from '../hooks/MissionList';
import { useCreateMission } from '../hooks/CreateMission';
import { useRocketsData } from '../hooks/RocketList';
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";


const MissionsPage = () => {
    const missions = useMissionsData();
    const [image, setImage] = useState(null);
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [dateStart, setDateStart] = useState('');
    const [dateEnd, setDateEnd] = useState('');
    const [rocket, setRocket] = useState('');
    const [error, getMission] = useCreateMission();
    const [rocketList, setRocketList] = useState('');
    const [apiKey, setApiKey] = useState('');
    const rockets = useRocketsData();

    const handleSubmit = async (event) => {
        event.preventDefault();
        await getMission(image, name, description, dateStart, dateEnd, rocket, apiKey);
    };


    return (
        <>
        <NavigationBar/>
        <Background/>
            <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name:</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                />

                <label htmlFor="description">Description:</label>
                <textarea
                    id="description"
                    value={description}
                    onChange={(event) => setDescription(event.target.value)}
                />

                <label htmlFor="date_start">Start Date:</label>
                <input
                    type="date"
                    id="date_start"
                    value={dateStart}
                    onChange={(event) => setDateStart(event.target.value)}
                />

                <label htmlFor="date_end">End Date:</label>
                <input
                    type="date"
                    id="date_end"
                    value={dateEnd}
                    onChange={(event) => setDateEnd(event.target.value)}
                />

                <label htmlFor="rocket">Rocket:</label>
                <select 
                    id="rocket"
                    value={rocket}
                    onChange={(event) => setRocket(event.target.value)}>
                
                    <option value="">Choose a rocket</option>
                    {rockets.map((rocket) => 
                        <option key={rocket.id} value={rocket.id}>
                            {rocket.name}
                        </option>
                    )}
                </select>
                <label htmlFor="image">Image:</label>
                <input
                    type="file"
                    id="image"
                    onChange={(event) => setImage(event.target.files[0])}
                />
                <label htmlFor="apiKey">Your api key</label>
                <input
                    type="text"
                    id="apiKey"
                    onChange={(event) => setApiKey(event.target.value)}
                />

            <button type="submit">Create</button>
            </form>
            </div>



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
