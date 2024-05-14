import React, { useState, useEffect } from 'react';
import axios from 'axios';
import api from "./api.js";
import styles from './UserManagement.module.css';

const UserManagement = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [newPassword, setNewPassword] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [newRole, setNewRole] = useState(Boolean);
  const [newUsername, setNewUsername] = useState ('');

  // Fetch all users from the API
  const fetchUsers = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/user', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });
      if (Array.isArray(response.data['data'])) {
        setUsers(response.data['data']);
      } else {
        console.error('Response data is not an array', response.data);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Update a user's password, email, and role
  const handleUpdateUser = async () => {
    try {
      const response = await axios.patch(`http://127.0.0.1:5000/api/user`, {
        username : newUsername, password : newPassword, email :newEmail, is_superuser: newRole
    }, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
      
    });
      if (response.status === 200) {
        alert('User updated successfully');
        fetchUsers(); // Refresh the list of users
        setSelectedUser(null); // Clear the selected user
      }
      else if (response.status === 404) {
        alert('Username not found in the database');
      } 
      else if (response.status === 403) {
        alert('You do not have permission to update this user');
      }
    } catch (error) {
        console.error(error);
      }
    };

  // Fetch the list of users when the component mounts
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>User Management</h1>
      {/* List of users */}
      <ul className={styles.userList}>
        {users.map((user) => (
          <li key={user.id} onClick={() => setSelectedUser(user)}>
            {user.username} ({user.email}, {user.role})
          </li>
        ))}
      </ul>
      {/* Form for updating a user */}
      {selectedUser && (
        <div className={styles.formContainer}>
          <h2 className={styles.formTitle}>Update User</h2>
          <form className={styles.form}>
          <label className={styles.label}>
              username:
              <input
                type="username"
                className={styles.input}
                value={newUsername}
                onChange={(e) => setNewUsername(e.target.value)}
                required
              />
              </label>
            <label className={styles.label}>
              Password:
              <input
                type="password"
                className={styles.input}
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                required
              />
            </label>
            <br />
            <label className={styles.label}>
              Email:
              <input
                type="email"
                className={styles.input}
                value={newEmail}
                onChange={(e) => setNewEmail(e.target.value)}
                required
              />
            </label>
            <br />
            <label className={styles.label}>
              Role:
              <select className={styles.input} value={newRole} onChange={(e) => setNewRole(e.target.value)}>
                <option value="True">User</option>
                <option value="False">Admin</option>
              </select>
              </label>
            <br />
            <button type="button" className={styles.button} onClick={handleUpdateUser}>
              Update
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default UserManagement;