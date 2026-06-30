# Job Application Tracker — Backend

A REST API built with Flask and SQLite for the Job Application Tracker.

## Tech Stack
- Python, Flask
- SQLite
- Flask-JWT-Extended (authentication)
- python-dotenv (environment variables)

## Features
- User registration and login with SHA256 hashed passwords
- JWT based authentication on protected routes
- Role based access (student / admin)
- Relational schema — applications linked to users via foreign key
- Filter applications by status using query parameters
- Clean error responses for missing, invalid, or expired tokens

## Project Structure
job_tracker_backend/
├── app.py               Flask app entry point, blueprint registration<br>
├── config.py            Loads environment variables<br>
├── db.py                Database connection and table creation<br>
├── models/<br>
│   ├── user.py<br>
│   └── application.py<br>
├── routes/<br>
│   ├── auth.py           /register, /login<br>
│   └── applications.py   CRUD + filter routes for applications<br>
├── requirements.txt<br>
└── Procfile              Start command for deployment

## API Endpoints

| Method | Endpoint | Auth required | Description |
|--------|----------|----------------|-------------|
| POST | /register | No | Create a new user |
| POST | /login | No | Authenticate, returns JWT token |
| POST | /applications | Yes | Add a new application |
| GET | /applications | Yes | Get applications (own, or all if admin) |
| PUT | /applications/<id> | Yes | Update status/notes of an application |
| DELETE | /applications/<id> | Yes | Delete an application |
| GET | /applications/filter?status= | Yes | Filter applications by status |

Protected routes require the header:
`Authorization: Bearer <token>`

## Setup — Run Locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

Create a `.env` file in this folder:
    JWT_SECRET_KEY=your_secret_key_here
    DATABASE=job_tracker.db

    Run the server:
```bash
python app.py
```

Server runs at `http://127.0.0.1:5000`

## Testing

Tested using Postman. Example register request:

```json
POST /register
{
    "name": "John",
    "email": "john@gmail.com",
    "password": "yourpassword",
    "role": "student"
}
```

## Possible Improvements
- Replace SHA256 with bcrypt for password hashing
- Add refresh tokens so users aren't logged out frequently
- Add pagination for large datasets
- Move from Flask's development server to a production WSGI server