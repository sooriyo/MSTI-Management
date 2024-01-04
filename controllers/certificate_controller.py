import flask
from flask import jsonify, request, send_file
from app import app
from models.certificate_model import certificate_model
obj = certificate_model()

@app.route("/cert/add",methods=['POST'])
def add_certificate(): 
  return obj.add_certificate(request.form)

@app.route("/cert/get", methods=['GET'])
def get_certificate():
    return obj.get_certificate()

@app.route("/cert/get/<int:id>", methods=['GET'])
def get_certificate_by_id(id):
    return obj.get_certificate_by_id(id)

@app.route("/cert/update",methods=['PUT'])
def update_certificate_by_id():
    return obj.update_certificate_by_id(request.form)

@app.route("/cert/delete/<int:id>",methods=['DELETE'])
def delete_certificate(id):
    return obj.delete_certificate(id)

@app.route("/cert/get/cert/<string:certId>", methods=['GET'])
def get_certificate_by_cert_id(certId):
    return obj.get_certificate_by_cert_id(certId)

@app.route("/cert/get/std/<string:studentId>", methods=['GET'])
def get_certificate_by_std_id(studentId):
    return obj.get_certificate_by_std_id(studentId)

@app.route("/cert/get/exp/<string:expDate>", methods=['GET'])
def get_certificate_by_exp_date(expDate):
    return obj.get_certificate_by_exp_date(expDate)

@app.route("/cert/update/cert",methods=['PUT'])
def update_certificate_by_cert_id():
    return obj.update_certificate_by_cert_id(request.form)