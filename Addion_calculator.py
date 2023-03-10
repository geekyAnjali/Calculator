# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Addion_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 600)
        MainWindow.setStyleSheet("background-color: rgb(56, 124, 131);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(56, 124, 131);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 6)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 4, 1, 1)
        self.rslt_bx = QtWidgets.QLineEdit(self.centralwidget)
        self.rslt_bx.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"background-color: rgb(255,255,255);")
        self.rslt_bx.setText("")
        self.rslt_bx.setObjectName("rslt_bx")
        self.gridLayout.addWidget(self.rslt_bx, 6, 1, 1, 1)
        self.Add_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_bttn.setStyleSheet("\n"
"background-color: rgb(193, 193, 193);\n"
"QPUshButton::hover:\n"
"background-color: rgb(203, 237, 255);")
        self.Add_bttn.setObjectName("Add_bttn")
        self.gridLayout.addWidget(self.Add_bttn, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.Num2_input = QtWidgets.QSpinBox(self.centralwidget)
        self.Num2_input.setStyleSheet("background-color: rgb(105, 255, 243);")
        self.Num2_input.setObjectName("Num2_input")
        self.gridLayout.addWidget(self.Num2_input, 3, 1, 1, 1)
        self.Num1_input = QtWidgets.QSpinBox(self.centralwidget)
        self.Num1_input.setStyleSheet("background-color: rgb(105, 255, 243);")
        self.Num1_input.setObjectName("Num1_input")
        self.gridLayout.addWidget(self.Num1_input, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.Num3_input = QtWidgets.QSpinBox(self.centralwidget)
        self.Num3_input.setStyleSheet("background-color: rgb(105, 255, 243);")
        self.Num3_input.setObjectName("Num3_input")
        self.gridLayout.addWidget(self.Num3_input, 4, 1, 1, 1)
        self.Clr_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.Clr_bttn.setStyleSheet("\n"
"background-color: rgb(193, 193, 193);\n"
"QPUshButton::hover:\n"
"background-color: rgb(203, 237, 255);")
        self.Clr_bttn.setObjectName("Clr_bttn")
        self.gridLayout.addWidget(self.Clr_bttn, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Addition program"))
        self.label_3.setText(_translate("MainWindow", "Num1"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.Add_bttn.setText(_translate("MainWindow", "ADD"))
        self.label_2.setText(_translate("MainWindow", "Num2"))
        self.label_5.setText(_translate("MainWindow", "Num3"))
        self.Clr_bttn.setText(_translate("MainWindow", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
