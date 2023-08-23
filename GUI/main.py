from profilehooks import profile
from functools import lru_cache
import sys
import os
import cv2
import numpy as np
from PIL import Image
import platform
from icecream import ic
from time import sleep
from ui_interface import *
from Custom_Widgets.Widgets import *
from PySide2.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from PySide2.QtSql import *

# Set enable for debugging.
ic.enable()
HOME_PATH = os.path.dirname(os.path.realpath(__file__))

class DatasetPopulatorThread(QThread):
    new_frame = pyqtSignal(QImage)
    saved_image = pyqtSignal(str)
    done_populating = pyqtSignal(str)

    def __init__(self, parent=None, camera_number:int=0, face_id:int=1, numberOfImages:int=30, initialCount:int=0):
        super().__init__(parent)
        self.face_detector = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
        self.face_id = face_id
        self.cam_number = camera_number
        self.numOfImg = numberOfImages
        self.initialCount = initialCount
        self.running = True
        self.video_capture = cv2.VideoCapture(self.cam_number)
        ic()

    def run(self):
        count = self.initialCount
        while self.running:
            ret, frame = self.video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1
                cv2.imwrite(f"{HOME_PATH}/Assets/dataset/User." + str(self.face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                self.saved_image.emit(f"Writing User." + str(self.face_id) + "." + str(count) + ".jpg")
            if count >= self.numOfImg:
                self.running = False
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                qt_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
                self.new_frame.emit(qt_image)
        self.video_capture.release()
        self.done_populating.emit(f"Done populating the Dataset for user {self.face_id} with {self.numOfImg} image Samples.")
    
    def stop(self):
        ic()
        self.running = False
        self.video_capture.release()

class TrainingDatasetThread(QThread):
    output_text = pyqtSignal(str)
    trainingComplete = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.datasetPath = f"{HOME_PATH}/Assets/dataset"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
        ic()

    def getImagesAndLabels(self, path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split('.')[1])
            faces = self.detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        ic()
        return faceSamples, ids
    
    def run(self):
        self.output_text.emit("Training faces. It will tke a few seconds. Wait ....")
        faces, ids = self.getImagesAndLabels(self.datasetPath)
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(f"{HOME_PATH}/Assets/trainer/trainer.yml")
        text = "{0} faces trained.".format(len(np.unique(ids)))
        self.output_text.emit(text)
        self.trainingComplete.emit()
        ic()

class FaceRecognitionTread(QThread):
    new_frame = pyqtSignal(QImage)
    error_announce = pyqtSignal(str)
    recognized = pyqtSignal(str)
    def __init__(self, names:list, camera_number:int=0):
        super().__init__()
        try:
            self.names = names
            self.recognizer = cv2.face.LBPHFaceRecognizer_create()
            self.faceCascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
            self.recognizer.read(f"{HOME_PATH}/Assets/trainer/trainer.yml")
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.cam_number = camera_number
            self.video_capture = cv2.VideoCapture(self.cam_number)
        except Exception as e:
            ic(e)
            self.error_announce.emit(str(e))
        ic()

    def run(self):
        self.running = True
        id = 0
        try:
            while self.running:
                ret, frame = self.video_capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 5
                )
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
                    id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])

                    if (confidence < 100):
                        id = self.names[id]
                        confidence = f" {round(100 - confidence)}"
                    else:
                        id = "unknown"
                        confidence = f" {round(100 - confidence)}"
                    
                    cv2.putText(
                        frame, str(id),
                        (x+5,y-5),
                        self.font, 1,
                        (255,255,255), 2
                    )
                    cv2.putText(
                        frame,
                        str(confidence),
                        (x+5, y+h-5),
                        self.font, 1,
                        (255,255,0), 1
                    )
                    self.recognized.emit(str(id))

                if ret:
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    qt_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
                    self.new_frame.emit(qt_image)

        except Exception as e:
            ic(e)
            self.error_announce.emit(str(e))
        ic()
    
    def stop(self):
        try:
            self.quit()
            self.running = False
            self.video_capture.release()
        except Exception as e:
            self.new_frame.emit(e)
            ic(e)
        ic()

