# 🚀 Scalable Task Management API (Full Stack)

A full-stack Task Management System built with **FastAPI (Python)** and **React**, implementing secure authentication, role-based access control, and scalable backend architecture.

This project was developed as part of a backend internship assignment to demonstrate real-world backend engineering skills including API design, security, and system scalability.

---

# 📌 Features

## 🔐 Authentication & Security

* User Registration & Login
* Password hashing using bcrypt
* JWT-based authentication
* Secure token handling
* Input validation using Pydantic

## 👥 Role-Based Access Control

* Two roles: **User** and **Admin**
* Admin can access all tasks
* Users can only access their own tasks

## 📊 Task Management (CRUD)

* Create, Read, Update, Delete tasks
* Task status toggle (Pending / Completed)
* Ownership-based access control

## ⚙️ Backend Engineering

* RESTful API design (`/api/v1/...`)
* Modular project structure
* SQLAlchemy ORM for database
* Centralized error handling
* Environment-based configuration

## 🌐 Frontend Integration

* React-based UI
* JWT authentication flow
* Protected dashboard
* API integration using Axios

## 📄 API Documentation

* Auto-generated Swagger docs:

  ```
  http://127.0.0.1:8000/docs
  ```

---

# 🏗️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite (can be switched to PostgreSQL)
* JWT (python-jose)
* Passlib (bcrypt)

### Frontend

* React (Vite)
* Axios
* CSS (custom styling)

---

# 📂 Project Structure

```
backend/
│── app/
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py

frontend/
│── src/
│   ├── pages/
│   ├── components/
│   ├── api/
```

---

# ⚙️ Step-by-Step Setup Guide

## 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd project
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🔐 Authentication Flow

1. User registers via `/auth/register`
2. User logs in via `/auth/login`
3. Server returns JWT token
4. Token stored in localStorage
5. Token sent in headers:

   ```
   Authorization: Bearer <token>
   ```

---

# 📊 API Endpoints

## Auth

* `POST /api/v1/auth/register`
* `POST /api/v1/auth/login`

## Tasks

* `GET /api/v1/tasks`
* `POST /api/v1/tasks`
* `PUT /api/v1/tasks/{id}`
* `DELETE /api/v1/tasks/{id}`

---

# 🔐 Security Practices

* Password hashing using bcrypt
* JWT token expiration
* Protected routes via middleware
* Input validation (Pydantic)
* Role-based authorization

---

# ⚡ Scalability Considerations

This project is designed to scale with the following improvements:

* 🔹 Microservices architecture (Auth Service, Task Service)
* 🔹 Redis caching for frequent queries
* 🔹 Load balancing using Nginx
* 🔹 Database scaling via replication/sharding
* 🔹 Docker containerization for deployment

---

# 🧪 Testing the API

Use:

* Swagger UI (recommended)
* Postman collection (can be added)

---

# 💡 Future Improvements

* Add refresh tokens
* Implement rate limiting
* Add logging system
* Integrate Redis caching
* Deploy using Docker + CI/CD

---

# 👨‍💻 Author

**Varun Kumar**

---

# ⭐ Final Note

This project focuses on writing **clean, scalable, and secure backend code** rather than just completing features.
The goal was to simulate a real-world backend system that can be extended into production-level architecture.

---
