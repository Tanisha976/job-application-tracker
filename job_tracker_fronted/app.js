const API_URL = "http://127.0.0.1:5000";
let token = "";

let isRegisterMode = false;

function toggleAuthMode(e) {
    e.preventDefault();
    isRegisterMode = !isRegisterMode;

    document.getElementById("auth-title").innerText = isRegisterMode ? "Register" : "Login";
    document.getElementById("register-fields").style.display = isRegisterMode ? "block" : "none";
    document.getElementById("auth-submit-btn").innerText = isRegisterMode ? "Register" : "Login";
    document.getElementById("auth-submit-btn").onclick = isRegisterMode ? register : login;
    document.getElementById("toggle-text").innerText = isRegisterMode ? "Already have an account?" : "Don't have an account?";
    document.getElementById("toggle-link").innerText = isRegisterMode ? "Login" : "Register";
    document.getElementById("login-error").innerText = "";
}

async function register() {
    const name = document.getElementById("reg-name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!name || !email || !password) {
        document.getElementById("login-error").innerText = "All fields are required";
        return;
    }

    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password, role: "student" })
    });

    const data = await response.json();

    if (response.ok) {
        document.getElementById("login-error").style.color = "var(--selected)";
        document.getElementById("login-error").innerText = "Registered! Please login now.";
        toggleAuthMode({ preventDefault: () => {} });
    } else {
        document.getElementById("login-error").style.color = "var(--rejected)";
        document.getElementById("login-error").innerText = data.error;
    }
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok) {
        token = data.token;
        document.getElementById("login-section").style.display = "none";
        document.getElementById("dashboard").style.display = "block";
        loadApplications();
    } else {
        document.getElementById("login-error").style.color = "var(--rejected)";
        document.getElementById("login-error").innerText = data.error;
    }
}

function logout() {
    token = "";
    document.getElementById("dashboard").style.display = "none";
    document.getElementById("login-section").style.display = "block";
}

async function loadApplications() {
    const response = await fetch(`${API_URL}/applications`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const applications = await response.json();
    const tbody = document.getElementById("applications-body");
    tbody.innerHTML = "";

    applications.forEach(app => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${app.company}</td>
            <td>${app.role}</td>
            <td>${app.status}</td>
            <td>${app.notes || ""}</td>
            <td>
                <button onclick="updateStatus(${app.id}, '${app.status}', '${(app.notes || '').replace(/'/g, "\\'")}')">Update</button>
                <button onclick="deleteApplication(${app.id})">Delete</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

async function addApplication() {
    const company = document.getElementById("company").value;
    const role = document.getElementById("role").value;
    const notes = document.getElementById("notes").value;

    await fetch(`${API_URL}/applications`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ company, role, notes })
    });

    document.getElementById("company").value = "";
    document.getElementById("role").value = "";
    document.getElementById("notes").value = "";

    loadApplications();
}

async function updateStatus(id, currentStatus, currentNotes) {
    const newStatus = prompt("Status (Applied/Interview/Rejected/Selected):", currentStatus);
    if (!newStatus) return;

    const newNotes = prompt("Notes:", currentNotes || "");

    await fetch(`${API_URL}/applications/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ status: newStatus, notes: newNotes })
    });

    loadApplications();
}

async function deleteApplication(id) {
    await fetch(`${API_URL}/applications/${id}`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${token}` }
    });

    loadApplications();
}