# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiVideoCut.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 40, 751, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_original = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_original.setText("")
        self.label_original.setObjectName("label_original")
        self.horizontalLayout.addWidget(self.label_original)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_top = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_top.setText("")
        self.label_top.setObjectName("label_top")
        self.verticalLayout_4.addWidget(self.label_top)
        self.label_bottom = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_bottom.setText("")
        self.label_bottom.setObjectName("label_bottom")
        self.verticalLayout_4.addWidget(self.label_bottom)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 510, 211, 161))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 29, 191, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 550, 561, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_openfile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_openfile.setObjectName("button_openfile")
        self.horizontalLayout_2.addWidget(self.button_openfile)
        self.button_begin = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_begin.setObjectName("button_begin")
        self.horizontalLayout_2.addWidget(self.button_begin)
        self.button_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_2.addWidget(self.button_cancel)
        self.icd_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.icd_time.setGeometry(QtCore.QRect(410, 470, 171, 61))
        self.icd_time.setObjectName("icd_time")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 240, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(870, 130, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(870, 350, 71, 20))
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(400, 650, 341, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 490, 41, 20))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VideoCut"))
        self.groupBox.setTitle(_translate("MainWindow", "步骤："))
        self.label.setText(_translate("MainWindow", "step1:打开文件"))
        self.label_2.setText(_translate("MainWindow", "step2：开始分割"))
        self.label_3.setText(_translate("MainWindow", "step3：等待至处理结束"))
        self.label_4.setText(_translate("MainWindow", "step4：关闭窗口"))
        self.button_openfile.setText(_translate("MainWindow", "打开文件"))
        self.button_begin.setText(_translate("MainWindow", "开始分割"))
        self.button_cancel.setText(_translate("MainWindow", "关闭"))
        self.label_8.setText(_translate("MainWindow", "原视频"))
        self.label_9.setText(_translate("MainWindow", "上半部分"))
        self.label_10.setText(_translate("MainWindow", "下半部分"))
        self.label_7.setText(_translate("MainWindow", "视频分割 v1.0"))
        self.label_5.setText(_translate("MainWindow", "Author @ LIN"))
        self.label_6.setText(_translate("MainWindow", "2018/04/13"))
        self.label_11.setText(_translate("MainWindow", "计时："))
