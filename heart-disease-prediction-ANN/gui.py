from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import tensorflow as tf
import os
import pandas as pd

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
        MainWindow.resize(800, 601)
        self.stylesheet ="""
        QMainWindow{
            background-color:#438644;
        }
        QLabel{
            color:#ffffff;
        }
        QFormLayout{
            margin-top:100px;
        }
        QLineEdit{
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        QComboBox{
            
        }
        """
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 10, 561, 471))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.l_age = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_age.setObjectName("l_age")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_age)
        self.age = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.age.setObjectName("age")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.age)
        self.l_sex = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_sex.setObjectName("l_sex")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l_sex)
        self.sex = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sex)
        self.l_cp = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_cp.setObjectName("l_cp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.l_cp)
        self.cp = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cp.setObjectName("cp")
        self.cp.addItem("")
        self.cp.addItem("")
        self.cp.addItem("")
        self.cp.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cp)
        self.l_trestbps = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_trestbps.setObjectName("l_trestbps")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.l_trestbps)
        self.trestbps = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.trestbps.setObjectName("trestbps")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.trestbps)
        self.l_chol = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_chol.setObjectName("l_chol")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.l_chol)
        self.chol = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.chol.setObjectName("chol")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.chol)
        self.fbs = QtWidgets.QComboBox(self.formLayoutWidget)
        self.fbs.setObjectName("fbs")
        self.fbs.addItem("")
        self.fbs.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fbs)
        self.l_restcg = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_restcg.setObjectName("l_restcg")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.l_restcg)
        self.restcg = QtWidgets.QComboBox(self.formLayoutWidget)
        self.restcg.setObjectName("restcg")
        self.restcg.addItem("")
        self.restcg.addItem("")
        self.restcg.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.restcg)
        self.l_thalach = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_thalach.setObjectName("l_thalach")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.l_thalach)
        self.thalach = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.thalach.setObjectName("thalach")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.thalach)
        self.l_exang = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_exang.setObjectName("l_exang")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.l_exang)
        self.exang = QtWidgets.QComboBox(self.formLayoutWidget)
        self.exang.setObjectName("exang")
        self.exang.addItem("")
        self.exang.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.exang)
        self.l_oldpeak = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_oldpeak.setObjectName("l_oldpeak")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.l_oldpeak)
        self.oldpeak = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.oldpeak.setObjectName("oldpeak")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.oldpeak)
        self.l_slope = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_slope.setObjectName("l_slope")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.l_slope)
        self.slop = QtWidgets.QComboBox(self.formLayoutWidget)
        self.slop.setObjectName("slop")
        self.slop.addItem("")
        self.slop.addItem("")
        self.slop.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.slop)
        self.l_ca = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_ca.setObjectName("l_ca")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.l_ca)
        self.ca = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ca.setObjectName("ca")
        self.ca.addItem("")
        self.ca.addItem("")
        self.ca.addItem("")
        self.ca.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ca)
        self.l_thal = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_thal.setObjectName("l_thal")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.l_thal)
        self.thal = QtWidgets.QComboBox(self.formLayoutWidget)
        self.thal.setObjectName("thal")
        self.thal.addItem("")
        self.thal.addItem("")
        self.thal.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.thal)
        self.l_target = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_target.setObjectName("l_target")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.l_target)
        self.target = QtWidgets.QComboBox(self.formLayoutWidget)
        self.target.setObjectName("target")
        self.target.addItem("")
        self.target.addItem("")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.target)
        self.l_fbs = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_fbs.setObjectName("l_fbs")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.l_fbs)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.hasil = QtWidgets.QLabel(self.formLayoutWidget)
        self.hasil.setObjectName("hasil")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.hasil)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.predict) #event buat klik

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet(self.stylesheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_age.setText(_translate("MainWindow", "Age"))
        self.l_sex.setText(_translate("MainWindow", "Sex"))
        self.sex.setItemText(0, _translate("MainWindow", "Male"))
        self.sex.setItemText(1, _translate("MainWindow", "Female"))
        self.l_cp.setText(_translate("MainWindow", "Cp"))
        self.cp.setItemText(0, _translate("MainWindow", "Typical Angina"))
        self.cp.setItemText(1, _translate("MainWindow", "Atypical Angina"))
        self.cp.setItemText(2, _translate("MainWindow", "Non-Anginal Pain"))
        self.cp.setItemText(3, _translate("MainWindow", "Asymptomatic"))
        self.l_trestbps.setText(_translate("MainWindow", "Trestbps"))
        self.l_chol.setText(_translate("MainWindow", "Chol"))
        self.fbs.setItemText(0, _translate("MainWindow", "True"))
        self.fbs.setItemText(1, _translate("MainWindow", "False"))
        self.l_restcg.setText(_translate("MainWindow", "Restcg"))
        self.restcg.setItemText(0, _translate("MainWindow", "Normal"))
        self.restcg.setItemText(1, _translate("MainWindow", "Having ST-T Wave Abnormality"))
        self.restcg.setItemText(2, _translate("MainWindow", "Showing Probable or Definite Left Ventricular Hypertrophy"))
        self.l_thalach.setText(_translate("MainWindow", "Thalach"))
        self.l_exang.setText(_translate("MainWindow", "Exang"))
        self.exang.setItemText(0, _translate("MainWindow", "Yes"))
        self.exang.setItemText(1, _translate("MainWindow", "No"))
        self.l_oldpeak.setText(_translate("MainWindow", "Oldpeak"))
        self.l_slope.setText(_translate("MainWindow", "Slope"))
        self.slop.setItemText(0, _translate("MainWindow", "Upsloping"))
        self.slop.setItemText(1, _translate("MainWindow", "Flat"))
        self.slop.setItemText(2, _translate("MainWindow", "Downsloping"))
        self.l_ca.setText(_translate("MainWindow", "Ca"))
        self.ca.setItemText(0, _translate("MainWindow", "0"))
        self.ca.setItemText(1, _translate("MainWindow", "1"))
        self.ca.setItemText(2, _translate("MainWindow", "2"))
        self.ca.setItemText(3, _translate("MainWindow", "3"))
        self.l_thal.setText(_translate("MainWindow", "Thal"))
        self.thal.setItemText(0, _translate("MainWindow", "Normal"))
        self.thal.setItemText(1, _translate("MainWindow", "Fixed Defect"))
        self.thal.setItemText(2, _translate("MainWindow", "Reversable Defect"))
        self.l_target.setText(_translate("MainWindow", "Target"))
        self.target.setItemText(0, _translate("MainWindow", "No"))
        self.target.setItemText(1, _translate("MainWindow", "Yes"))
        self.l_fbs.setText(_translate("MainWindow", "Fbs"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.hasil.setText(_translate("MainWindow", "TextLabel"))
        
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
        arrInput = np.array([age, int(sex), cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]).reshape((1,13))
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