import { useEffect, useState } from "react";
import API from "../api/axios";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [form, setForm] = useState({ title: "", description: "" });

  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const createTask = async () => {
    await API.post("/tasks", form);
    setForm({ title: "", description: "" });
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await API.delete(`/tasks/${id}`);
    fetchTasks();
  };

  return (
    <div className="container">
      <h2>Dashboard</h2>

      <div>
        <input placeholder="Title" value={form.title}
          onChange={e => setForm({...form, title: e.target.value})}/>
        <input placeholder="Description" value={form.description}
          onChange={e => setForm({...form, description: e.target.value})}/>
        <button onClick={createTask}>Add Task</button>
      </div>

      <ul>
        {tasks.map(t => (
          <li key={t.id}>
            <b>{t.title}</b> - {t.description}
            <button onClick={() => deleteTask(t.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}