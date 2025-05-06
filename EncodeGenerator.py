import cv2
import insightface
import pickle
import os


app = insightface.app.FaceAnalysis()
app.prepare(ctx_id=1, det_size=(640, 640))  


folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        
        faces = app.get(img_rgb)

       
        if len(faces) > 0:
           
            face = faces[0]
            encode = face.embedding  
            encodeList.append(encode)
        else:
            print("No face detected in the image.")
    
    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("File Saved")

