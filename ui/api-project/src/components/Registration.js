import React, { useState } from 'react';
import axios from 'axios';
import styles from './Registration.module.css';
import api from "./api.js";

const Registration = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("hello");
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/user', {
        username,
        password,
        email,
      });
      if (response.status === 201) {
        alert('Registration successful');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Registration</h1>
      <form className={styles.form} onSubmit={handleSubmit}>
        <label className={styles.label}>
          Username:
          <input
            type="text"
            className={styles.input}
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        <br />
        <label className={styles.label}>
          Password:
          <input
            type="password"
            className={styles.input}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <label className={styles.label}>
          Email:
          <input
            type="email"
            className={styles.input}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit" className={styles.button} on onClick={()=> {
          window.location.href = '/';
        }}>
          Register
        
        </button>
      </form>
      <div>
        <p>
          Already have an account? 
          <button
            onClick={() => {
              // navigate to login page
              window.location.href = '/';
            }}
          >
            Login here
          </button>
        </p>
      </div>
    </div>
  );
};

export default Registration;