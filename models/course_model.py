from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig


class course_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def get_course(self):
        self.cur.execute(f"SELECT * FROM tbl_course")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)    
    
    def get_course_by_id(self, id):
        self.cur.execute(f"SELECT * FROM tbl_course WHERE id={id}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def add_course(self, data):
        self.cur.execute(f"INSERT INTO tbl_course (courseId, courseName, courseType, courseDuration, courseFee) VALUES ('{data['courseId']}', '{data['courseName']}', '{data['courseType']}', '{data['courseDuration']}', '{data['courseFee']}')")
        return make_response({"message": "Course Added Successfully"}, 200)
    
    def update_course(self, data):
        self.cur.execute(f"UPDATE tbl_course SET courseId='{data['courseId']}', courseName='{data['courseName']}', courseType='{data['courseType']}', courseDuration='{data['courseDuration']}', courseFee='{data['courseFee']}' WHERE id={data['id']}")
        return make_response({"message": "Course Updated Successfully"}, 200)
    
    def delete_course(self, id):
        self.cur.execute(f"DELETE FROM tbl_course WHERE id={id}")
        return make_response({"message": "Course Deleted Successfully"}, 200)
    
    def get_course_by_courseId(self, courseId):
        self.cur.execute(f"SELECT * FROM tbl_course WHERE courseId='{courseId}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_course_by_courseType(self, courseType):
        self.cur.execute(f"SELECT * FROM tbl_course WHERE courseType='{courseType}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200) 
    
        
   
            