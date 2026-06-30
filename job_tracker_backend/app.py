from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from db import init_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

jwt = JWTManager(app)

from flask import jsonify

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired. Please login again."}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token. Please login again."}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Authorization token missing."}), 401

from routes.auth import auth_bp
from routes.application import applications_bp

app.register_blueprint(auth_bp)
app.register_blueprint(applications_bp)

import os

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)