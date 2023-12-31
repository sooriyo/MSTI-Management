import flask
from flask import request, send_file
from app import app
from models.admin_model import admin_model
import os
from datetime import datetime
obj = admin_model()

@app.route("/admin/all")

def all_admin():
    return obj.all_admin_model()

@app.route("/admin/add",methods=['POST'])
def add_admin(): 
  return obj.add_admin_model(request.form)

@app.route("/admin/delete/<id>",methods=['DELETE'])
def delete_admin(id):
    return obj.delete_admin_model(id)

@app.route("/admin/update",methods=['PUT'])
def update_admin():
    
    return obj.update_admin_model(request.form)

@app.route("/admin/update/st",methods=['PUT'])
def update_admin_satus():
    
    return obj.update_admin_status_model(request.form)

@app.route("/admin/getall/<int:id>", methods=['GET'])
def get_admin_by_id(id):
    return obj.search_admin_id_model(id)
