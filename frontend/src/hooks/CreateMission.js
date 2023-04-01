import { useState } from 'react';

export const useCreateMission = () => {
  const [error, setError] = useState(null);

  async function getMission(email) {
    const response = await fetch('http://127.0.0.1:8000/api/mission/create?api_key=150af2b4256f7b9a3e0b68c6c6b92eb974cbef0c', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email }),
    });
    if (response.ok) {
      setError(null);
    } else {
      const data = await response.json();
      setError(data);
    }
  }

  return [error, getMission];
}