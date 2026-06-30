# Job Application Tracker API
A REST API built with Flask and SQLite to track campus placement applications.

## Tech Stack
- Python, Flask
- SQLite
- JWT Authentication
- python-dotenv

## Features
- User registration and login with hashed passwords
- JWT based authentication
- Role based access control (student/admin)
- Add, update, delete job applications
- Filter applications by status
- Admin can view all applications

## API Endpoints

| Method | Endpoint                     | Description             |
|--------|------------------------------|-------------------------|
| POST   | /register                    | Register new user       |
| POST   | /login                       | Login and get JWT token |
| POST   | /applications                | Add application         |
| GET    | /applications                | View own applications   |
| PUT    | /applications/<id>           | Update status           |
| DELETE | /applications/<id>           | Delete application      |
| GET    | /applications/filter?status= | Filter by status        |

## Setup
pip install -r requirements.txt
python app.py

## Testing
Use Postman to test all endpoints.
Add this header to protected routes:
    Authorization: Bearer your_token_here