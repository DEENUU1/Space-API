import React from "react";
import NavigationBar from '../components/NavigationBar';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup'
const HomePage = () => {
    return (
        <>
        <NavigationBar/>
            <CardGroup>
                <Card style={{width: "20rem"}}>
                    <Card.Img style={{width: "30rem", height: "30rem"}} variant='top' src="https://www.thephotoargus.com/wp-content/uploads/2017/07/earth-7.jpg" />
                    <Card.Body>
                        <Card.Title>List of planets</Card.Title>
                        <Card.Text>
                            ad adsas dskdskdask lskdsal kdl dasld kasl dksal adskl
                        </Card.Text>
                        <Card.Link href="/planets">Click here!</Card.Link>
                    </Card.Body>
                </Card>
                <Card style={{width: "20rem"}}>
                    <Card.Img style={{width: "30rem", height: "30rem"}} variant='top' src="https://i2.wp.com/nypost.com/wp-content/uploads/sites/2/2017/03/170320-solar-system-planets-feature.jpg?quality=90&strip=all&ssl=1" />
                    <Card.Body>
                        <Card.Title>List of systems</Card.Title>
                        <Card.Text>
                            ad adsas dskdskdask lskdsal kdl dasld kasl dksal adskl
                        </Card.Text>
                        <Card.Link href="/systems">Click here!</Card.Link>
                    </Card.Body>
                </Card>
                <Card style={{width: "20rem"}}>
                    <Card.Img style={{width: "30rem", height: "30rem"}} variant='top' src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Milky_Way_2010.jpg" />
                    <Card.Body>
                        <Card.Title>List of galaxies</Card.Title>
                        <Card.Text>
                            ad adsas dskdskdask lskdsal kdl dasld kasl dksal adskl
                        </Card.Text>
                        <Card.Link href="/galaxies">Click here!</Card.Link>
                    </Card.Body>
                </Card>
                
            </CardGroup>
        </>
    )
}

export default HomePage  