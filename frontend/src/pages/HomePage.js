import React from "react";
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup'
import Background from "../components/Background";

const HomePage = () => {
    return (
        <>
        <NavigationBar/>
        <Background/>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Img variant="top" src="https://www.thephotoargus.com/wp-content/uploads/2017/07/earth-7.jpg" />
                    <Card.Body>
                        <Card.Title> Planet List </Card.Title>
                        <Card.Text> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/planets">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Img variant="top" src="https://i.ytimg.com/vi/3bGraeIkaJw/maxresdefault.jpg" />
                    <Card.Body>
                        <Card.Title> System List </Card.Title>
                        <Card.Text> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/systems">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Img variant="top" src="https://spacetechnologyandrealscience.files.wordpress.com/2012/01/milky-way.jpg" />
                    <Card.Body>
                        <Card.Title> Galaxies List </Card.Title>
                        <Card.Text> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/galaxies">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
                <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '20px'}}>
                    <Card style={{ width: '30rem' }} className="text-center">
                    <Card.Img variant="top" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Arabsat-6A_Mission_(40628442293).jpg/1200px-Arabsat-6A_Mission_(40628442293).jpg" />
                    <Card.Body>
                        <Card.Title> Rockets List </Card.Title>
                        <Card.Text> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor </Card.Text>
                    </Card.Body>
                    <ListGroup variant="flush">
                        <Card.Link href="/rockets">Click here!</Card.Link>
                    </ListGroup>
                    </Card>
                </div>
        </>
    )
}

export default HomePage  