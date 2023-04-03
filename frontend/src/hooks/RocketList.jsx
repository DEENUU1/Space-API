import {useEffect, useState} from "react";
import axios from 'axios'

export const useRocketsData = () => {
    const [rockets, setRockets] = useState([]);
  
    useEffect(() => {
      axios.get(`http://127.0.0.1:8000/api/rockets/?api_key=${process.env.REACT_APP_API_KEY}`)
        .then(response => {
          setRockets(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return rockets;
  };
  