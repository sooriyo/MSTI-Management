import flask
from flask import request, send_file
from app import app
from models.cdc_model import cdc_model
obj = cdc_model()


@app.route("/cdc/all")
def all_cdc():
    return obj.get_cdc()

@app.route("/cdc/add",methods=['POST'])
def add_cdc(): 
  return obj.add_cdc(request.form)

@app.route("/cdc/delete/<id>",methods=['DELETE'])
def delete_cdc(id):
    return obj.delete_cdc(id)

@app.route("/cdc/update",methods=['PUT'])
def update_cdc():
    return obj.update_cdc(request.form)

@app.route("/cdc/getall/<int:id>", methods=['GET'])
def get_cdc_by_id(id):
    return obj.get_cdc_by_id(id)

@app.route("/cdc/getall/<string:cdcId>", methods=['GET'])
def get_cdc_by_cdcId(cdcId):
    return obj.get_cdc_by_cdcId(cdcId)

@app.route("/cdc/getall/<string:expDate>", methods=['GET'])
def get_cdc_by_expDate(expDate):
    return obj.get_cdc_by_expDate(expDate)

@app.route("/cdc/getall/<string:issuDate>", methods=['GET'])
def get_cdc_by_issuDate(issuDate):
    return obj.get_cdc_by_issuDate(issuDate)

@app.route("/cdc/getall/<string:studentId>", methods=['GET'])
def get_cdc_by_studentId(studentId):
    return obj.get_cdc_by_studentId(studentId)

@app.route("/cdc/updatebyid",methods=['PUT'])
def update_cdc_by_id():
    return obj.update_cdc_by_id(request.form)

