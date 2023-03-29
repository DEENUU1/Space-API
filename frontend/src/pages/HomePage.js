import React from "react";
import NavigationBar from '../components/NavigationBar';

const HomePage = () => {
    return (
        <>
        <NavigationBar/>
            <div>
                <h1>Space API </h1>
                <a href='/planets'>List of planets</a><br></br>
                <a href='/galaxies'>List of galaxies</a><br></br>
                <a href='/systems'>List of systems</a><br></br>
            </div>
        </>
    )
}

export default HomePage  