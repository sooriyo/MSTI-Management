from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig

class admin_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        print("Connected to DB")
        self.cur = self.con.cursor(dictionary=True)
        
    def all_admin_model(self):
        self.cur.execute("SELECT * FROM tbl_admin")
        result = self.cur.fetchall()
        if len(result)>0:
            #return {"payload":result}
            return make_response({"payload":result},200)
        else:
            return "No Data Found"
        
    def add_admin_model(self,data):
        
       self.cur.execute(f"INSERT INTO tbl_admin(staffId, password, name, email, adminLevel, mobileNumber) VALUES ('{data['staffId']}', '{data['password']}', '{data['name']}', '{data['email']}', '{data['adminLevel']}', '{data['mobileNumber']}')")

       return make_response({"message":"ADMIN_CREATED_SUCCESSFULLY"},201)
   
    def update_admin_model(self,data):
        self.cur.execute(f"UPDATE tbl_admin SET staffId='{data['staffId']}',password='{data['password']}',name='{data['name']}',email='{data['email']}',adminLevel='{data['adminLevel']}',mobileNumber='{data['mobileNumber']}'")
        
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)  
        
    def search_admin_id_model(self, user_id):
        query = "SELECT staffId, password, name, email, adminLevel, mobileNumber FROM tbl_admin WHERE id=%s"
        self.cur.execute(query, (user_id,))

        result = self.cur.fetchall()  

        if len(result) > 0:
            return make_response({"message": "SEARCH_SUCCESSFULLY", "data": result}, 200)
        else:
            return make_response({"message": "USER_NOT_FOUND"}, 404)
        
    def update_admin_status_model(self,data):
            self.cur.execute(f"UPDATE tbl_admin SET adminLevel='{data['adminLevel']}' WHERE id={data['id']}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
            else:
                return make_response({"message":"NOTHING_TO_UPDATE"},204)  
            
    def delete_admin_model(self,id):
        self.cur.execute(f"DELETE FROM tbl_admin WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
            

        
        