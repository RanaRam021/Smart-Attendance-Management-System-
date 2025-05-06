from flask import Flask, request, jsonify, render_template , Response # type: ignore
import firebase_admin
from firebase_admin import credentials, db
import csv
from io import  StringIO 
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv() 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("DB_URL")
})


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def check_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if check_admin(username, password):
        return render_template('admin.html')
    else:
        return "Invalid credentials. Please try again."

@app.route('/get_attendance', methods=['GET'])
def get_attendance():
    rollno = request.args.get('rollno')
    if not rollno:
        return jsonify({"error": "Please provide a roll number."})
    
    try:
        ref = db.reference(f"Students/{rollno}")
        student_data = ref.get()
        
        if student_data:
            return jsonify(student_data)
        else:
            return jsonify({"error": "Roll number not found in database."})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/download')
def download():
    
    students_data = db.reference('Students').get()
    common_data = db.reference('commoninfo').get()

    
    csv_data = [["Name", "Roll No", "Weekly Total Percentage","Weekly Total Attendace", "Weekly Total Classes", "Cumulative Total Percentage",  "Cumulative Total Attendance" ,   "Cumulative Total Classes"]]
    for student_id, student_info in students_data.items():
        name = student_info.get('name', '')
        roll_no = student_info.get('roll_no', '')
        weekly_percentage = student_info.get('weekly_total_percentage', '')
        weekly_attendance = student_info.get('weekly_total_attendance', '')
        weekly_classes = common_data.get('weekly_total_classes', '')
        cumulative_percentage = student_info.get('cumulative_total_percentage', '')
        cumulative_attendance = student_info.get('cumulative_total_attendance', '')
        cumulative_classes = common_data.get('cumulative_total_classes', '')
        csv_data.append([name, roll_no, weekly_percentage,weekly_attendance, weekly_classes, cumulative_percentage , cumulative_attendance, cumulative_classes])
    
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(csv_data)
    
   
    response = Response(output.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=students_attendance.csv'
    
    return response




if __name__ == '__main__':
    app.run(debug=True)
