from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig


class cdc_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def get_cdc(self):
        self.cur.execute(f"SELECT * FROM tbl_cdc")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200) 
    
    def get_cdc_by_id(self, id):
        self.cur.execute(f"SELECT * FROM tbl_cdc WHERE id = {id}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_cdc_by_cdcId(self, cdcId):
        self.cur.execute(f"SELECT * FROM tbl_cdc WHERE cdcId = {cdcId}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def add_cdc(self, data):
        self.cur.execute(f"INSERT INTO tbl_cdc (cdcId, expDate, issuDate, studentId) VALUES ('{data['cdcId']}', '{data['expDate']}', '{data['issuDate']}', '{data['studentId']}')")
        return make_response({"message": "CDC added successfully"}, 200)
    
    def update_cdc(self, data):
        self.cur.execute(f"UPDATE tbl_cdc SET expDate='{data['expDate']}', issuDate='{data['issuDate']}', studentId='{data['studentId']}' WHERE cdcId='{data['courseId']}'")
        return make_response({"message": "CDC updated successfully"}, 200)
    
    def update_cdc_by_id(self, data):
        self.cur.execute(f"UPDATE tbl_cdc SET cdcId='{data['courseId']}', expDate='{data['expDate']}', issuDate='{data['issuDate']}', studentId='{data['studentId']}' WHERE id={data['id']}")
        return make_response({"message": "CDC updated successfully"}, 200)
    
    def delete_cdc(self, id):
        self.cur.execute(f"DELETE FROM tbl_cdc WHERE id={id}")
        return make_response({"message": "CDC deleted successfully"}, 200)
    
    def get_cdc_by_expDate(self, expDate):
        self.cur.execute(f"SELECT * FROM tbl_cdc WHERE expDate = {expDate}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_cdc_by_issuDate(self, issuDate):
        self.cur.execute(f"SELECT * FROM tbl_cdc WHERE issuDate = {issuDate}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_cdc_by_studentId(self, studentId):
        self.cur.execute(f"SELECT * FROM tbl_cdc WHERE studentId = {studentId}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)