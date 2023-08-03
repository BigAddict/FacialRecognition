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
        
    def face_dataset(self, cam_number:int=0, num_of_shots:int=30) -> cv2.Mat:
        self.cam_number = cam_number
        self.num_of_shot = num_of_shots
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
    
    def getImagesAndLabels(self, path) -> dict:
        self._path = path
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        self._faceSamples = []
        ids = []

        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            Img_id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = self.face_detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                self._faceSamples.append(img_numpy[y:y+h,x:x+h])
                ids.append(Img_id)
        return self._faceSamples,ids

    def face_training(self) -> None:
        self.dataset_path = f'{self.home_path}/dataset'
        faces,ids = self.getImagesAndLabels(self.dataset_path)
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(f'{self.home_path}/trainer/trainer.yml')
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

    def face_recognition(self, cam_number:int) -> cv2.Mat:
        self.cam_number = cam_number
        self.camera = cv2.VideoCapture(self.cam_number)
        self.camera.set(3, 640)
        self.camera.set(4, 480)
        self.id = 0
        self.names = ['None', 'BigAddict', '420_G', 'Taraja']
        
        minW = 0.1*self.camera.get(3)
        minH = 0.1*self.camera.get(4)
        while True:
            ret, img = self.camera.read()

rec = FaceRecognition()
rec.face_dataset()