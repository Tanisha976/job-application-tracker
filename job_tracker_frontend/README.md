# Job Application Tracker — Frontend

A vanilla HTML, CSS, and JavaScript client for the Job Application
Tracker API. No framework, no build step — plain static files that
talk directly to the backend using fetch().

## Live Demo
https://storied-heliotrope-bc8014.netlify.app

## Tech Stack
- HTML
- CSS (custom, no framework)
- JavaScript (vanilla, fetch API)

## Features
- Combined login / register form with a single toggle
- Dashboard showing all applications in a table
- Add new applications through a form
- Update status and notes per application
- Delete applications
- JWT token stored in memory and attached to every authenticated request

## Project Structure
job_tracker_frontend/
├── index.html    Page structure — login/register form, dashboard
├── app.js        All API calls (fetch) and DOM logic
└── style.css     Custom styling

## Setup — Run Locally

This is a static site — no installation or build step needed.

1. Make sure the backend is running (locally or pointed at the live
   Render URL — check the `API_URL` constant at the top of `app.js`)
2. Open `index.html` directly in a browser, or serve it with a tool
   like VS Code's Live Server extension

## Connecting to a Different Backend

Change this line at the top of `app.js`:
```javascript
const API_URL = "https://job-application-tracker-ucek.onrender.com";
```
Replace with `http://127.0.0.1:5000` to point at a local backend instead.

## Possible Improvements
- Replace `prompt()` based status updates with a proper modal/form
- Add client side input validation before sending requests
- Add loading states while waiting on API responses