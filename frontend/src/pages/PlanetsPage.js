import React from "react";
import { usePlanetsData } from '../hooks/planets.js'

const PlanetsPage = () => {
  const planets = usePlanetsData();

  return (
    <div>
      <h1>Planets</h1>
      <div>
        {planets.map(planet => (
          <div key={planet.name}>
            <h3>{planet.name}</h3>
            <p>{planet.description}</p>
            <h4>More informations about this planet</h4>
            <ul>
              <li>Age: {planet.age}</li>
              <li>Star: {planet.star}</li>
              <li>Number of stars: {planet.number_of_stars}</li>
              <li>Orbital period: {planet.orbital_period}</li>
              <li>Setellites: {planet.setellites}</li>
              <li>Mean radius: {planet.mean_radius}</li>
              <li>Mass: {planet.mass}</li>
              <li>Gravity on surface: {planet.surface_gravity}</li>
              <li>Min temp: {planet.surface_temp_min}</li>
              <li>Max temp: {planet.surface_temp_max}</li>
              <li>Mean temp: {planet.surface_temp_mean}</li>
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PlanetsPage;
