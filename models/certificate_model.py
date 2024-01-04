from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig


class certificate_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def get_certificate(self):
        self.cur.execute(f"SELECT * FROM tbl_certificate")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_certificate_by_id(self, id):
        self.cur.execute(f"SELECT * FROM tbl_certificate WHERE id={id}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def add_certificate(self, data):
        self.cur.execute(f"INSERT INTO tbl_certificate (certId , issuDate, expDate, studentId) VALUES ('{data['certId']}', '{data['issuDate']}', '{data['expDate']}', '{data['studentId']}')")
        return make_response({"message": "Certificate Added Successfully"}, 200)
    
    def update_certificate_by_id(self, data):
        self.cur.execute(f"UPDATE tbl_certificate SET certId='{data['certId']}', issuDate='{data['issuDate']}', expDate='{data['expDate']}', studentId='{data['studentId']}' WHERE id={data['id']}")
        return make_response({"message": "Certificate Updated Successfully"}, 200)
    
    def update_certificate_by_cert_id(self, data):
        self.cur.execute(f"UPDATE tbl_certificate SET issuDate='{data['issuDate']}', expDate='{data['expDate']}', studentId='{data['studentId']}' WHERE certId='{data['certId']}'")
        return make_response({"message": "Certificate Updated Successfully"}, 200)
    
    def delete_certificate(self, id):
        self.cur.execute(f"DELETE FROM tbl_certificate WHERE id={id}")
        return make_response({"message": "Certificate Deleted Successfully"}, 200)
    
    def get_certificate_by_cert_id(self, certId):
        self.cur.execute(f"SELECT * FROM tbl_certificate WHERE certId='{certId}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_certificate_by_std_id(self, studentId):
        self.cur.execute(f"SELECT * FROM tbl_certificate WHERE studentId='{studentId}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_certificate_by_exp_date(self, expDate):
        self.cur.execute(f"SELECT * FROM tbl_certificate WHERE expDate='{expDate}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    
    
    
    
    
        