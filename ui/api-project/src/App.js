import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Login from './components/Login';
import Registration from './components/Registration';
import SyslogViewer from './components/SyslogViewer';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/register" component={Registration} />
        <Route path="/syslog" component={SyslogViewer} />
      </Switch>
    </Router>
  );
}

export default App;