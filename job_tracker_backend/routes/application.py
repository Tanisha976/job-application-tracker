from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from db import get_connection
from datetime import date

applications_bp = Blueprint("applications", __name__)

@applications_bp.route("/applications", methods=["POST"])
@jwt_required()
def add_application():
    user_id = get_jwt_identity()
    data = request.get_json()

    company = data.get("company")
    role = data.get("role")
    notes = data.get("notes", "")

    if not company or not role:
        return jsonify({"error": "Company and role are required"}), 400

    conn = get_connection()
    conn.execute(
        "INSERT INTO applications (user_id, company, role, status, date_applied, notes) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, company, role, "Applied", str(date.today()), notes)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Application added successfully"}), 201


@applications_bp.route("/applications", methods=["GET"])
@jwt_required()
def get_applications():
    user_id = get_jwt_identity()
    claims = get_jwt()
    role = claims.get("role")

    conn = get_connection()

    if role == "admin":
        applications = conn.execute(
            "SELECT a.*, u.name, u.email FROM applications a JOIN users u ON a.user_id = u.id"
        ).fetchall()
    else:
        applications = conn.execute(
            "SELECT * FROM applications WHERE user_id = ?",
            (user_id,)
        ).fetchall()

    conn.close()

    return jsonify([dict(a) for a in applications]), 200


@applications_bp.route("/applications/<int:app_id>", methods=["PUT"])
@jwt_required()
def update_application(app_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    status = data.get("status")
    notes = data.get("notes")

    if not status:
        return jsonify({"error": "Status is required"}), 400

    conn = get_connection()

    application = conn.execute(
        "SELECT * FROM applications WHERE id = ? AND user_id = ?",
        (app_id, user_id)
    ).fetchone()

    if not application:
        return jsonify({"error": "Application not found or unauthorized"}), 404

    conn.execute(
        "UPDATE applications SET status = ?, notes = ? WHERE id = ?",
        (status, notes, app_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Application updated"}), 200


@applications_bp.route("/applications/<int:app_id>", methods=["DELETE"])
@jwt_required()
def delete_application(app_id):
    user_id = get_jwt_identity()

    conn = get_connection()

    application = conn.execute(
        "SELECT * FROM applications WHERE id = ? AND user_id = ?",
        (app_id, user_id)
    ).fetchone()

    if not application:
        return jsonify({"error": "Application not found or unauthorized"}), 404

    conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Application deleted"}), 200

@applications_bp.route("/applications/filter", methods=["GET"])
@jwt_required()
def filter_applications():
    user_id = get_jwt_identity()
    status = request.args.get("status")

    if not status:
        return jsonify({"error": "Status parameter required"}), 400

    conn = get_connection()
    applications = conn.execute(
        "SELECT * FROM applications WHERE user_id = ? AND status = ?",
        (user_id, status)
    ).fetchall()
    conn.close()

    return jsonify([dict(a) for a in applications]), 200