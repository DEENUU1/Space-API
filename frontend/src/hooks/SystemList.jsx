import {useEffect, useState} from "react";
import axios from 'axios'

export const useSystemsData = () => {
    const [systems, setSystems] = useState([]);
  
    useEffect(() => {
      axios.get(`http://127.0.0.1:8000/api/systems/?api_key=${process.env.REACT_APP_API_KEY}`)
        .then(response => {
          setSystems(response.data.results);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return systems;
  };
  