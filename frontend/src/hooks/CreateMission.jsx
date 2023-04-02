import { useState } from 'react';

export const useCreateMission = () => {
  const [error, setError] = useState(null);

  async function createMission(image, name, description, dateStart, dateEnd, rocket, apiKey) {
    const formData = new FormData();
    formData.append('image', image);
    formData.append('name', name);
    formData.append('description', description);
    formData.append('date_start', dateStart);
    formData.append('date_end', dateEnd);
    formData.append('rocket', rocket);

    const response = await fetch(`http://127.0.0.1:8000/api/mission/create?api_key=${apiKey}`, {
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
