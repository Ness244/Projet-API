import React, { useState } from 'react';
import axios from 'axios';
import styles from './Login.module.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleClick = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/user/login', {
        username,
        password,
      });
      if (response.status === 200) {
        const token = response.data["access_token"];
        localStorage.setItem('access_token', token);
        // Redirect to syslog page
        window.location.href = '/syslog';
      }
    } catch (error) {
      setError(error.message);
    }
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    handleClick();
  };

  return (
    <div className={styles.container}>
      <form className={styles.form} onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
        />
        <label htmlFor="password">Password</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
        <button type="submit">Login</button>
        {error && <p>{error}</p>}
        <div>
          <p>
            Don't have an account yet?
            <button
              onClick={() => {
                // navigate to registration page
                window.location.href = '/register';
              }}
            >
              Register here
            </button>
          </p>
        </div>
      </form>
    </div>
  );
};

export default Login;
