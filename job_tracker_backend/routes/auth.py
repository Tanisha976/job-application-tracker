from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from db import get_connection
import hashlib

auth_bp = Blueprint("auth", __name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role","student")

    if not name or not email or not password:
        return jsonify({"error" : "All fields required"}), 400
    
    hashed = hash_password(password)

    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO users (name,email,password,role) VALUES (?,?,?,?)",
            (name,email,hashed,role)
        )
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error":"email already exists"}), 409
    finally:
        conn.close()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    
    hashed = hash_password(password)

    conn = get_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email,hashed)
    ).fetchone()
    conn.close()

    if not user:
        return jsonify({"error" : "Invalid credentials"}), 401
    
    token = create_access_token(identity=str(user["id"]), additional_claims={"role": user["role"]})
    return jsonify({"token": token, "role": user["role"]}), 200