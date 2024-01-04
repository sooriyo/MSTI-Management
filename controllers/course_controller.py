import flask
from flask import request, send_file
from app import app
from models.course_model import course_model
obj = course_model()

@app.route("/crs/all")
def all_course():
    return obj.get_course()

@app.route("/crs/add",methods=['POST'])
def add_course(): 
  return obj.add_course(request.form)

@app.route("/crs/delete/<id>",methods=['DELETE'])
def delete_course(id):
    return obj.delete_course(id)

@app.route("/crs/update",methods=['PUT'])
def update_course():
    return obj.update_course(request.form)

@app.route("/crs/getall/<int:id>", methods=['GET'])
def get_course_by_id(id):
    return obj.get_course_by_id(id)

@app.route("/crs/getall/<string:courseId>", methods=['GET'])
def get_course_by_courseId(courseId):
    return obj.get_course_by_courseId(courseId)

@app.route("/crs/getall/<string:courseType>", methods=['GET'])
def get_course_by_courseType(courseType):
    return obj.get_course_by_courseType(courseType)






