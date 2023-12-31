import flask
from flask import request, send_file
from app import app
from models.user_model import user_model
import os
from datetime import datetime
obj = user_model()


@app.route("/user/login", methods=['GET'])
def login_user():
    return obj.login(request.form)






