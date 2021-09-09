#!/usr/bin/env python3

from flask import Flask                 #from the flask package import the flask class.

app = Flask(__name__)         #instantiate the Flask class with a parameter __name__ into "app". we're creating an instance of a class into a variable, which makes it an object. In object oriented programming, everything is a class. Classes are like a blueprint. And the result of that instantiating    Class: Object   (Blueprint: House)

@app.route("/")             #@app.route is a decorate that wraps the function underneath it.
def index():                #view function that is being wrapped.
    return "<h1>Hello, world!</h1>"


@app.route("/about")
def about_me():
    me = {
        "first_name": "Chris",
        "last_name": "Daming",
        "hobbies": "reading"
    }
    return me


