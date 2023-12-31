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
        # print("Connected to DB")
        self.cur = self.con.cursor(dictionary=True)
        
   
            
    
    def login(self, data):
        self.cur.execute(f"SELECT * FROM tbl_users WHERE userName='{data['userName']}' AND password='{data['password']}'")
        result = self.cur.fetchall()

        if len(result) == 1:
            userName = result[0]['userName']  
            userType = result[0]['userType']
            userId = result[0]['id']   

            exptime = datetime.now() + timedelta(minutes=15)
            exp_epoch_time = exptime.timestamp()

            token_payload = {
                "userName": userName,
                "userType": userType,
                "exp": int(exp_epoch_time)
            }

            jwt_token = jwt.encode(token_payload, "MSTI@Auth", algorithm="HS256")
            return make_response({"token": jwt_token,"AccessTime":datetime.now(),"UserName":userName,"UserType":userType}, 200)
        else:
            return make_response({"message": "NO SUCH USER"}, 204)        
    
        
        