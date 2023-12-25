from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig


class user_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        print("Connected to DB")
        self.cur = self.con.cursor(dictionary=True)
        
    def all_user_model(self):
        self.cur.execute("SELECT * FROM tbl_users")
        result = self.cur.fetchall()
        if len(result)>0:
            #return {"payload":result}
            return make_response({"payload":result},200)
        else:
            return "No Data Found"
    
    def add_user_model(self,data):
        
       self.cur.execute(f"INSERT INTO tbl_users(name, nic, email, phone, address, userName, password, userType) VALUES ('{data['name']}', '{data['nic']}', '{data['email']}', '{data['phone']}', '{data['address']}', '{data['userName']}', '{data['password']}', '{data['userType']}')")

       return make_response({"message":"CREATED_SUCCESSFULLY"},201)
       

    def delete_user_model(self,id):
        self.cur.execute(f"DELETE FROM tbl_users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
        
    
    def update_user_model(self,data):
        self.cur.execute(f"UPDATE tbl_users SET name='{data['name']}',nic='{data['nic']}',email='{data['email']}',phone='{data['phone']}',address='{data['address']}',userName='{data['userName']}',password='{data['password']}',userType='{data['userType']}' WHERE id={data['id']}")
        
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)  
        
        
        
    def search_user_id_model(self, user_id):
        query = "SELECT name, nic, email, phone, address, userName, password, userType FROM tbl_users WHERE id=%s"
        self.cur.execute(query, (user_id,))

        result = self.cur.fetchall()  

        if len(result) > 0:
            return make_response({"message": "SEARCH_SUCCESSFULLY", "data": result}, 200)
        else:
            return make_response({"message": "USER_NOT_FOUND"}, 404)


        
        
    def update_user_status_model(self,data):
            self.cur.execute(f"UPDATE tbl_users SET status='{data['status']}',userType='{data['userType']}' WHERE id={data['id']}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
            else:
                return make_response({"message":"NOTHING_TO_UPDATE"},204)  
            
            
    def login_user_model(self, data):
        self.cur.execute(f"SELECT * FROM tbl_users WHERE userName='{data['userName']}' AND password='{data['password']}'")
        result = self.cur.fetchall()
        
        # return result

        if len(result)>0:
            payload = {
                'id': result[0]['id'],
                'userName': result[0]['userName'],
                'userType': result[0]['userType'],
                'exp': datetime.utcnow() + timedelta(minutes=60),
                'iat': datetime.utcnow()
            }
            token = jwt.encode(payload, 'mstiAuthCon', algorithm='HS256')
            return make_response({"token":token,"Date Time":datetime.utcnow(),"message":"LOGIN_SUCCESSFULLY",},200)
        else:
            return make_response({"message":"INVALID_CREDENTIALS"},404)
        