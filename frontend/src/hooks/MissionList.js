import {useEffect, useState} from "react";
import axios from 'axios'

export const useMissionsData = () => {
    const [missions, setMissions] = useState([]);
  
    useEffect(() => {
      axios.get('http://127.0.0.1:8000/api/missions/?api_key=150af2b4256f7b9a3e0b68c6c6b92eb974cbef0c')
        .then(response => {
          setMissions(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return missions;
  };
  