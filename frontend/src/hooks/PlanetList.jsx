import {useEffect, useState} from "react";
import axios from 'axios'

export const usePlanetsData = () => {
    const [planets, setPlanets] = useState([]);
  
    useEffect(() => {
      axios.get(`http://127.0.0.1:8000/api/planets/?api_key=${process.env.REACT_APP_API_KEY}`)
        .then(response => {
          setPlanets(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return planets;
  };
  