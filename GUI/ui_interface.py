# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacegfPtTU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(887, 588)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.headerContainer)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Title)

        self.headerSubContainer = QFrame(self.headerContainer)
        self.headerSubContainer.setObjectName(u"headerSubContainer")
        self.headerSubContainer.setFrameShape(QFrame.StyledPanel)
        self.headerSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerSubContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.headerSubContainer)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.headerSubContainer)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon1)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.headerSubContainer)
        self.closeBtn.setObjectName(u"closeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.headerSubContainer, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.headerContainer, 0, 0, 1, 2, Qt.AlignTop)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leftContainer = QFrame(self.mainContainer)
        self.leftContainer.setObjectName(u"leftContainer")
        self.leftContainer.setFrameShape(QFrame.StyledPanel)
        self.leftContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.leftContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cameraOutput = QLabel(self.leftContainer)
        self.cameraOutput.setObjectName(u"cameraOutput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cameraOutput.sizePolicy().hasHeightForWidth())
        self.cameraOutput.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.cameraOutput, 0, 0, 1, 1)

        self.textOutput = QPlainTextEdit(self.leftContainer)
        self.textOutput.setObjectName(u"textOutput")

        self.gridLayout_3.addWidget(self.textOutput, 1, 0, 1, 1, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.leftContainer)

        self.rightContainer = QFrame(self.mainContainer)
        self.rightContainer.setObjectName(u"rightContainer")
        self.rightContainer.setFrameShape(QFrame.StyledPanel)
        self.rightContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.rightContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rightContainerHeader = QFrame(self.rightContainer)
        self.rightContainerHeader.setObjectName(u"rightContainerHeader")
        sizePolicy2.setHeightForWidth(self.rightContainerHeader.sizePolicy().hasHeightForWidth())
        self.rightContainerHeader.setSizePolicy(sizePolicy2)
        self.rightContainerHeader.setFrameShape(QFrame.StyledPanel)
        self.rightContainerHeader.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.rightContainerHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QCustomStackedWidget(self.rightContainerHeader)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.imageDataset = QWidget()
        self.imageDataset.setObjectName(u"imageDataset")
        self.formLayout = QFormLayout(self.imageDataset)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.imageDataset)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cameraSelect = QComboBox(self.imageDataset)
        self.cameraSelect.setObjectName(u"cameraSelect")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cameraSelect)

        self.label_4 = QLabel(self.imageDataset)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lcdNumber_2 = QLCDNumber(self.imageDataset)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("intValue", 30)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lcdNumber_2)

        self.imagesToTake = QDial(self.imageDataset)
        self.imagesToTake.setObjectName(u"imagesToTake")
        self.imagesToTake.setMinimum(1)
        self.imagesToTake.setMaximum(100)
        self.imagesToTake.setSingleStep(10)
        self.imagesToTake.setValue(30)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.imagesToTake)

        self.label_3 = QLabel(self.imageDataset)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setWordWrap(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.noOfTrainedPeopleDisplay = QLCDNumber(self.imageDataset)
        self.noOfTrainedPeopleDisplay.setObjectName(u"noOfTrainedPeopleDisplay")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.noOfTrainedPeopleDisplay)

        self.label_5 = QLabel(self.imageDataset)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(self.imageDataset)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit)

        self.existingUser = QCheckBox(self.imageDataset)
        self.existingUser.setObjectName(u"existingUser")
        self.existingUser.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.existingUser)

        self.addOnDataset = QCheckBox(self.imageDataset)
        self.addOnDataset.setObjectName(u"addOnDataset")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.addOnDataset.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.addOnDataset)

        self.datasetProcess = QPushButton(self.imageDataset)
        self.datasetProcess.setObjectName(u"datasetProcess")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.datasetProcess)

        self.stackedWidget.addWidget(self.imageDataset)
        self.recognitionSettings = QWidget()
        self.recognitionSettings.setObjectName(u"recognitionSettings")
        self.gridLayout_4 = QGridLayout(self.recognitionSettings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.recognitionSettings)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.cameraSelectRec = QComboBox(self.recognitionSettings)
        self.cameraSelectRec.setObjectName(u"cameraSelectRec")

        self.gridLayout_4.addWidget(self.cameraSelectRec, 0, 1, 1, 2)

        self.label_6 = QLabel(self.recognitionSettings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 2)

        self.noOfTrainedPeopleDisplay2 = QLCDNumber(self.recognitionSettings)
        self.noOfTrainedPeopleDisplay2.setObjectName(u"noOfTrainedPeopleDisplay2")

        self.gridLayout_4.addWidget(self.noOfTrainedPeopleDisplay2, 1, 2, 1, 1)

        self.label_7 = QLabel(self.recognitionSettings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 2)

        self.recognizedNames = QTextEdit(self.recognitionSettings)
        self.recognizedNames.setObjectName(u"recognizedNames")

        self.gridLayout_4.addWidget(self.recognizedNames, 2, 2, 1, 1)

        self.startRecognitionBtn = QPushButton(self.recognitionSettings)
        self.startRecognitionBtn.setObjectName(u"startRecognitionBtn")

        self.gridLayout_4.addWidget(self.startRecognitionBtn, 3, 0, 1, 2)

        self.resetBtn = QPushButton(self.recognitionSettings)
        self.resetBtn.setObjectName(u"resetBtn")

        self.gridLayout_4.addWidget(self.resetBtn, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.recognitionSettings)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.rightContainerHeader)

        self.rightContainerFooter = QFrame(self.rightContainer)
        self.rightContainerFooter.setObjectName(u"rightContainerFooter")
        self.rightContainerFooter.setFrameShape(QFrame.StyledPanel)
        self.rightContainerFooter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rightContainerFooter)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.datasetBtn = QPushButton(self.rightContainerFooter)
        self.datasetBtn.setObjectName(u"datasetBtn")

        self.horizontalLayout_4.addWidget(self.datasetBtn)

        self.recognitionBtn = QPushButton(self.rightContainerFooter)
        self.recognitionBtn.setObjectName(u"recognitionBtn")

        self.horizontalLayout_4.addWidget(self.recognitionBtn)

        self.trainDatasetBtn = QPushButton(self.rightContainerFooter)
        self.trainDatasetBtn.setObjectName(u"trainDatasetBtn")

        self.horizontalLayout_4.addWidget(self.trainDatasetBtn)


        self.verticalLayout.addWidget(self.rightContainerFooter, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.rightContainer)


        self.gridLayout.addWidget(self.mainContainer, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.imagesToTake.rangeChanged.connect(self.lcdNumber_2.display)
        self.resetBtn.clicked.connect(self.recognizedNames.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Face Recognition", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.cameraOutput.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No of Images to Take", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"No of Trained People", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.existingUser.setText(QCoreApplication.translate("MainWindow", u"Existing User", None))
        self.addOnDataset.setText(QCoreApplication.translate("MainWindow", u"Add on existing Dataset", None))
        self.datasetProcess.setText(QCoreApplication.translate("MainWindow", u"Start Process", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"No of Trained People", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"People Recognized", None))
        self.startRecognitionBtn.setText(QCoreApplication.translate("MainWindow", u"Start Recognition", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.datasetBtn.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.recognitionBtn.setText(QCoreApplication.translate("MainWindow", u"Recognition", None))
        self.trainDatasetBtn.setText(QCoreApplication.translate("MainWindow", u"Train Dataset", None))
    # retranslateUi

