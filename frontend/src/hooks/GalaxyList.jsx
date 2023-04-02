import {useEffect, useState} from "react";
import axios from 'axios'


export const useGalaxysData = () => {
    const [galaxies, setGalaxies] = useState([]);
  
    useEffect(() => {
      axios.get(`http://127.0.0.1:8000/api/galaxies/?api_key=${process.env.REACT_APP_API_KEY}`)
        .then(response => {
          setGalaxies(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return galaxies;
  };
  