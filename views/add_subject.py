# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/add_subject_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_subject(object):
    def setupUi(self, add_subject):
        add_subject.setObjectName("add_subject")
        add_subject.resize(809, 362)
        add_subject.setMinimumSize(QtCore.QSize(491, 295))
        self.gridLayout = QtWidgets.QGridLayout(add_subject)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(add_subject)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.group_num_lbl = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.group_num_lbl.setFont(font)
        self.group_num_lbl.setObjectName("group_num_lbl")
        self.verticalLayout.addWidget(self.group_num_lbl)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.subject_name_lbl = QtWidgets.QTextEdit(self.groupBox)
        self.subject_name_lbl.setMaximumSize(QtCore.QSize(256, 27))
        self.subject_name_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.subject_name_lbl.setAutoFillBackground(False)
        self.subject_name_lbl.setObjectName("subject_name_lbl")
        self.verticalLayout_2.addWidget(self.subject_name_lbl)
        self.group_num_lbl_2 = QtWidgets.QTextEdit(self.groupBox)
        self.group_num_lbl_2.setMaximumSize(QtCore.QSize(256, 27))
        self.group_num_lbl_2.setObjectName("group_num_lbl_2")
        self.verticalLayout_2.addWidget(self.group_num_lbl_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(262, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 6, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(284, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lec_day_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.lec_day_comp_box.setMinimumSize(QtCore.QSize(70, 0))
        self.lec_day_comp_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lec_day_comp_box.setModelColumn(0)
        self.lec_day_comp_box.setObjectName("lec_day_comp_box")
        self.lec_day_comp_box.addItem("")
        self.lec_day_comp_box.addItem("")
        self.lec_day_comp_box.addItem("")
        self.lec_day_comp_box.addItem("")
        self.lec_day_comp_box.addItem("")
        self.horizontalLayout_2.addWidget(self.lec_day_comp_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(312, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 5, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.strt_lec_priod_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.strt_lec_priod_comp_box.setMinimumSize(QtCore.QSize(60, 0))
        self.strt_lec_priod_comp_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.strt_lec_priod_comp_box.setObjectName("strt_lec_priod_comp_box")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.strt_lec_priod_comp_box.addItem("")
        self.horizontalLayout_5.addWidget(self.strt_lec_priod_comp_box)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.end_lec_priod_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.end_lec_priod_comp_box.setMinimumSize(QtCore.QSize(60, 0))
        self.end_lec_priod_comp_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.end_lec_priod_comp_box.setObjectName("end_lec_priod_comp_box")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.end_lec_priod_comp_box.addItem("")
        self.horizontalLayout_5.addWidget(self.end_lec_priod_comp_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 2, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(262, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 6, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(235, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.sec_day_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.sec_day_comp_box.setMinimumSize(QtCore.QSize(70, 0))
        self.sec_day_comp_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sec_day_comp_box.setModelColumn(0)
        self.sec_day_comp_box.setObjectName("sec_day_comp_box")
        self.sec_day_comp_box.addItem("")
        self.sec_day_comp_box.addItem("")
        self.sec_day_comp_box.addItem("")
        self.sec_day_comp_box.addItem("")
        self.sec_day_comp_box.addItem("")
        self.horizontalLayout_6.addWidget(self.sec_day_comp_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 3, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(312, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 5, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.strt_sec_priod_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.strt_sec_priod_comp_box.setMinimumSize(QtCore.QSize(60, 0))
        self.strt_sec_priod_comp_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.strt_sec_priod_comp_box.setObjectName("strt_sec_priod_comp_box")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.strt_sec_priod_comp_box.addItem("")
        self.horizontalLayout_7.addWidget(self.strt_sec_priod_comp_box)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.end_sec_priod_comp_box = QtWidgets.QComboBox(self.groupBox)
        self.end_sec_priod_comp_box.setMinimumSize(QtCore.QSize(60, 0))
        self.end_sec_priod_comp_box.setObjectName("end_sec_priod_comp_box")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.end_sec_priod_comp_box.addItem("")
        self.horizontalLayout_7.addWidget(self.end_sec_priod_comp_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 4, 2, 1, 4)
        spacerItem9 = QtWidgets.QSpacerItem(262, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 4, 6, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(17, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 5, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.clear_btn = QtWidgets.QPushButton(self.groupBox)
        self.clear_btn.setMinimumSize(QtCore.QSize(120, 34))
        self.clear_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons8-remove-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon)
        self.clear_btn.setIconSize(QtCore.QSize(20, 22))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_8.addWidget(self.clear_btn)
        self.add_grp_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_grp_btn.setMinimumSize(QtCore.QSize(120, 34))
        self.add_grp_btn.setObjectName("add_grp_btn")
        self.horizontalLayout_8.addWidget(self.add_grp_btn)
        self.register_btn = QtWidgets.QPushButton(self.groupBox)
        self.register_btn.setMinimumSize(QtCore.QSize(120, 34))
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout_8.addWidget(self.register_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 6, 1, 1, 6)
        spacerItem12 = QtWidgets.QSpacerItem(244, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 6, 7, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(17, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 7, 4, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(add_subject)
        self.clear_btn.clicked.connect(self.subject_name_lbl.clear)
        self.clear_btn.clicked.connect(self.group_num_lbl_2.clear)
        QtCore.QMetaObject.connectSlotsByName(add_subject)

    def retranslateUi(self, add_subject):
        _translate = QtCore.QCoreApplication.translate
        add_subject.setWindowTitle(_translate("add_subject", "HTI Table Generator"))
        self.groupBox.setTitle(_translate("add_subject", "Add New Subject"))
        self.label.setText(_translate("add_subject", "Subject Name"))
        self.group_num_lbl.setText(_translate("add_subject", "Group "))
        self.subject_name_lbl.setPlaceholderText(_translate("add_subject", "?????????? ??????????????"))
        self.group_num_lbl_2.setPlaceholderText(_translate("add_subject", "G4"))
        self.label_3.setText(_translate("add_subject", "Lecture Day"))
        self.lec_day_comp_box.setItemText(0, _translate("add_subject", "Saturday"))
        self.lec_day_comp_box.setItemText(1, _translate("add_subject", "Sunday"))
        self.lec_day_comp_box.setItemText(2, _translate("add_subject", "Monday"))
        self.lec_day_comp_box.setItemText(3, _translate("add_subject", "Tuesday"))
        self.lec_day_comp_box.setItemText(4, _translate("add_subject", "Wednesday"))
        self.label_4.setText(_translate("add_subject", "Lecture period"))
        self.label_5.setText(_translate("add_subject", "from"))
        self.strt_lec_priod_comp_box.setItemText(0, _translate("add_subject", "1"))
        self.strt_lec_priod_comp_box.setItemText(1, _translate("add_subject", "2"))
        self.strt_lec_priod_comp_box.setItemText(2, _translate("add_subject", "3"))
        self.strt_lec_priod_comp_box.setItemText(3, _translate("add_subject", "4"))
        self.strt_lec_priod_comp_box.setItemText(4, _translate("add_subject", "5"))
        self.strt_lec_priod_comp_box.setItemText(5, _translate("add_subject", "6"))
        self.strt_lec_priod_comp_box.setItemText(6, _translate("add_subject", "7"))
        self.label_6.setText(_translate("add_subject", "to"))
        self.end_lec_priod_comp_box.setItemText(0, _translate("add_subject", "1"))
        self.end_lec_priod_comp_box.setItemText(1, _translate("add_subject", "2"))
        self.end_lec_priod_comp_box.setItemText(2, _translate("add_subject", "3"))
        self.end_lec_priod_comp_box.setItemText(3, _translate("add_subject", "4"))
        self.end_lec_priod_comp_box.setItemText(4, _translate("add_subject", "5"))
        self.end_lec_priod_comp_box.setItemText(5, _translate("add_subject", "6"))
        self.end_lec_priod_comp_box.setItemText(6, _translate("add_subject", "7"))
        self.end_lec_priod_comp_box.setItemText(7, _translate("add_subject", "8"))
        self.label_7.setText(_translate("add_subject", "Section Period"))
        self.sec_day_comp_box.setItemText(0, _translate("add_subject", "Saturday"))
        self.sec_day_comp_box.setItemText(1, _translate("add_subject", "Sunday"))
        self.sec_day_comp_box.setItemText(2, _translate("add_subject", "Monday"))
        self.sec_day_comp_box.setItemText(3, _translate("add_subject", "Tuesday"))
        self.sec_day_comp_box.setItemText(4, _translate("add_subject", "Wednesday"))
        self.label_8.setText(_translate("add_subject", "Sections Period"))
        self.label_9.setText(_translate("add_subject", "From"))
        self.strt_sec_priod_comp_box.setItemText(0, _translate("add_subject", "1"))
        self.strt_sec_priod_comp_box.setItemText(1, _translate("add_subject", "2"))
        self.strt_sec_priod_comp_box.setItemText(2, _translate("add_subject", "3"))
        self.strt_sec_priod_comp_box.setItemText(3, _translate("add_subject", "4"))
        self.strt_sec_priod_comp_box.setItemText(4, _translate("add_subject", "5"))
        self.strt_sec_priod_comp_box.setItemText(5, _translate("add_subject", "6"))
        self.strt_sec_priod_comp_box.setItemText(6, _translate("add_subject", "7"))
        self.label_10.setText(_translate("add_subject", "to"))
        self.end_sec_priod_comp_box.setItemText(0, _translate("add_subject", "1"))
        self.end_sec_priod_comp_box.setItemText(1, _translate("add_subject", "2"))
        self.end_sec_priod_comp_box.setItemText(2, _translate("add_subject", "3"))
        self.end_sec_priod_comp_box.setItemText(3, _translate("add_subject", "4"))
        self.end_sec_priod_comp_box.setItemText(4, _translate("add_subject", "5"))
        self.end_sec_priod_comp_box.setItemText(5, _translate("add_subject", "6"))
        self.end_sec_priod_comp_box.setItemText(6, _translate("add_subject", "7"))
        self.end_sec_priod_comp_box.setItemText(7, _translate("add_subject", "8"))
        self.clear_btn.setText(_translate("add_subject", "clear"))
        self.add_grp_btn.setText(_translate("add_subject", "Add new group "))
        self.register_btn.setText(_translate("add_subject", "Register"))
import app_resources_rc
