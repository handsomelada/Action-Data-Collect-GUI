# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(2014, 1180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("西大图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.View1Groupbox = QtWidgets.QGroupBox(self.groupBox_3)
        self.View1Groupbox.setObjectName("View1Groupbox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.View1Groupbox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.View_1 = QtWidgets.QLabel(self.View1Groupbox)
        self.View_1.setText("")
        self.View_1.setObjectName("View_1")
        self.verticalLayout_7.addWidget(self.View_1)
        self.horizontalLayout_2.addWidget(self.View1Groupbox)
        self.View2Groupbox = QtWidgets.QGroupBox(self.groupBox_3)
        self.View2Groupbox.setObjectName("View2Groupbox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.View2Groupbox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.View_2 = QtWidgets.QLabel(self.View2Groupbox)
        self.View_2.setText("")
        self.View_2.setObjectName("View_2")
        self.verticalLayout_8.addWidget(self.View_2)
        self.horizontalLayout_2.addWidget(self.View2Groupbox)
        self.View3Groupbox = QtWidgets.QGroupBox(self.groupBox_3)
        self.View3Groupbox.setObjectName("View3Groupbox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.View3Groupbox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.View_3 = QtWidgets.QLabel(self.View3Groupbox)
        self.View_3.setText("")
        self.View_3.setObjectName("View_3")
        self.verticalLayout_9.addWidget(self.View_3)
        self.horizontalLayout_2.addWidget(self.View3Groupbox)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.OpenCamButton = QtWidgets.QPushButton(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenCamButton.sizePolicy().hasHeightForWidth())
        self.OpenCamButton.setSizePolicy(sizePolicy)
        self.OpenCamButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.OpenCamButton.setObjectName("OpenCamButton")
        self.horizontalLayout_8.addWidget(self.OpenCamButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.ShownSizebox = QtWidgets.QComboBox(self.groupBox_9)
        self.ShownSizebox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ShownSizebox.setObjectName("ShownSizebox")
        self.ShownSizebox.addItem("")
        self.ShownSizebox.addItem("")
        self.horizontalLayout_6.addWidget(self.ShownSizebox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.FrameLabel = QtWidgets.QLabel(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameLabel.sizePolicy().hasHeightForWidth())
        self.FrameLabel.setSizePolicy(sizePolicy)
        self.FrameLabel.setObjectName("FrameLabel")
        self.horizontalLayout_12.addWidget(self.FrameLabel)
        self.FrameEditLine = QtWidgets.QLineEdit(self.groupBox_10)
        self.FrameEditLine.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameEditLine.sizePolicy().hasHeightForWidth())
        self.FrameEditLine.setSizePolicy(sizePolicy)
        self.FrameEditLine.setMaximumSize(QtCore.QSize(50, 16777215))
        self.FrameEditLine.setObjectName("FrameEditLine")
        self.horizontalLayout_12.addWidget(self.FrameEditLine)
        self.horizontalLayout_12.setStretch(0, 5)
        self.horizontalLayout_12.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.SavePathLabel = QtWidgets.QLabel(self.groupBox_10)
        self.SavePathLabel.setObjectName("SavePathLabel")
        self.horizontalLayout_13.addWidget(self.SavePathLabel)
        self.ShowPathButton = QtWidgets.QToolButton(self.groupBox_10)
        self.ShowPathButton.setObjectName("ShowPathButton")
        self.horizontalLayout_13.addWidget(self.ShowPathButton)
        self.PathOpenButton = QtWidgets.QPushButton(self.groupBox_10)
        self.PathOpenButton.setObjectName("PathOpenButton")
        self.horizontalLayout_13.addWidget(self.PathOpenButton)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.verticalLayout_4.addWidget(self.groupBox_10)
        self.verticalLayout_4.setStretch(0, 8)
        self.verticalLayout_4.setStretch(1, 8)
        self.horizontalLayout_14.addLayout(self.verticalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_11.setSpacing(1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.SceneLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SceneLabel.sizePolicy().hasHeightForWidth())
        self.SceneLabel.setSizePolicy(sizePolicy)
        self.SceneLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.SceneLabel.setObjectName("SceneLabel")
        self.horizontalLayout_11.addWidget(self.SceneLabel)
        self.SceneChosenBox = QtWidgets.QComboBox(self.groupBox_2)
        self.SceneChosenBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SceneChosenBox.setObjectName("SceneChosenBox")
        self.SceneChosenBox.addItem("")
        self.SceneChosenBox.addItem("")
        self.SceneChosenBox.addItem("")
        self.horizontalLayout_11.addWidget(self.SceneChosenBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_17.setSpacing(1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.SizeSettingLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SizeSettingLabel.sizePolicy().hasHeightForWidth())
        self.SizeSettingLabel.setSizePolicy(sizePolicy)
        self.SizeSettingLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.SizeSettingLabel.setObjectName("SizeSettingLabel")
        self.horizontalLayout_17.addWidget(self.SizeSettingLabel)
        self.SizeSetChosenBox = QtWidgets.QComboBox(self.groupBox_2)
        self.SizeSetChosenBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SizeSetChosenBox.setObjectName("SizeSetChosenBox")
        self.SizeSetChosenBox.addItem("")
        self.SizeSetChosenBox.addItem("")
        self.SizeSetChosenBox.addItem("")
        self.SizeSetChosenBox.addItem("")
        self.SizeSetChosenBox.addItem("")
        self.SizeSetChosenBox.addItem("")
        self.horizontalLayout_17.addWidget(self.SizeSetChosenBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.IDLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDLabel.sizePolicy().hasHeightForWidth())
        self.IDLabel.setSizePolicy(sizePolicy)
        self.IDLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.IDLabel.setObjectName("IDLabel")
        self.horizontalLayout_10.addWidget(self.IDLabel)
        self.ID_EditLine = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID_EditLine.sizePolicy().hasHeightForWidth())
        self.ID_EditLine.setSizePolicy(sizePolicy)
        self.ID_EditLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ID_EditLine.setObjectName("ID_EditLine")
        self.horizontalLayout_10.addWidget(self.ID_EditLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_15.setSpacing(1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.RepetLabel = QtWidgets.QLabel(self.groupBox_2)
        self.RepetLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.RepetLabel.setObjectName("RepetLabel")
        self.horizontalLayout_15.addWidget(self.RepetLabel)
        self.Repet_EditLine = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Repet_EditLine.sizePolicy().hasHeightForWidth())
        self.Repet_EditLine.setSizePolicy(sizePolicy)
        self.Repet_EditLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Repet_EditLine.setObjectName("Repet_EditLine")
        self.horizontalLayout_15.addWidget(self.Repet_EditLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ActionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.ActionLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ActionLabel.setObjectName("ActionLabel")
        self.horizontalLayout_9.addWidget(self.ActionLabel)
        self.ActionEditLine = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ActionEditLine.sizePolicy().hasHeightForWidth())
        self.ActionEditLine.setSizePolicy(sizePolicy)
        self.ActionEditLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ActionEditLine.setObjectName("ActionEditLine")
        self.horizontalLayout_9.addWidget(self.ActionEditLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.SignupButton = QtWidgets.QPushButton(self.groupBox_2)
        self.SignupButton.setObjectName("SignupButton")
        self.horizontalLayout_7.addWidget(self.SignupButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.DeleteButton = QtWidgets.QPushButton(self.groupBox_2)
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout_7.addWidget(self.DeleteButton)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StartCollectButton = QtWidgets.QPushButton(self.groupBox_2)
        self.StartCollectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.StartCollectButton.setObjectName("StartCollectButton")
        self.horizontalLayout_4.addWidget(self.StartCollectButton)
        self.EndCollectButton = QtWidgets.QPushButton(self.groupBox_2)
        self.EndCollectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.EndCollectButton.setObjectName("EndCollectButton")
        self.horizontalLayout_4.addWidget(self.EndCollectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ProgressLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.ProgressLabel_2.setObjectName("ProgressLabel_2")
        self.horizontalLayout_5.addWidget(self.ProgressLabel_2)
        self.ShowCollectTime = QtWidgets.QLabel(self.groupBox_2)
        self.ShowCollectTime.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowCollectTime.sizePolicy().hasHeightForWidth())
        self.ShowCollectTime.setSizePolicy(sizePolicy)
        self.ShowCollectTime.setStyleSheet("QLabel{\n"
"color:rgb(255, 0, 0)\n"
"}")
        self.ShowCollectTime.setObjectName("ShowCollectTime")
        self.horizontalLayout_5.addWidget(self.ShowCollectTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProgressLabel = QtWidgets.QLabel(self.groupBox_2)
        self.ProgressLabel.setObjectName("ProgressLabel")
        self.horizontalLayout.addWidget(self.ProgressLabel)
        self.ShowCollectStatus = QtWidgets.QLabel(self.groupBox_2)
        self.ShowCollectStatus.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowCollectStatus.sizePolicy().hasHeightForWidth())
        self.ShowCollectStatus.setSizePolicy(sizePolicy)
        self.ShowCollectStatus.setStyleSheet("QLabel{\n"
"color:rgb(255, 0, 0)\n"
"}")
        self.ShowCollectStatus.setObjectName("ShowCollectStatus")
        self.horizontalLayout.addWidget(self.ShowCollectStatus)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 5)
        self.verticalLayout_2.setStretch(6, 4)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 1)
        self.horizontalLayout_14.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_6.addWidget(self.plainTextEdit)
        self.horizontalLayout_14.addWidget(self.groupBox)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Annotation = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Annotation.sizePolicy().hasHeightForWidth())
        self.Annotation.setSizePolicy(sizePolicy)
        self.Annotation.setObjectName("Annotation")
        self.horizontalLayout_3.addWidget(self.Annotation)
        self.horizontalLayout_14.addWidget(self.groupBox_8)
        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 4)
        self.horizontalLayout_14.setStretch(2, 8)
        self.horizontalLayout_14.setStretch(3, 6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(mainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(mainWindow)
        self.actionclose.setObjectName("actionclose")

        self.retranslateUi(mainWindow)
        self.SignupButton.clicked['bool'].connect(self.ActionEditLine.setEnabled)
        self.SignupButton.clicked['bool'].connect(self.ID_EditLine.setEnabled)
        self.SignupButton.clicked['bool'].connect(self.SceneChosenBox.setEnabled)
        self.DeleteButton.clicked['bool'].connect(self.ActionEditLine.setDisabled)
        self.DeleteButton.clicked['bool'].connect(self.ID_EditLine.setDisabled)
        self.DeleteButton.clicked['bool'].connect(self.SceneChosenBox.setDisabled)
        self.DeleteButton.clicked['bool'].connect(self.ActionEditLine.clear)
        self.DeleteButton.clicked['bool'].connect(self.ID_EditLine.clear)
        self.SignupButton.clicked['bool'].connect(self.Repet_EditLine.setEnabled)
        self.DeleteButton.clicked['bool'].connect(self.Repet_EditLine.setDisabled)
        self.DeleteButton.clicked['bool'].connect(self.Repet_EditLine.clear)
        self.EndCollectButton.clicked['bool'].connect(self.ActionEditLine.setDisabled)
        self.EndCollectButton.clicked['bool'].connect(self.Repet_EditLine.setDisabled)
        self.EndCollectButton.clicked['bool'].connect(self.ID_EditLine.setDisabled)
        self.EndCollectButton.clicked['bool'].connect(self.SceneChosenBox.setDisabled)
        self.SignupButton.clicked['bool'].connect(self.SizeSetChosenBox.setEnabled)
        self.DeleteButton.clicked['bool'].connect(self.SizeSetChosenBox.setDisabled)
        self.EndCollectButton.clicked['bool'].connect(self.SizeSetChosenBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "毕设数据采集"))
        self.groupBox_3.setTitle(_translate("mainWindow", "RGB相机"))
        self.View1Groupbox.setTitle(_translate("mainWindow", "视角1"))
        self.View2Groupbox.setTitle(_translate("mainWindow", "视角2"))
        self.View3Groupbox.setTitle(_translate("mainWindow", "视角3"))
        self.groupBox_9.setTitle(_translate("mainWindow", "1.摄像头操作"))
        self.OpenCamButton.setText(_translate("mainWindow", "打开摄像头"))
        self.label.setText(_translate("mainWindow", "界面视角显示大小："))
        self.ShownSizebox.setItemText(0, _translate("mainWindow", "640*480"))
        self.ShownSizebox.setItemText(1, _translate("mainWindow", "400*300"))
        self.groupBox_10.setTitle(_translate("mainWindow", "2.设置"))
        self.FrameLabel.setText(_translate("mainWindow", "采样帧数"))
        self.SavePathLabel.setText(_translate("mainWindow", "存储路径"))
        self.ShowPathButton.setText(_translate("mainWindow", "..."))
        self.PathOpenButton.setText(_translate("mainWindow", "选择"))
        self.groupBox_2.setTitle(_translate("mainWindow", "3.用户注册"))
        self.SceneLabel.setText(_translate("mainWindow", "采集场景"))
        self.SceneChosenBox.setItemText(0, _translate("mainWindow", "S001"))
        self.SceneChosenBox.setItemText(1, _translate("mainWindow", "S002"))
        self.SceneChosenBox.setItemText(2, _translate("mainWindow", "S003"))
        self.SizeSettingLabel.setText(_translate("mainWindow", "尺寸设置"))
        self.SizeSetChosenBox.setItemText(0, _translate("mainWindow", "E001"))
        self.SizeSetChosenBox.setItemText(1, _translate("mainWindow", "E002"))
        self.SizeSetChosenBox.setItemText(2, _translate("mainWindow", "E003"))
        self.SizeSetChosenBox.setItemText(3, _translate("mainWindow", "E004"))
        self.SizeSetChosenBox.setItemText(4, _translate("mainWindow", "E005"))
        self.SizeSetChosenBox.setItemText(5, _translate("mainWindow", "E006"))
        self.IDLabel.setText(_translate("mainWindow", "人员编号"))
        self.RepetLabel.setText(_translate("mainWindow", "重复次数"))
        self.ActionLabel.setText(_translate("mainWindow", "采集动作"))
        self.SignupButton.setText(_translate("mainWindow", "注册用户"))
        self.DeleteButton.setText(_translate("mainWindow", "删除用户"))
        self.StartCollectButton.setText(_translate("mainWindow", "开始采集"))
        self.EndCollectButton.setText(_translate("mainWindow", "结束采集"))
        self.ProgressLabel_2.setText(_translate("mainWindow", "采集时间"))
        self.ShowCollectTime.setText(_translate("mainWindow", "0.00秒"))
        self.ProgressLabel.setText(_translate("mainWindow", "采集文件检查"))
        self.ShowCollectStatus.setText(_translate("mainWindow", "采集未开始"))
        self.groupBox.setTitle(_translate("mainWindow", "采集说明"))
        self.plainTextEdit.setPlainText(_translate("mainWindow", "1.先打开摄像头查看摄像头是否运行正常；\n"
"2.设置采样帧数与文件存储路径；\n"
"3.点击用户注册后开始采集；\n"
"4.动作完成后点击结束采集"))
        self.groupBox_8.setTitle(_translate("mainWindow", "数据集注释"))
        self.Annotation.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">该数据集采用3个RGB相机，采集人体的RGB图像信息，用于2D人体姿态估计与动作识别。保存视频的RGB图像视频帧命名如下：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">S：采集场景，暂定3个</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C：相机阵列中共有3个相机，因此有C001-C003；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">P：动作执行人员视具体情况而定，暂定10人；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">R：重复动作次数，暂定2次；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A：不同的动作类别，暂定8种车间工人违规动作；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">F：视频帧数索引。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此外，每个视频序列下每一帧RGB图像保存在包含SCPRA文件名前缀的目录下，如S001C001P001R001A001F001.png。</p></body></html>"))
        self.actionopen.setText(_translate("mainWindow", "open"))
        self.actionclose.setText(_translate("mainWindow", "close"))