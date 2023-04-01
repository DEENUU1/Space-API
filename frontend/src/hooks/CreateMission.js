import { useState } from 'react';

export const useCreateMission = () => {
  const [error, setError] = useState(null);

  async function createMission(image, name, description, dateStart, dateEnd, rocket) {
    const formData = new FormData();
    formData.append('image', image);
    formData.append('name', name);
    formData.append('description', description);
    formData.append('date_start', dateStart);
    formData.append('date_end', dateEnd);
    formData.append('rocket', rocket);

    const response = await fetch('http://127.0.0.1:8000/api/mission/create?api_key=150af2b4256f7b9a3e0b68c6c6b92eb974cbef0c', {
      method: 'POST',
      body: formData,
    });
    
    if (response.ok) {
      setError(null);
    } else {
      const data = await response.json();
      setError(data);
    }
  }

  return [error, createMission];
}
