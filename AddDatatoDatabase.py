import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os

load_dotenv() 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':  os.getenv("DB_URL")
})

ref = db.reference('Students')



data = {
    "321654":
        {
            "name": "Rana Ram",
            "major": "CSE",
            "roll_no": 321654,
            "starting_year": 2021,
            "CGPA": "8.4",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:31:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage": 40,
            "cumulative_total_percentage": 40
          


        },
    "852741":
        {
            "name": "Suresh",
            "major": "CSE",
            "roll_no": 852741,
            "starting_year": 2021,
            "CGPA": "8",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "963852":
        {
            "name": "Priyanshu",
            "major": "CSE",
            "roll_no": 963852,
            "starting_year": 2021,
            "CGPA": "9",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "468426":
        {
            "name": "Pushkar",
            "major": "CSE",
            "roll_no": 468426,
            "starting_year": 2021,
            "CGPA": "9.9",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
           "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "568987":
        {
            "name": "Rudraksha",
            "major": "CSE",
            "roll_no": 568987,
            "starting_year": 2021,
            "CGPA": "7.6",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "458945":
        {
            "name": "Rishabh",
            "major": "CSE",
            "roll_no": 458945,
            "starting_year": 2021,
            "CGPA": "9",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "788744":
        {
            "name": "Rohan",
            "major": "CSE",
            "roll_no": 788744,
            "starting_year": 2021,
            "CGPA": "8.7",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "455123":
        {
            "name": "Rohit",
            "major": "CSE",
            "roll_no": 455123,
            "starting_year": 2021,
            "CGPA": "8.1",
            "year": 4,
            "last_attendance_time": "2024-12-02 14:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "659889":
        {
            "name": "Pratham",
            "major": "CSE",
            "roll_no": 659889,
            "starting_year": 2021,
            "CGPA": "8.3",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        },
    "856556":
        {
            "name": "Kunal",
            "major": "CSE",
            "roll_no": 856556,
            "starting_year": 2021,
            "CGPA": "7.7",
            "year": 4,
            "last_attendance_time": "2024-12-01 15:30:34",
            "cumulative_total_attendance": 7,
            "weekly_total_attendance": 7,
            "weekly_total_percentage":40,
            "cumulative_total_percentage":40
        }
    
}



for key, value in data.items():
    ref.child(key).set(value)


common_info_ref = db.reference('commoninfo')

common_info = {
    "cumulative_total_classes": 420,
    "weekly_total_classes": 35,
    "last_reset_date": "2024-12-01"
}

for key, value in common_info.items():
    common_info_ref.child(key).set(value)