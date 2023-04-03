import { useState } from 'react';

export const useGetToken = () => {
  const [error, setError] = useState(null);

  async function getToken(email, username) {
    const response = await fetch('http://127.0.0.1:8000/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, username }),
    });
    if (response.ok) {
      setError(null);
    } else {
      const data = await response.json();
      const username = await response.json();
      setError(data);
    }
  }

  return [error, getToken];
}