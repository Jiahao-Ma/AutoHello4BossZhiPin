# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Marko\Desktop\auto_hello\auto_hello_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 281)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 659, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBtn.sizePolicy().hasHeightForWidth())
        self.StartBtn.setSizePolicy(sizePolicy)
        self.StartBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.StartBtn.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 15pt \"等线\";")
        self.StartBtn.setObjectName("StartBtn")
        self.horizontalLayout_3.addWidget(self.StartBtn)
        self.PauseBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PauseBtn.sizePolicy().hasHeightForWidth())
        self.PauseBtn.setSizePolicy(sizePolicy)
        self.PauseBtn.setMinimumSize(QtCore.QSize(80, 20))
        self.PauseBtn.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 15pt \"等线\";")
        self.PauseBtn.setObjectName("PauseBtn")
        self.horizontalLayout_3.addWidget(self.PauseBtn)
        self.NumGreet = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumGreet.sizePolicy().hasHeightForWidth())
        self.NumGreet.setSizePolicy(sizePolicy)
        self.NumGreet.setMinimumSize(QtCore.QSize(0, 20))
        self.NumGreet.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 13pt \"等线\";")
        self.NumGreet.setAlignment(QtCore.Qt.AlignCenter)
        self.NumGreet.setWordWrap(False)
        self.NumGreet.setIndent(0)
        self.NumGreet.setObjectName("NumGreet")
        self.horizontalLayout_3.addWidget(self.NumGreet)
        self.NumGreetSelect = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumGreetSelect.sizePolicy().hasHeightForWidth())
        self.NumGreetSelect.setSizePolicy(sizePolicy)
        self.NumGreetSelect.setMinimumSize(QtCore.QSize(0, 20))
        self.NumGreetSelect.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 8pt \"等线\";\n"
"font: 75 14pt \"等线\";")
        self.NumGreetSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.NumGreetSelect.setDecimals(0)
        self.NumGreetSelect.setMaximum(500.0)
        self.NumGreetSelect.setProperty("value", 400.0)
        self.NumGreetSelect.setObjectName("NumGreetSelect")
        self.horizontalLayout_3.addWidget(self.NumGreetSelect)
        self.Speed = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Speed.sizePolicy().hasHeightForWidth())
        self.Speed.setSizePolicy(sizePolicy)
        self.Speed.setMinimumSize(QtCore.QSize(0, 20))
        self.Speed.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 13pt \"等线\";")
        self.Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed.setWordWrap(False)
        self.Speed.setIndent(0)
        self.Speed.setObjectName("Speed")
        self.horizontalLayout_3.addWidget(self.Speed)
        self.SpeedSelect = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpeedSelect.sizePolicy().hasHeightForWidth())
        self.SpeedSelect.setSizePolicy(sizePolicy)
        self.SpeedSelect.setMinimumSize(QtCore.QSize(0, 20))
        self.SpeedSelect.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 8pt \"等线\";\n"
"font: 75 14pt \"等线\";")
        self.SpeedSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedSelect.setDecimals(2)
        self.SpeedSelect.setMaximum(10.0)
        self.SpeedSelect.setProperty("value", 1.0)
        self.SpeedSelect.setObjectName("SpeedSelect")
        self.horizontalLayout_3.addWidget(self.SpeedSelect)
        self.RandomSpeed = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.RandomSpeed.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 10pt \"等线\";")
        self.RandomSpeed.setChecked(True)
        self.RandomSpeed.setObjectName("RandomSpeed")
        self.horizontalLayout_3.addWidget(self.RandomSpeed)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Browser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.Browser.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 12pt \"等线\";")
        self.Browser.setObjectName("Browser")
        self.horizontalLayout_4.addWidget(self.Browser)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Speed_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Speed_2.sizePolicy().hasHeightForWidth())
        self.Speed_2.setSizePolicy(sizePolicy)
        self.Speed_2.setMinimumSize(QtCore.QSize(0, 20))
        self.Speed_2.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 13pt \"等线\";")
        self.Speed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed_2.setWordWrap(False)
        self.Speed_2.setIndent(0)
        self.Speed_2.setObjectName("Speed_2")
        self.verticalLayout_2.addWidget(self.Speed_2)
        self.TargetWin = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.TargetWin.sizePolicy().hasHeightForWidth())
        self.TargetWin.setSizePolicy(sizePolicy)
        self.TargetWin.setMinimumSize(QtCore.QSize(30, 30))
        self.TargetWin.setMaximumSize(QtCore.QSize(300, 250))
        self.TargetWin.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 12pt \"等线\";")
        self.TargetWin.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TargetWin.setAlignment(QtCore.Qt.AlignCenter)
        self.TargetWin.setObjectName("TargetWin")
        self.verticalLayout_2.addWidget(self.TargetWin)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ScreenShotBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScreenShotBtn.sizePolicy().hasHeightForWidth())
        self.ScreenShotBtn.setSizePolicy(sizePolicy)
        self.ScreenShotBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.ScreenShotBtn.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 12pt \"等线\";")
        self.ScreenShotBtn.setObjectName("ScreenShotBtn")
        self.horizontalLayout_2.addWidget(self.ScreenShotBtn)
        self.DefaultBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DefaultBtn.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 12pt \"等线\";")
        self.DefaultBtn.setObjectName("DefaultBtn")
        self.horizontalLayout_2.addWidget(self.DefaultBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Comment1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comment1.sizePolicy().hasHeightForWidth())
        self.Comment1.setSizePolicy(sizePolicy)
        self.Comment1.setMinimumSize(QtCore.QSize(0, 20))
        self.Comment1.setStyleSheet("font: 22pt \"黑体\";\n"
"font: 75 11pt \"等线\";")
        self.Comment1.setAlignment(QtCore.Qt.AlignCenter)
        self.Comment1.setWordWrap(False)
        self.Comment1.setIndent(0)
        self.Comment1.setObjectName("Comment1")
        self.verticalLayout.addWidget(self.Comment1)
        self.Comment2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comment2.sizePolicy().hasHeightForWidth())
        self.Comment2.setSizePolicy(sizePolicy)
        self.Comment2.setMinimumSize(QtCore.QSize(0, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Comment2.setPalette(palette)
        self.Comment2.setStyleSheet("font: 22pt \"黑体\";\n"
"text-decoration: underline;\n"
"font: 9pt \"Agency FB\";\n"
"font: 75 11pt \"等线\";\n"
"font: rgb(255, 0, 0);")
        self.Comment2.setAlignment(QtCore.Qt.AlignCenter)
        self.Comment2.setWordWrap(False)
        self.Comment2.setIndent(0)
        self.Comment2.setObjectName("Comment2")
        self.verticalLayout.addWidget(self.Comment2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StartBtn.setText(_translate("Form", "Start"))
        self.PauseBtn.setText(_translate("Form", "Pause"))
        self.NumGreet.setText(_translate("Form", "Num of Greet:"))
        self.Speed.setText(_translate("Form", "Speed:"))
        self.RandomSpeed.setText(_translate("Form", "Random Speed"))
        self.Speed_2.setText(_translate("Form", "Detection Target"))
        self.TargetWin.setText(_translate("Form", "Default Target"))
        self.ScreenShotBtn.setText(_translate("Form", "ScreenShot"))
        self.DefaultBtn.setText(_translate("Form", "Default"))
        self.Comment1.setText(_translate("Form", "If the detection fails, you could select your target by taking a screen shot."))
        self.Comment2.setText(_translate("Form", "[NOTICE] To avoid being identified, detection target has been specially processed!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())