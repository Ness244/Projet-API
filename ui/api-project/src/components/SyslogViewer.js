import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SyslogViewer = () => {
  const [syslogs, setSyslogs] = useState([]);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    const fetchSyslogs = async () => {
      try {
        const response = await axios.get('/api/syslog');
        setSyslogs(response.data);
      } catch (error) {
        console.error('Error fetching syslogs:', error);
      }
    };

    fetchSyslogs();
  }, []);

  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  const filteredSyslogs = syslogs.filter((syslog) => {
    if (filter === '') return true;
    return syslog.message.includes(filter);
  });

  return (
    <div>
      <h1>Syslog Viewer</h1>
      <input type="text" value={filter} onChange={handleFilterChange} placeholder="Filter by message" />
      <ul>
        {filteredSyslogs.map((syslog, index) => (
          <li key={index}>
            {syslog.message} ({syslog.timestamp})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SyslogViewer;