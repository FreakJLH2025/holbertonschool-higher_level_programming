#!/usr/bin/python3
"""
Simple API built using Flask.
"""

from flask import Flask, jsonify, request

app = Flask(_name_)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint."""
    return "OK"


@app.route("/data")
def get_data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return full object for a given username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if _name_ == "_main_":
    app.run()
