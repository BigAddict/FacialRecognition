from PIL import Image
import numpy as np
import cv2
import os

class FaceRecognition:
    def __init__(self) -> None:
        self.home_path = os.path.dirname(os.path.realpath(__file__))
        self.face_detector = cv2.CascadeClassifier(
            f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"
            )
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        
    def face_dataset(self, cam_number:int=0, num_of_shots:int=30, face_id:int=1) -> cv2.Mat:
        self.cam_number = cam_number
        self.num_of_shot = num_of_shots
        self.face_id = face_id
        self.count = 0
        self.camera = cv2.VideoCapture(self.cam_number)
        while(True):
            ret, img = self.camera.read()
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(grayImg, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                self.count += 1
                cv2.imwrite(f"{self.home_path}/dataset/User." + str(self.face_id) + '.' + str(self.count) + ".jpg", grayImg[y:y+h,x:x+w])
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif self.count >= num_of_shots:
                break
        self.camera.release()
        return img

rec = FaceRecognition()
img = rec.face_dataset()
cv2.imshow("Image", img)