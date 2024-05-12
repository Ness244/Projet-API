import React, { useState } from 'react';
import styles from './Login.module.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // handle login logic here
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