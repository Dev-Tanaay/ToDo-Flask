# ToDo Flask App

A robust REST API for managing tasks, built with Flask, SQLAlchemy, and JWT Authentication.

## Features

- User Authentication (Signup/Login)
- JWT Token-based Authorization
- Create, Read, Update, Delete (CRUD) Todos
- Toggle Todo Completion Status
- SQLite/PostgreSQL support (via SQLAlchemy)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Dev-Tanaay/ToDo-Flask.git
cd ToDo-Flask
```

### 2. Set up Virtual Environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_super_secret_key_here
DATABASE_URL=sqlite:///todo.db
```
(Or use your PostgreSQL URL for `DATABASE_URL`)

### 5. Initialize Database

Run the migrations to create the database tables:

```bash
flask db upgrade
```

### 6. Run the Application

```bash
flask run
```
The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Authentication
- `POST /api/user/signup`: Create a new user account.
- `POST /api/user/login`: Login and receive a JWT token.

### Todos (Requires `Authorization: Bearer <token>`)
- `GET /api/todo/`: Fetch all todos for the logged-in user.
- `POST /api/todo/create`: Create a new todo.
- `GET /api/todo/<id>`: Get details of a specific todo.
- `PUT /api/todo/<id>`: Toggle completion status of a todo.
- `POST /api/todo/update/<id>`: Update title/description of a todo.
- `DELETE /api/todo/<id>`: Delete a todo.

