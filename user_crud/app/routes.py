from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import User

@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return render_template("home.html", data=out)


@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success"
    }
# out ["body"] = User.query.all()
    users = User.query.all()
    out["body"] = []
    for user in users:
        user_dict = {}
        user_dict["id"] = user.id
        user_dict["first_name"] = user.first_name
        user_dict["last_name"] = user.last_name
        user_dict["hobbies"] = user.hobbies
        user_dict["active"] = user.active
        out["body"].append(user_dict)


    return render_template("user_list.html", data=out)

@app.route("/users/<int:pk>")
def get_single_user(pk):
    user = User.query.filter_by(id=pk).first()
    if user:
        return render_template("user_detail.html", user=user)
    return render_template("404.html"), 404

@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
#     out["user_id"] = insert(
#         user_data.get("first_name"),
#         user_data.get("last_name"),
#         user_data.get("hobbies")
#     )
    return out, 201

# @app.route("/greeting/<user_name>")
# def greet_user(user_name):
#     return render_template("home.html", name=user_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404