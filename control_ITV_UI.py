# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_ITV.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ITV_control(object):
    def setupUi(self, ITV_control):
        ITV_control.setObjectName("ITV_control")
        ITV_control.setEnabled(True)
        ITV_control.resize(720, 480)
        ITV_control.setMinimumSize(QtCore.QSize(720, 480))
        ITV_control.setMaximumSize(QtCore.QSize(720, 480))
        self.centralwidget = QtWidgets.QWidget(ITV_control)
        self.centralwidget.setObjectName("centralwidget")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(620, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.quit.setFont(font)
        self.quit.setStyleSheet("font:20pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 15px;")
        self.quit.setObjectName("quit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(7, 290, 701, 181))
        self.widget.setObjectName("widget")
        self.control = QtWidgets.QHBoxLayout(self.widget)
        self.control.setContentsMargins(0, 0, 0, 0)
        self.control.setObjectName("control")
        self.on = QtWidgets.QPushButton(self.widget)
        self.on.setMinimumSize(QtCore.QSize(275, 160))
        self.on.setMaximumSize(QtCore.QSize(275, 160))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.on.setFont(font)
        self.on.setAutoFillBackground(False)
        self.on.setStyleSheet("font:35pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 35px;")
        self.on.setObjectName("on")
        self.control.addWidget(self.on)
        self.off = QtWidgets.QPushButton(self.widget)
        self.off.setMinimumSize(QtCore.QSize(275, 160))
        self.off.setMaximumSize(QtCore.QSize(275, 160))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.off.setFont(font)
        self.off.setStyleSheet("font:35pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 35px;")
        self.off.setObjectName("off")
        self.control.addWidget(self.off)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 601, 281))
        self.widget1.setObjectName("widget1")
        self.output = QtWidgets.QVBoxLayout(self.widget1)
        self.output.setContentsMargins(0, 0, 0, 0)
        self.output.setObjectName("output")
        self.ITV_A = QtWidgets.QCheckBox(self.widget1)
        self.ITV_A.setMinimumSize(QtCore.QSize(600, 70))
        self.ITV_A.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ITV_A.setFont(font)
        self.ITV_A.setStyleSheet("font:35pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 10px;")
        self.ITV_A.setChecked(False)
        self.ITV_A.setObjectName("ITV_A")
        self.output.addWidget(self.ITV_A)
        self.ITV_B = QtWidgets.QCheckBox(self.widget1)
        self.ITV_B.setMinimumSize(QtCore.QSize(600, 70))
        self.ITV_B.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ITV_B.setFont(font)
        self.ITV_B.setStyleSheet("font:35pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 10px;")
        self.ITV_B.setChecked(False)
        self.ITV_B.setObjectName("ITV_B")
        self.output.addWidget(self.ITV_B)
        self.ITV_C = QtWidgets.QCheckBox(self.widget1)
        self.ITV_C.setMinimumSize(QtCore.QSize(600, 70))
        self.ITV_C.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ITV_C.setFont(font)
        self.ITV_C.setStyleSheet("font:35pt \"MS Shell Dlg 2\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(200, 200, 200), stop:1 rgb(100, 100, 100));border: 1px solid black; border-radius: 10px;")
        self.ITV_C.setChecked(False)
        self.ITV_C.setObjectName("ITV_C")
        self.output.addWidget(self.ITV_C)
        ITV_control.setCentralWidget(self.centralwidget)

        self.retranslateUi(ITV_control)
        QtCore.QMetaObject.connectSlotsByName(ITV_control)

    def retranslateUi(self, ITV_control):
        _translate = QtCore.QCoreApplication.translate
        ITV_control.setWindowTitle(_translate("ITV_control", "MainWindow"))
        self.quit.setText(_translate("ITV_control", "Quit"))
        self.on.setText(_translate("ITV_control", "HIGH"))
        self.off.setText(_translate("ITV_control", "LOW"))
        self.ITV_A.setText(_translate("ITV_control", " IVT 1 (psi): "))
        self.ITV_B.setText(_translate("ITV_control", " IVT 2 (psi): "))
        self.ITV_C.setText(_translate("ITV_control", " IVT 3 (psi): "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ITV_control = QtWidgets.QMainWindow()
    ui = Ui_ITV_control()
    ui.setupUi(ITV_control)
    ITV_control.show()
    sys.exit(app.exec_())