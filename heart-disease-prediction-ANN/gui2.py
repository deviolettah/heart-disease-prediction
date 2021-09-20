# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import tensorflow as tf
import os
import pandas as pd

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(16,input_dim=13, kernel_initializer='normal', activation='relu'),
  tf.keras.layers.Dense(32,kernel_initializer='normal', activation='relu'),
  tf.keras.layers.Dense(32,kernel_initializer='normal', activation='relu'),
  tf.keras.layers.Dense(8,kernel_initializer='normal', activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])
adam = tf.keras.optimizers.Adam(lr=0.001)
model.compile(optimizer=adam,
                loss='binary_crossentropy',
                metrics=['acc'])

checkpoint_filepath = './best_model/ckpt{epoch}.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_filepath)
latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)
model.load_weights(latest)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 553)
        MainWindow.setFixedSize(889, 553)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 891, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:green;\n"
"color:white;\n"
"font-size:18px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 31, 891, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size:18px;\n"
"background-color:white;\n"
"color:green;")
        self.label_2.setObjectName("label_2")
        self.hasil = QtWidgets.QLabel(self.centralwidget)
        self.hasil.setGeometry(QtCore.QRect(700, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.hasil.setFont(font)
        self.hasil.setStyleSheet("font-size:12px;\n"
"background-color:orange;")
        self.hasil.setAlignment(QtCore.Qt.AlignCenter)
        self.hasil.setObjectName("hasil")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size:18px")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(599, 60, 291, 451))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(-1, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color:#02ce02;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(60, 70, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.age.setFont(font)
        self.age.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.age.setObjectName("age")
        self.sex = QtWidgets.QComboBox(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(60, 100, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.sex.setFont(font)
        self.sex.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.cp = QtWidgets.QComboBox(self.centralwidget)
        self.cp.setGeometry(QtCore.QRect(60, 130, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.cp.setFont(font)
        self.cp.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.cp.setObjectName("cp")
        self.cp.addItem("")
        self.cp.addItem("")
        self.cp.addItem("")
        self.cp.addItem("")
        self.trestbps = QtWidgets.QLineEdit(self.centralwidget)
        self.trestbps.setGeometry(QtCore.QRect(60, 160, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.trestbps.setFont(font)
        self.trestbps.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.trestbps.setObjectName("trestbps")
        self.chol = QtWidgets.QLineEdit(self.centralwidget)
        self.chol.setGeometry(QtCore.QRect(60, 190, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.chol.setFont(font)
        self.chol.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.chol.setObjectName("chol")
        self.fbs = QtWidgets.QComboBox(self.centralwidget)
        self.fbs.setGeometry(QtCore.QRect(60, 220, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.fbs.setFont(font)
        self.fbs.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.fbs.setObjectName("fbs")
        self.fbs.addItem("")
        self.fbs.addItem("")
        self.restcg = QtWidgets.QComboBox(self.centralwidget)
        self.restcg.setGeometry(QtCore.QRect(60, 250, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.restcg.setFont(font)
        self.restcg.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.restcg.setObjectName("restcg")
        self.restcg.addItem("")
        self.restcg.addItem("")
        self.restcg.addItem("")
        self.thalach = QtWidgets.QLineEdit(self.centralwidget)
        self.thalach.setGeometry(QtCore.QRect(60, 280, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.thalach.setFont(font)
        self.thalach.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.thalach.setObjectName("thalach")
        self.exang = QtWidgets.QComboBox(self.centralwidget)
        self.exang.setGeometry(QtCore.QRect(60, 310, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.exang.setFont(font)
        self.exang.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.exang.setObjectName("exang")
        self.exang.addItem("")
        self.exang.addItem("")
        self.oldpeak = QtWidgets.QLineEdit(self.centralwidget)
        self.oldpeak.setGeometry(QtCore.QRect(60, 340, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.oldpeak.setFont(font)
        self.oldpeak.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.oldpeak.setObjectName("oldpeak")
        self.slop = QtWidgets.QComboBox(self.centralwidget)
        self.slop.setGeometry(QtCore.QRect(60, 370, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.slop.setFont(font)
        self.slop.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.slop.setObjectName("slop")
        self.slop.addItem("")
        self.slop.addItem("")
        self.slop.addItem("")
        self.ca = QtWidgets.QComboBox(self.centralwidget)
        self.ca.setGeometry(QtCore.QRect(60, 400, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.ca.setFont(font)
        self.ca.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.ca.setObjectName("ca")
        self.ca.addItem("")
        self.ca.addItem("")
        self.ca.addItem("")
        self.ca.addItem("")
        self.thal = QtWidgets.QComboBox(self.centralwidget)
        self.thal.setGeometry(QtCore.QRect(60, 430, 511, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.thal.setFont(font)
        self.thal.setStyleSheet("font-size:12px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;")
        self.thal.setObjectName("thal")
        self.thal.addItem("")
        self.thal.addItem("")
        self.thal.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 460, 511, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font-size:12px;\n"
"background-color: #FFA500;")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 250, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 280, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 310, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 340, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 370, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 400, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 430, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_16.setObjectName("label_16")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 60, 601, 451))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:green;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.hasil.raise_()
        self.label_3.raise_()
        self.age.raise_()
        self.sex.raise_()
        self.cp.raise_()
        self.trestbps.raise_()
        self.chol.raise_()
        self.fbs.raise_()
        self.restcg.raise_()
        self.thalach.raise_()
        self.exang.raise_()
        self.oldpeak.raise_()
        self.slop.raise_()
        self.ca.raise_()
        self.thal.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.predict)#event buat klik

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Klasifikasi Penyakit Jantung"))
        self.label_2.setText(_translate("MainWindow", " Algoritma Neural Network"))
        self.hasil.setText(_translate("MainWindow", "HASIL"))
        self.label_3.setText(_translate("MainWindow", "Resiko Penyakit Jantung:"))
        self.sex.setItemText(0, _translate("MainWindow", "Male"))
        self.sex.setItemText(1, _translate("MainWindow", "Female"))
        self.cp.setItemText(0, _translate("MainWindow", "Typical Angina"))
        self.cp.setItemText(1, _translate("MainWindow", "Atypical Angina"))
        self.cp.setItemText(2, _translate("MainWindow", "Non-Anginal Pain"))
        self.cp.setItemText(3, _translate("MainWindow", "Asymptomatic"))
        self.fbs.setItemText(0, _translate("MainWindow", "True"))
        self.fbs.setItemText(1, _translate("MainWindow", "False"))
        self.restcg.setItemText(0, _translate("MainWindow", "Normal"))
        self.restcg.setItemText(1, _translate("MainWindow", "Having ST-T Wave Abnormality"))
        self.restcg.setItemText(2, _translate("MainWindow", "Showing Probable or Definite Left Ventricular Hypertrophy"))
        self.exang.setItemText(0, _translate("MainWindow", "Yes"))
        self.exang.setItemText(1, _translate("MainWindow", "No"))
        self.slop.setItemText(0, _translate("MainWindow", "Upsloping"))
        self.slop.setItemText(1, _translate("MainWindow", "Flat"))
        self.slop.setItemText(2, _translate("MainWindow", "Downsloping"))
        self.ca.setItemText(0, _translate("MainWindow", "0"))
        self.ca.setItemText(1, _translate("MainWindow", "1"))
        self.ca.setItemText(2, _translate("MainWindow", "2"))
        self.ca.setItemText(3, _translate("MainWindow", "3"))
        self.thal.setItemText(0, _translate("MainWindow", "Normal"))
        self.thal.setItemText(1, _translate("MainWindow", "Fixed Defect"))
        self.thal.setItemText(2, _translate("MainWindow", "Reversable Defect"))
        self.pushButton.setText(_translate("MainWindow", "PREDICT"))
        self.label_4.setText(_translate("MainWindow", "Age"))
        self.label_5.setText(_translate("MainWindow", "Sex"))
        self.label_6.setText(_translate("MainWindow", "Cp"))
        self.label_7.setText(_translate("MainWindow", "Testbps"))
        self.label_8.setText(_translate("MainWindow", "Chol"))
        self.label_9.setText(_translate("MainWindow", "Fbs"))
        self.label_10.setText(_translate("MainWindow", "Restecg"))
        self.label_11.setText(_translate("MainWindow", "Thalach"))
        self.label_12.setText(_translate("MainWindow", "Exang"))
        self.label_13.setText(_translate("MainWindow", "Oldpeak"))
        self.label_14.setText(_translate("MainWindow", "Slope"))
        self.label_15.setText(_translate("MainWindow", "Ca"))
        self.label_16.setText(_translate("MainWindow", "Thal"))
        
    def predict(self): # fungsi saat klik
        # proses mengambil value
        age = self.age.text()
        sex = 1 if self.sex.currentText() == 'Male' else 0

        # cp = self.cp.currentText()
        if self.cp.currentText() == 'Typical Angina':
            cp = 1
        elif self.cp.currentText() == 'Atypical Angina':
            cp = 2
        elif self.cp.currentText() == 'Non-Anginal Pain':
            cp = 3
        elif self.cp.currentText() == 'Asymptomatic':
            cp = 4

        trestbps = self.trestbps.text()
        chol = self.chol.text()
        fbs = 1 if self.fbs.currentText() == 'True' else 0

        # restcg = self.restcg.currentText()
        if self.restcg.currentText() == 'Normal':
            restcg = 0 
        elif self.restcg.currentText() == 'Having ST-T Wave Abnormality':
            restcg = 1
        elif self.restcg.currentText() == 'Showing Probable or Definite Left Ventricular Hypertrophy':
            restcg = 2
            
        thalach  = self.thalach.text()
        exang = 1 if self.exang.currentText() == 'Yes' else 0
        oldpeak = self.oldpeak.text()

        # slope = self.slop.currentText()
        if self.slop.currentText() == 'Upsloping':
            slope = 1 
        elif self.slop.currentText() == 'Flat':
            slope = 2
        elif self.slop.currentText() == 'Downsloping':
            slope = 3
        
        ca = self.ca.currentText()
        
        # thal = self.thal.currentText()
        if self.thal.currentText() == 'Normal':
            thal = 3 
        elif self.thal.currentText() == 'Fixed Defect':
            thal = 6
        elif self.thal.currentText() == 'Reversable Defect':
            thal = 7
        
        # input value ke array
        arrInput = np.array([float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restcg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]).reshape((1,13))
        print(arrInput) # cetak input di cmd
        print(arrInput.shape) # cetak dimensi array
        
        #prediksi
        predictions = model.predict(arrInput)
        print(predictions[0])
        if predictions[0]<0.5:
            print("0 tidak beresiko")
            hsl = "Tidak Beresiko"
        elif predictions[0]>=0.5:
            print("1 beresiko")
            hsl = "Beresiko"
            
        _translate = QtCore.QCoreApplication.translate 
        self.hasil.setText(_translate("MainWindow", hsl)) # ubah label hasil dg umur
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