@profile(stdout=False, filename='main.prof')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not self.createDatabase():
            sys.exit(1)

        self.ui.cameraSelect.addItems(self.get_connected_cameras())
        self.ui.cameraSelectRec.addItems(self.get_connected_cameras())
        self.ui.imagesToTake.valueChanged.connect(self.sliderMoved)
        self.ui.datasetProcess.clicked.connect(self.datasetPopulationStart)
        self.ui.trainDatasetBtn.clicked.connect(self.datasetTrainingStart)
        self.ui.startRecognitionBtn.clicked.connect(self.faceRecognitionStart)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateNumOfTrainedUsers)
        self.timer.timeout.connect(self.createView)
        self.timer.start(1000)

        self.datasetPopulator = None
        self.trainingDataset = None
        self.recognizeFaces = None
        loadJsonStyle(self, self.ui)
        self.show()

    def datasetPopulationStart(self):
        name = self.ui.lineEdit.text().lower()
        if name:
            cam_number = self.ui.cameraSelect.currentIndex()
            numOfImg = self.ui.lcdNumber_2.value()
            self.ui.datasetProcess.setEnabled(False)
            face_id, initialCount, numOfImages = self.generateId(name, numOfImg)
            self.faceRecognitionStop()
            self.datasetPopulator = DatasetPopulatorThread(camera_number=cam_number,
                                                        face_id=face_id, numberOfImages=numOfImages, initialCount=initialCount)
            self.datasetPopulator.new_frame.connect(self.update_frame)
            self.datasetPopulator.saved_image.connect(self.text_output)
            self.datasetPopulator.done_populating.connect(self.announcer)
            self.datasetPopulator.done_populating.connect(self.datasetPopulationComplete)
            self.datasetPopulator.start()
        else:
            self.announcer("Please enter a name")
    
    def datasetPopulationStop(self):
        if self.datasetPopulator and self.datasetPopulator.isRunning():
            self.datasetPopulator.stop()
            self.datasetPopulator.wait()
            self.datasetPopulator = None
    
    def datasetPopulationComplete(self):
        self.ui.datasetProcess.setEnabled(True)
        self.datasetPopulator = None
        ic()
    
    def datasetTrainingStart(self):
        self.faceRecognitionStop()
        self.ui.trainDatasetBtn.setEnabled(False)
        self.trainingDataset = TrainingDatasetThread()
        self.trainingDataset.output_text.connect(self.text_output)
        self.trainingDataset.trainingComplete.connect(self.datasetTrainingComplete)
        self.trainingDataset.start()
        ic()

    def datasetTrainingComplete(self):
        self.trainingDataset = None
        self.ui.trainDatasetBtn.setEnabled(True)
        self.updateNumOfTrainedUsers()
        self.text_output("Dataset training complete!!")

    def faceRecognitionStart(self):
        cam_number = self.ui.cameraSelectRec.currentIndex()
        self.ui.startRecognitionBtn.setEnabled(False)
        names = self.fetchNames()
        self.recognizeFaces = FaceRecognitionTread(names, cam_number)
        self.recognizeFaces.new_frame.connect(self.update_frame)
        self.recognizeFaces.error_announce.connect(self.announcer)
        self.recognizeFaces.recognized.connect(self.updateRecognizedOutput)
        self.recognizeFaces.start()
        ic()

    def faceRecognitionStop(self):
        if self.recognizeFaces and self.recognizeFaces.isRunning():
            self.recognizeFaces.stop()
            self.recognizeFaces.wait()
            self.recognizeFaces = None
            self.ui.startRecognitionBtn.setEnabled(True)
            self.text_output("Face Recognition Stopped.")
        ic()

    def fetchNames(self) -> list:
        fetchQuery = QSqlQuery()
        names = []
        fetchQuery.exec_("SELECT name FROM users")
        while fetchQuery.next():
            names.append(fetchQuery.value(0))
        fetchQuery.finish()
        ic(names)
        return names
        
    def fetchnumberOfImages(self, id_:int) -> int:
        fetchQuery = QSqlQuery()
        fetchQuery.prepare("SELECT numberOfImages FROM traineddata WHERE id = ?")
        fetchQuery.addBindValue(id_)
        if fetchQuery.exec_():
            while fetchQuery.next():
                num = fetchQuery.value("numberOfImages")
        return num

    def generateId(self, currentUser:str, numOfImages:int) -> tuple:
        names = self.fetchNames()
        id_ = names.index(currentUser)
        if currentUser in names:
            ic("Duplicates found")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"The name {currentUser} already exsists. To add into the dataset, press OK if otherwise press CANCEL")
            msg.setWindowTitle("Duplicates")
            cancel_button = msg.addButton("Cancel", QMessageBox.RejectRole)
            ok_button = msg.addButton("Ok", QMessageBox.AcceptRole)
            msg.exec_()
            clickedButton = msg.clickedButton()
            if clickedButton == cancel_button:
                initialCount = 0
                self.updateDatabase(id_, numOfImages)
                return id_, initialCount, numOfImages
            elif clickedButton == ok_button:
                initialCount = numOfImages
                numOfImages = int(self.fetchnumberOfImages(id_)) + int(numOfImages)
                ic(int(self.fetchnumberOfImages(id_)))
                ic(int(numOfImages))
                ic(initialCount)
                self.updateDatabase(id_, numOfImages)
                return id_, initialCount, numOfImages
        elif currentUser not in names:
            ic("duplicates not found")
            id = len(names)
            self.addToDatabase(currentUser, id, numOfImages)
            initialCount = 0
            return id, initialCount, numOfImages

    def addToDatabase(self, name:str, id:int, numOfImages:int) -> bool:
        addToTrainedDataQuery = QSqlQuery()
        addToTrainedDataQuery.prepare("INSERT INTO traineddata (id, numberOfImages) VALUES (?, ?)")
        addToTrainedDataQuery.addBindValue(id)
        addToTrainedDataQuery.addBindValue(numOfImages)
        addTousersQuery = QSqlQuery()
        addTousersQuery.prepare("INSERT INTO users(id, name) VALUES (?, ?)")
        addTousersQuery.addBindValue(id)
        addTousersQuery.addBindValue(name)
        if addToTrainedDataQuery.exec_():
            if addTousersQuery.exec_():
                ic("Both queries worked succesfully")
                return True
            else:
                ic("The add to users query did not work")
                return False
        else:
            ic("The add to traineddata qeury did not work")
            return False
        
    def updateDatabase(self, id:int, numOfImages:int) -> bool:
        updateTrainedDataQuery = QSqlQuery()
        updateTrainedDataQuery.prepare("UPDATE traineddata SET numberOfImages = ? WHERE id = ?")
        updateTrainedDataQuery.addBindValue(numOfImages)
        updateTrainedDataQuery.addBindValue(id)
        if updateTrainedDataQuery.exec_():
            ic("Update query worked fine")
            return True
        else:
            ic("The update query did not work fine")
            return False
        
    def createView(self):
        self.model = QSqlTableModel()
        self.model.setTable("users")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "id")
        self.model.setHeaderData(1, Qt.Horizontal, "name")
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()

    def text_output(self, text:str):
        text += "\n"
        self.ui.textOutput.setReadOnly(False)
        self.ui.textOutput.insertPlainText(text)
        self.ui.textOutput.setReadOnly(True)
        ic()

    def updateRecognizedOutput(self, txt:str):
        currentText = self.ui.recognizedNames.toPlainText()
        if txt != currentText.split():
            txt += "\n"
            self.ui.recognizedNames.insertPlainText(txt)

    def updateNumOfTrainedUsers(self):
        numTrainedUsers = int(len(self.fetchNames())-1)
        self.ui.noOfTrainedPeopleDisplay.display(numTrainedUsers)
        self.ui.noOfTrainedPeopleDisplay2.display(numTrainedUsers)

    def update_frame(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self.ui.pixmap_item.setPixmap(pixmap)

    def createDatabase(self):
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName(f"{HOME_PATH}/Assets/FaceRecognition.sqlite3")
        if not self.con.open():
            QMessageBox.critical(
                None,
                "Facial Recognition - Error",
                "Database Error: %s" % self.con.lastError().databaseText()
            )
            ic()
            return False
        query = QSqlQuery()
        if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS traineddata(
            id IiNTEGER PRIMARY KEY UNIQUE NOT NULL,
            numberOfImages INTEGER NOT NULL
                )
            """
        ):
            QMessageBox.critical(
                None,
                "Facial Recognition - Error",
                "Database Error: %s" % self.con.lastError().databaseText()
            )
            return False
        if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL,
            FOREIGN KEY(id) REFERENCES traineddata(id),
            PRIMARY KEY(id)
                )
            """
        ):
            QMessageBox.critical(
                None,
                "Facial Recognition - Error",
                "Database Error: %s" % self.con.lastError().databaseText()
            )
            return False
        if len(self.fetchNames()) == 0:
            self.addToDatabase('unknown', 0, 0)
        ic()
        query.finish()
        return True

    @lru_cache(maxsize=1024)
    def get_connected_cameras(self):
        camera_names = []

        # Determine the operating system
        os_name = platform.system()
        if os_name == "Windows":
            for i in range(10):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    camera_name = f"Camera {i + 1}"
                    camera_names.append(camera_name)
                    cap.release()

        elif os_name == "Linux" or os_name == "Darwin":
            for i in range(10):
                cap = cv2.VideoCapture(f'/dev/video{i}')
                if cap.isOpened():
                    camera_name = f"Camera {i + 1}"
                    camera_names.append(camera_name)
                    cap.release()
        ic()
        return camera_names
    
    def sliderMoved(self):
        value = self.ui.imagesToTake.value()
        self.ui.lcdNumber_2.display(value)
        ic()

    def announcer(self, announcement:str):
        announce = QMessageBox()
        announce.setIcon(QMessageBox.Information)
        announce.setText(announcement)
        announce.setWindowTitle("Info")
        announce.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        run = announce.exec()
        ic()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())