import flask
from flask import request, send_file
from app import app
from models.user_model import user_model
import os
from datetime import datetime
obj = user_model()



@app.route("/user/all")

def all_users():
    return obj.all_user_model()

@app.route("/user/add",methods=['POST'])
def add_user(): 
  return obj.add_user_model(request.form)

@app.route("/user/delete/<id>",methods=['DELETE'])
def delete_user(id):
    return obj.delete_user_model(id)

@app.route("/user/update",methods=['PUT'])
def update_user():
    
    return obj.update_user_model(request.form)

@app.route("/user/update/st",methods=['PUT'])
def update_user_satus():
    
    return obj.update_user_status_model(request.form)

@app.route("/user/getall/<int:id>", methods=['GET'])
def get_user_by_id(id):
    return obj.search_user_id_model(id)

@app.route("/user/login", methods=['GET'])
def login_user():
    return obj.login_user_model(request.form)






