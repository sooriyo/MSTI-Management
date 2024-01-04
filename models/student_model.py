from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify, request
import jwt
from configs.config import dbconfig


class student_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def get_student(self):
        self.cur.execute(f"SELECT * FROM tbl_student")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_student_by_id(self, id):
        self.cur.execute(f"SELECT * FROM tbl_student WHERE id={id}")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    def get_student_by_std_id(self, studentId):
        self.cur.execute(f"SELECT * FROM tbl_student WHERE studentId = '{studentId}'")
        result = self.cur.fetchall()
        return make_response({"data": result}, 200)
    
    
    def add_std(self, data):
        self.cur.execute(f"INSERT INTO tbl_student (studentId, fullName, nameWithIni, permentAddress, mobileNumber, nic, passportNumber, gender, country, email, mainCourse, studentImg, courseId) VALUES ('{data['studentId']}', '{data['fullName']}', '{data['nameWithIni']}', '{data['permentAddress']}', '{data['mobileNumber']}', '{data['nic']}', '{data['passportNumber']}', '{data['gender']}', '{data['country']}', '{data['email']}', '{data['mainCourse']}', '{data['studentImg']}', '{data['courseId']}')")
        return make_response({"message": "Student Added Successfully"}, 200)

    
    def update_std_by_id(self, data):
        self.cur.execute(f"UPDATE tbl_student SET  studentId = '{data['studentId']}', fullName = '{data['fullName']}', nameWithIni = '{data['nameWithIni']}', permentAddress = '{data['permentAddress']}', mobileNumber = '{data['mobileNumber']}', nic = '{data['nic']}', passportNumber = '{data['passportNumber']}', gender = '{data['gender']}', country = '{data['country']}', email = '{data['email']}', mainCourse = '{data['mainCourse']}', studentImg = '{data['studentImg']}', courseId = '{data['courseId']}' WHERE id = '{data['id']}'")
        return make_response({"message": "Student Updated Successfully"}, 200)
    
    
    def update_std_by_std_id(self, data):
        self.cur.execute(f"UPDATE tbl_student SET fullName = '{data['fullName']}', nameWithIni = '{data['nameWithIni']}', permentAddress = '{data['permentAddress']}', mobileNumber = '{data['mobileNumber']}', nic = '{data['nic']}', passportNumber = '{data['passportNumber']}', gender = '{data['gender']}', country = '{data['country']}', email = '{data['email']}', mainCourse = '{data['mainCourse']}', studentImg = '{data['studentImg']}', courseId = '{data['courseId']}' WHERE studentId = '{data['studentId']}'")
        return make_response({"message": "Student Updated Successfully"}, 200)
    
    def delete_std(self, id):
        self.cur.execute(f"DELETE FROM tbl_student WHERE id={id}")
        return make_response({"message": "Student Deleted Successfully"}, 200)