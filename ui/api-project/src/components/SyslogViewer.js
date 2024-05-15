import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import styles from './SyslogViewer.module.css';

const SyslogViewer = () => {
  const { search } = useLocation();
  const { user } = useAuth0();

  const [syslogs, setSyslogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSyslogs = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.get(`http://127.0.0.1:5000/api/syslog?`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });

      if (response.status !== 200) {
        console.log(response.data);
        throw new Error('Failed to fetch syslogs');
      }

      const data = await response.data.data;
      console.log(data);
      setSyslogs(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (user && search) {
      fetchSyslogs();
    }
  }, [user, search]);

  return (
    <div className={styles.syslogViewer}>
      <div className={styles.profileHeader}>
        <h2>{user && user.name}</h2>
        <p className="lead text-muted">Profil {user && user.nickname}</p>
        <h2>Syslog Viewer</h2>
      </div>
      <div className="row">
        <div className="col-12 text-center">
          <button type="button" className={`${styles.btn} ${styles.btnPrimary} mb-3`} onClick={fetchSyslogs}>
            Sys log
          </button>
          <button type="button" className={`${styles.btn} ${styles.btnPrimary} mb-3`} onClick={() => { window.location.href = '/user-management'; }}>
            Admin User management
          </button>
          {loading && <p>Loading...</p>}
          {error && <p className={`${styles.textDanger} text-danger`}>{error}</p>}
          {syslogs.length > 0 && (
            <table className={`table table-striped table-hover ${styles.table}`}>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Severity</th>
                  <th>Hostname</th>
                  <th>App Name</th>
                  <th>Proc ID</th>
                  <th>Msg ID</th>
                  <th>Timestamp</th>
                  <th>Message</th>
                </tr>
              </thead>
              <tbody>
                {syslogs.map((syslog) => (
                  <tr key={syslog.id}>
                    <td>{syslog.id}</td>
                    <td>{syslog.severity}</td>
                    <td>{syslog.hostname}</td>
                    <td>{syslog.app_name}</td>
                    <td>{syslog.proc_id}</td>
                    <td>{syslog.msg_id}</td>
                    <td>{syslog.timestamp}</td>
                    <td>{syslog.msg}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
};

export default SyslogViewer;
