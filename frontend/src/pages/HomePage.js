import React from "react";
import NagationBar from '../components/NavigationBar';

const HomePage = () => {
    return (
        <div>
            <NagationBar/>
            <div>
                <h1>Space API </h1>
                <a href='/planets'>List of planets</a><br></br>
                <a href='/galaxies'>List of galaxies</a>
            </div>
        </div>
    )
}

export default HomePage  