import { useState } from 'react';

export const useDeleteToken = () => {
  const [error, setError] = useState(null);

  async function deleteToken(email, token) {
    const response = await fetch('http://127.0.0.1:8000/delete-token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, token }),
    });
    if (response.ok) {
      setError(null);
    } else {
      const data = await response.json();
      setError(data);
    }
  }

  return [error, deleteToken];
}