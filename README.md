# Job Application Tracker

A full stack web application to track campus placement applications
— companies applied to, interview rounds, and outcomes 
— built with a Flask REST API backend and a vanilla JS frontend.

## Live Demo
- Frontend: https://storied-heliotrope-bc8014.netlify.app
- Backend API: https://job-application-tracker-ucek.onrender.com

Note: Backend is hosted on Render's free tier, so the first request after a period of inactivity may take 20-30 seconds to respond while the server wakes up.

## Project Structure

This is a monorepo containing two independently deployable parts:
    job-application-tracker/
    ├── job_tracker_backend/    Flask REST API (see its own README)
    └── job_tracker_frontend/   HTML/CSS/JS client (see its own README)

## Features
- User registration and login with hashed passwords
- JWT based authentication on every protected route
- Role based access control — students see only their own applications, admins can view all
- Add, update, and delete job applications
- Filter applications by status
- Status tracked through stages: Applied, Interview, Rejected, Selected

## Tech Stack
- Backend: Python, Flask, SQLite, Flask-JWT-Extended
- Frontend: HTML, CSS, JavaScript (vanilla, no framework)
- Deployment: Render (backend), Netlify (frontend)

## Why I built this

I wanted a project that went beyond basic CRUD — something that forced me to actually integrate authentication, a relational database, and a frontend talking to a real API, instead of learning each concept in isolation. This project is also genuinely something I use to track my own placement applications.

## Running Locally

See the README inside each subfolder (`job_tracker_backend` and `job_tracker_frontend`) for setup instructions specific to each part.