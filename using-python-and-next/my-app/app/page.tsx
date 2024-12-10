'use client'
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('/api/hello');
      setMessage(response.data.message);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Next.js + Python Flask App</h1>
      <p>{message}</p>
    </div>
  );
}
