import { useEffect, useState } from "react";

function App() {
  const [health, setHealth] = useState(null);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/health")
      .then((response) => response.json())
      .then((data) => setHealth(data));

    fetch("http://localhost:5000/api/users")
      .then((response) => response.json())
      .then((data) => setUsers(data.users));
  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>DevSecOps Platform</h1>

      <h2>Backend Status</h2>

      {health ? (
        <p>
          {health.service}: <strong>{health.status}</strong>
        </p>
      ) : (
        <p>Checking backend...</p>
      )}

      <h2>Users</h2>

      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.id} - {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
