import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // corrected the IP address
});

// Add a request interceptor to add the token to the headers
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const registerUser = async (userData) => {
  try {
    const response = await api.post('/user', userData);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const loginUser = async (userData) => {
  try {
    const response = await api.post('/user/login', userData);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const getSyslogs = async (filter) => {
  try {
    const response = await api.get(`/syslog?filter=${filter}`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const addSyslog = async (syslogData) => {
  try {
    const response = await api.post('/syslog', syslogData);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const deleteSyslog = async (syslogId) => {
  try {
    const response = await api.delete(`/syslog/${syslogId}`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const getUser = async () => {
  try {
    const response = await api.get('/user');
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};