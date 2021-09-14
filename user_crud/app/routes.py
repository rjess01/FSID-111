from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 

from app.database import scan, read

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success",
    }
    out ["body"] = scan()
    return out


@app.route("/users/<int:pk>")
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    out["body"] = read(pk)
    return out


@app.route("/users", method=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return out, 201

@app.route("/users", method=["PUT"])
def update_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = insert(
        user_data.put("first_name"),
        user_data.put("last_name"),
        user_data.put("hobbies")
    )
    return out, 201





