
import React, { useState } from "react";

const UserCreate = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = { email, password, role };

    try {
      const res = await fetch("http://localhost:8000/auth/create_user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        alert("Failed to create user");
        return;
      }

      alert("User created successfully!");
    } catch (err) {
      console.error(err);
      alert("Network error");
    }
  };

  return (
    <div style={styles.container}>
      <form style={styles.form} onSubmit={handleSubmit}>
        <h2 style={styles.title}>Create User</h2>

        <div style={styles.field}>
          <label style={styles.label}>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={styles.input}
            placeholder="Enter email"
            required
          />
        </div>

        <div style={styles.field}>
          <label style={styles.label}>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={styles.input}
            placeholder="Enter password"
            required
          />
        </div>

        <div style={styles.field}>
          <label style={styles.label}>Role</label>
          <select
            value={role}
            onChange={(e) => setRole(e.target.value)}
            style={styles.select}
            required
          >
            <option value="">Select role</option>
            <option value="patient">patient</option>
            <option value="doctor">doctor</option>
            <option value="pharmacy">pharmacy</option>
            <option value="insurance">insurance</option>
            <option value="admin">admin</option>
          </select>
        </div>

        <button type="submit" style={styles.button}>
          Create User
        </button>
      </form>
    </div>
  );
};

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f4f6f8",
  },
  form: {
    width: "350px",
    padding: "25px",
    borderRadius: "10px",
    background: "#fff",
    boxShadow: "0 8px 20px rgba(0,0,0,0.1)",
  },
  title: {
    textAlign: "center",
    marginBottom: "20px",
    color: "#333",
  },
  field: {
    marginBottom: "15px",
  },
  label: {
    display: "block",
    marginBottom: "5px",
    fontWeight: "600",
    color: "#555",
  },
  input: {
    width: "100%",
    padding: "10px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    outline: "none",
  },
  select: {
    width: "100%",
    padding: "10px",
    borderRadius: "6px",
    border: "1px solid #ccc",
  },
  button: {
    width: "100%",
    padding: "12px",
    border: "none",
    borderRadius: "6px",
    background: "#007bff",
    color: "#fff",
    fontSize: "16px",
    fontWeight: "bold",
    cursor: "pointer",
  },
};

export default UserCreate;





