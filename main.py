import cv2
import numpy as np
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
import insightface
import pickle
from ultralytics import YOLO   # type: ignore
from dotenv import load_dotenv
import os

load_dotenv() 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':  os.getenv("DB_URL")
})

app = insightface.app.FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))  # ctx_id=0 for CPU, or use 1 for GPU

print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

cap = cv2.VideoCapture(0)  

model = YOLO('yolov8n.pt')  

def cosine_similarity(embedding1, embedding2):
    
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    return dot_product / (norm1 * norm2)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  
    if not success:
        print("Failed to grab frame")
        continue

    results = model(imgS)  

    boxes = results[0].boxes  
    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            w, h = x2 - x1, y2 - y1
            imgFace = imgS[y1:y1 + h, x1:x1 + w]

            
            padding = 0.7
            x1, y1 = int(x1 + padding * w), int(y1 + padding * h)
            x2, y2 = int(x2 - padding * w), int(y2 - padding * h)
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            
            faces = app.get(imgFace)
            if faces:
                
                face = faces[0]
                encodeFace = np.array(face.embedding)

                
                similarity_scores = [cosine_similarity(encodeFace, known_encode) for known_encode in encodeListKnown]
                matchIndex = np.argmax(similarity_scores) 

                if similarity_scores[matchIndex] > 0.6:  
                
               
                    
                    id = studentIds[matchIndex]

                  
                    studentInfo = db.reference(f'Students/{id}').get()
                    print(studentInfo)

                  
                    datetimeObject = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                    now = datetime.now()
                
                    commonInfo = db.reference(f'commoninfo').get()
                    commonInfoRef = db.reference(f'commoninfo')
                    last_reset_date_str = commonInfo['last_reset_date']
                    last_reset_date = datetime.strptime(last_reset_date_str, "%Y-%m-%d")

                   
                    if (now - last_reset_date).days >= 7:
                        ref = db.reference(f'Students/{id}')
                        studentInfo['weekly_total_attendance'] = 0
                        ref.child('weekly_total_attendance').set(studentInfo['weekly_total_attendance'])
                        

                        commonInfoRef.child('last_reset_date').set(now.strftime("%Y-%m-%d"))

                    if secondsElapsed > 30:
                        ref = db.reference(f'Students/{id}')
                        studentInfo['cumulative_total_attendance'] += 1
                        studentInfo['weekly_total_attendance'] += 1
                        ref.child('cumulative_total_attendance').set(studentInfo['cumulative_total_attendance'])
                        ref.child('weekly_total_attendance').set(studentInfo['weekly_total_attendance'])

                        studentInfo['cumulative_total_percentage'] = ( studentInfo['cumulative_total_attendance'] / commonInfo['cumulative_total_classes']) * 100
                        studentInfo['weekly_total_percentage'] = ( studentInfo['weekly_total_attendance'] / commonInfo['weekly_total_classes']) * 100 
                        
                        ref.child('weekly_total_percentage').set(round(studentInfo['weekly_total_percentage'],2))
                        ref.child('cumulative_total_percentage').set(round(studentInfo['cumulative_total_percentage'],2))
                        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    cv2.imshow("Face Attendance", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
