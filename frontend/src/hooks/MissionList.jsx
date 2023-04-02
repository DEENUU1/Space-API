import {useEffect, useState} from "react";
import axios from 'axios'

export const useMissionsData = () => {
    const [missions, setMissions] = useState([]);
  
    useEffect(() => {
      axios.get(`http://127.0.0.1:8000/api/missions/?api_key=${process.env.REACT_APP_API_KEY}`)
        .then(response => {
          setMissions(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return missions;
  };
  