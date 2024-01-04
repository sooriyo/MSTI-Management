import flask
from flask import jsonify, request, send_file
from app import app
from models.student_model import student_model
obj = student_model()


@app.route("/std/add",methods=['POST'])
def add_studen(): 
  return obj.add_std(request.form)


@app.route("/std/get", methods=['GET'])
def get_student():
    return obj.get_student()

@app.route("/std/get/<int:id>", methods=['GET'])
def get_student_by_id(id):
    return obj.get_student_by_id(id)

@app.route("/std/get/std/<string:studentId>", methods=['GET'])
def get_student_by_std_id(studentId):
    return obj.get_student_by_std_id(studentId)

@app.route("/std/update",methods=['PUT'])
def update_std_by_id():
    return obj.update_std_by_id(request.form)

@app.route("/std/update/<int:studentId>",methods=['PUT'])
def update_std_by_std_id(studentId):
    return obj.update_std_by_std_id(request.form)

@app.route("/std/delete/<int:id>",methods=['DELETE'])
def delete_std(id):
    return obj.delete_std(id)

