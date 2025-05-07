# 📸 Smart Attendance Management System (Face Recognition Based)

A Python-based attendance management system that uses facial recognition to automatically mark attendance of students in real-time. It features a web interface for both students and admin, enabling live attendance viewing and CSV report downloads.

---

## 🎯 Project Aim

The goal of this project is to automate the traditional attendance system using AI, making it more secure, efficient, and user-friendly. This system eliminates proxy attendance and provides real-time access to attendance data.

---

## 🚀 Features

- Real-time face recognition for attendance marking.
- Automatically stores attendance in Firebase.
- Web interface using Flask for:
  - Students to view attendance.
  - Admins to login and download attendance data as CSV.
- Face encoding generation from student images.
- Secure storage of environment variables and credentials.

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** – for image processing and webcam access
- **Insight Face** – for generating and comparing facial encodings
- **Yolo** – for Face detection
- **Flask** – for web interface
- **Firebase** – to store and fetch attendance data
- **HTML/CSS** – for frontend templates

---

## 🧪 Sample Usage

- When `main.py` runs, it accesses the webcam, identifies students' faces in real-time using YOLOv8 and face recognition, and records attendance by marking them present in the Firebase Realtime Database.

- **Students** can log in through the web interface to:
  - View their **real-time attendance records**
  - Check their **weekly attendance**
  - Track **cumulative attendance**
  - Monitor **weekly average** and **cumulative average**

- **Admins** (management) can:
  - Log in via `/login`
  - View all attendance records
  - Download attendance data in **CSV format** for any date

---

## ✅ How to Run the Project

1. Clone the repository
   ```bash
    git clone https://github.com/RanaRam021/Smart-Attendance-Management-System.git
    cd Smart-Attendance-Management-System

2. Create and activate virtual environment
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    
    --- OR ---
    source venv/bin/activate # On macOS/Linux

3. Install dependencies
    ```bash
    pip install -r requirements.txt

4. Setup Firebase
- Create a Firebase project.
- Download serviceAccountKey.json and save it in the project root.
- Create a .env file and add:
    ```bash
    FIREBASE_DB_URL=your_firebase_realtime_database_url

5. Generate encodings
- Make sure student images are placed in the Images/ folder.
    ```bash
    python EncodeGenerator.py

6. Start face recognition system
    ```bash
    python main.py

7. Run Flask web app
    ```bash
    python app.py

---

## 🔐 Note on Dataset

> The image dataset used for face encoding is **not included** in this repository due to **privacy concerns**. You may create your own dataset under the `Images/` directory following the required structure.

---

## 🤝 Contribution
- Contributions are welcome! Please fork the repository and submit a pull request for review.

