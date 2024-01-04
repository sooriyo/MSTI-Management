import flask
from flask import request, send_file
from app import app
from models.user_model import user_model
obj = user_model()


@app.route("/user/login", methods=['GET'])
def login_user():
    return obj.login(request.form)






