# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardaz_app.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cardaz_app(object):
    def setupUi(self, cardaz_app):
        cardaz_app.setObjectName("cardaz_app")
        cardaz_app.resize(695, 375)
        cardaz_app.setAcceptDrops(False)
        self.centralWidget = QtWidgets.QWidget(cardaz_app)
        self.centralWidget.setObjectName("centralWidget")
        self.form_tabcontrol = QtWidgets.QStackedWidget(self.centralWidget)
        self.form_tabcontrol.setGeometry(QtCore.QRect(0, 20, 691, 331))
        self.form_tabcontrol.setObjectName("form_tabcontrol")
        self.login_form = QtWidgets.QWidget()
        self.login_form.setObjectName("login_form")
        self.label = QtWidgets.QLabel(self.login_form)
        self.label.setGeometry(QtCore.QRect(200, 100, 271, 21))
        self.label.setObjectName("label")
        self.yesacc_BTN = QtWidgets.QPushButton(self.login_form)
        self.yesacc_BTN.setGeometry(QtCore.QRect(150, 180, 91, 29))
        self.yesacc_BTN.setObjectName("yesacc_BTN")
        self.noacc_BTN = QtWidgets.QPushButton(self.login_form)
        self.noacc_BTN.setGeometry(QtCore.QRect(450, 180, 91, 29))
        self.noacc_BTN.setObjectName("noacc_BTN")
        self.testformBTN = QtWidgets.QPushButton(self.login_form)
        self.testformBTN.setGeometry(QtCore.QRect(310, 250, 91, 29))
        self.testformBTN.setObjectName("testformBTN")
        self.form_tabcontrol.addWidget(self.login_form)
        self.P_info_form = QtWidgets.QWidget()
        self.P_info_form.setObjectName("P_info_form")
        self.first_name_TB = QtWidgets.QLineEdit(self.P_info_form)
        self.first_name_TB.setGeometry(QtCore.QRect(110, 30, 161, 21))
        self.first_name_TB.setObjectName("first_name_TB")
        self.fname_label = QtWidgets.QLabel(self.P_info_form)
        self.fname_label.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.fname_label.setObjectName("fname_label")
        self.last_name_TB = QtWidgets.QLineEdit(self.P_info_form)
        self.last_name_TB.setGeometry(QtCore.QRect(390, 30, 161, 21))
        self.last_name_TB.setObjectName("last_name_TB")
        self.lname_label = QtWidgets.QLabel(self.P_info_form)
        self.lname_label.setGeometry(QtCore.QRect(290, 30, 91, 21))
        self.lname_label.setObjectName("lname_label")
        self.mi_TB = QtWidgets.QLineEdit(self.P_info_form)
        self.mi_TB.setGeometry(QtCore.QRect(620, 30, 41, 21))
        self.mi_TB.setObjectName("mi_TB")
        self.mi_label = QtWidgets.QLabel(self.P_info_form)
        self.mi_label.setGeometry(QtCore.QRect(590, 30, 31, 21))
        self.mi_label.setObjectName("mi_label")
        self.phone_TB = QtWidgets.QLineEdit(self.P_info_form)
        self.phone_TB.setGeometry(QtCore.QRect(110, 60, 131, 21))
        self.phone_TB.setObjectName("phone_TB")
        self.phone_Label = QtWidgets.QLabel(self.P_info_form)
        self.phone_Label.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.phone_Label.setObjectName("phone_Label")
        self.zipcode_Label = QtWidgets.QLabel(self.P_info_form)
        self.zipcode_Label.setGeometry(QtCore.QRect(490, 150, 71, 21))
        self.zipcode_Label.setObjectName("zipcode_Label")
        self.street_Label = QtWidgets.QLabel(self.P_info_form)
        self.street_Label.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.street_Label.setObjectName("street_Label")
        self.state_Label = QtWidgets.QLabel(self.P_info_form)
        self.state_Label.setGeometry(QtCore.QRect(270, 150, 41, 21))
        self.state_Label.setObjectName("state_Label")
        self.phone_TB_2 = QtWidgets.QLineEdit(self.P_info_form)
        self.phone_TB_2.setGeometry(QtCore.QRect(570, 150, 91, 21))
        self.phone_TB_2.setObjectName("phone_TB_2")
        self.city_Label = QtWidgets.QLabel(self.P_info_form)
        self.city_Label.setGeometry(QtCore.QRect(80, 150, 31, 21))
        self.city_Label.setObjectName("city_Label")
        self.street_TB = QtWidgets.QLineEdit(self.P_info_form)
        self.street_TB.setGeometry(QtCore.QRect(130, 120, 531, 21))
        self.street_TB.setObjectName("street_TB")
        self.state_CB = QtWidgets.QComboBox(self.P_info_form)
        self.state_CB.setGeometry(QtCore.QRect(320, 150, 161, 21))
        self.state_CB.setEditable(True)
        self.state_CB.setObjectName("state_CB")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.state_CB.addItem("")
        self.street_TB_2 = QtWidgets.QLineEdit(self.P_info_form)
        self.street_TB_2.setGeometry(QtCore.QRect(130, 150, 121, 21))
        self.street_TB_2.setObjectName("street_TB_2")
        self.titlelLabel = QtWidgets.QLabel(self.P_info_form)
        self.titlelLabel.setGeometry(QtCore.QRect(250, 0, 181, 16))
        self.titlelLabel.setObjectName("titlelLabel")
        self.execute_BTN = QtWidgets.QPushButton(self.P_info_form)
        self.execute_BTN.setGeometry(QtCore.QRect(550, 220, 91, 29))
        self.execute_BTN.setObjectName("execute_BTN")
        self.form_tabcontrol.addWidget(self.P_info_form)
        self.select_account = QtWidgets.QWidget()
        self.select_account.setObjectName("select_account")
        self.listWidget = QtWidgets.QListWidget(self.select_account)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 641, 201))
        self.listWidget.setObjectName("listWidget")
        self.start_info_Label = QtWidgets.QLabel(self.select_account)
        self.start_info_Label.setGeometry(QtCore.QRect(130, 20, 411, 21))
        self.start_info_Label.setObjectName("start_info_Label")
        self.ready_BTN = QtWidgets.QPushButton(self.select_account)
        self.ready_BTN.setGeometry(QtCore.QRect(570, 250, 91, 29))
        self.ready_BTN.setObjectName("ready_BTN")
        self.form_tabcontrol.addWidget(self.select_account)
        self.hgraph = QtWidgets.QWidget()
        self.hgraph.setObjectName("hgraph")
        self.back_BTN = QtWidgets.QPushButton(self.hgraph)
        self.back_BTN.setGeometry(QtCore.QRect(40, 0, 91, 29))
        self.back_BTN.setObjectName("back_BTN")
        self.heart_graph = PlotWidget(self.hgraph)
        self.heart_graph.setGeometry(QtCore.QRect(10, 30, 671, 281))
        self.heart_graph.setObjectName("heart_graph")
        self.form_tabcontrol.addWidget(self.hgraph)
        self.testpsql = QtWidgets.QWidget()
        self.testpsql.setObjectName("testpsql")
        self.sBTN = QtWidgets.QPushButton(self.testpsql)
        self.sBTN.setGeometry(QtCore.QRect(30, 40, 91, 29))
        self.sBTN.setObjectName("sBTN")
        self.s1BTN = QtWidgets.QPushButton(self.testpsql)
        self.s1BTN.setGeometry(QtCore.QRect(30, 80, 91, 29))
        self.s1BTN.setObjectName("s1BTN")
        self.sfilterBTN = QtWidgets.QPushButton(self.testpsql)
        self.sfilterBTN.setGeometry(QtCore.QRect(30, 120, 91, 29))
        self.sfilterBTN.setObjectName("sfilterBTN")
        self.insBTN = QtWidgets.QPushButton(self.testpsql)
        self.insBTN.setGeometry(QtCore.QRect(30, 160, 91, 29))
        self.insBTN.setObjectName("insBTN")
        self.upBTN = QtWidgets.QPushButton(self.testpsql)
        self.upBTN.setGeometry(QtCore.QRect(30, 200, 91, 29))
        self.upBTN.setObjectName("upBTN")
        self.exitBTN = QtWidgets.QPushButton(self.testpsql)
        self.exitBTN.setGeometry(QtCore.QRect(500, 40, 111, 29))
        self.exitBTN.setObjectName("exitBTN")
        self.remBTN = QtWidgets.QPushButton(self.testpsql)
        self.remBTN.setGeometry(QtCore.QRect(30, 240, 91, 29))
        self.remBTN.setObjectName("remBTN")
        self.form_tabcontrol.addWidget(self.testpsql)
        cardaz_app.setCentralWidget(self.centralWidget)

        self.retranslateUi(cardaz_app)
        self.form_tabcontrol.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(cardaz_app)

    def retranslateUi(self, cardaz_app):
        _translate = QtCore.QCoreApplication.translate
        cardaz_app.setWindowTitle(_translate("cardaz_app", "cardaz_app"))
        self.label.setText(_translate("cardaz_app", "Do you have a record with us aleady?"))
        self.yesacc_BTN.setText(_translate("cardaz_app", "Yes"))
        self.noacc_BTN.setText(_translate("cardaz_app", "No"))
        self.testformBTN.setText(_translate("cardaz_app", "Test Form"))
        self.fname_label.setText(_translate("cardaz_app", "<html><head/><body><p>First Name:</p></body></html>"))
        self.lname_label.setText(_translate("cardaz_app", "<html><head/><body><p>Last Name:</p></body></html>"))
        self.mi_label.setText(_translate("cardaz_app", "mi:"))
        self.phone_Label.setText(_translate("cardaz_app", "Phone#: "))
        self.zipcode_Label.setText(_translate("cardaz_app", "Zip Code:"))
        self.street_Label.setText(_translate("cardaz_app", "Street Address:"))
        self.state_Label.setText(_translate("cardaz_app", "State:"))
        self.city_Label.setText(_translate("cardaz_app", "City:"))
        self.state_CB.setItemText(0, _translate("cardaz_app", "<None>"))
        self.state_CB.setItemText(1, _translate("cardaz_app", "Alabama"))
        self.state_CB.setItemText(2, _translate("cardaz_app", "Alaska"))
        self.state_CB.setItemText(3, _translate("cardaz_app", "Arkansas"))
        self.state_CB.setItemText(4, _translate("cardaz_app", "California"))
        self.state_CB.setItemText(5, _translate("cardaz_app", "Colorado"))
        self.state_CB.setItemText(6, _translate("cardaz_app", "Connecticut"))
        self.state_CB.setItemText(7, _translate("cardaz_app", "Delaware"))
        self.state_CB.setItemText(8, _translate("cardaz_app", "Florida"))
        self.state_CB.setItemText(9, _translate("cardaz_app", "Georgia"))
        self.state_CB.setItemText(10, _translate("cardaz_app", "Hawaii"))
        self.state_CB.setItemText(11, _translate("cardaz_app", "Idaho"))
        self.state_CB.setItemText(12, _translate("cardaz_app", "Illinois"))
        self.state_CB.setItemText(13, _translate("cardaz_app", "Indiana"))
        self.state_CB.setItemText(14, _translate("cardaz_app", "Iowa"))
        self.state_CB.setItemText(15, _translate("cardaz_app", "Kansas"))
        self.state_CB.setItemText(16, _translate("cardaz_app", "Kentucky"))
        self.state_CB.setItemText(17, _translate("cardaz_app", "louisiana"))
        self.state_CB.setItemText(18, _translate("cardaz_app", "Maine"))
        self.state_CB.setItemText(19, _translate("cardaz_app", "Maryland"))
        self.state_CB.setItemText(20, _translate("cardaz_app", "Massachusetts"))
        self.state_CB.setItemText(21, _translate("cardaz_app", "Michigan"))
        self.state_CB.setItemText(22, _translate("cardaz_app", "Minnesota"))
        self.state_CB.setItemText(23, _translate("cardaz_app", "Mississippi"))
        self.state_CB.setItemText(24, _translate("cardaz_app", "Missouri"))
        self.state_CB.setItemText(25, _translate("cardaz_app", "Montana"))
        self.state_CB.setItemText(26, _translate("cardaz_app", "Nebraska"))
        self.state_CB.setItemText(27, _translate("cardaz_app", "Nevada"))
        self.state_CB.setItemText(28, _translate("cardaz_app", "New Hamshire"))
        self.state_CB.setItemText(29, _translate("cardaz_app", "New Jersey"))
        self.state_CB.setItemText(30, _translate("cardaz_app", "New Mexico"))
        self.state_CB.setItemText(31, _translate("cardaz_app", "New York"))
        self.state_CB.setItemText(32, _translate("cardaz_app", "North Carolina"))
        self.state_CB.setItemText(33, _translate("cardaz_app", "North Dakota"))
        self.state_CB.setItemText(34, _translate("cardaz_app", "Ohio"))
        self.state_CB.setItemText(35, _translate("cardaz_app", "Oklahoma"))
        self.state_CB.setItemText(36, _translate("cardaz_app", "Oregon"))
        self.state_CB.setItemText(37, _translate("cardaz_app", "Pennsylvannia"))
        self.state_CB.setItemText(38, _translate("cardaz_app", "Rhode Island"))
        self.state_CB.setItemText(39, _translate("cardaz_app", "South Carolina"))
        self.state_CB.setItemText(40, _translate("cardaz_app", "Tennessee"))
        self.state_CB.setItemText(41, _translate("cardaz_app", "Texas"))
        self.state_CB.setItemText(42, _translate("cardaz_app", "Utah"))
        self.state_CB.setItemText(43, _translate("cardaz_app", "Vermont"))
        self.state_CB.setItemText(44, _translate("cardaz_app", "Virginia"))
        self.state_CB.setItemText(45, _translate("cardaz_app", "West Virginia"))
        self.state_CB.setItemText(46, _translate("cardaz_app", "Wisconsin"))
        self.state_CB.setItemText(47, _translate("cardaz_app", "Wyoming"))
        self.titlelLabel.setText(_translate("cardaz_app", "Patient infomation Form"))
        self.execute_BTN.setText(_translate("cardaz_app", "Start"))
        self.start_info_Label.setText(_translate("cardaz_app", "Please Select your account, and hit ready to start the test."))
        self.ready_BTN.setText(_translate("cardaz_app", "Ready"))
        self.back_BTN.setText(_translate("cardaz_app", "back"))
        self.sBTN.setText(_translate("cardaz_app", "select All"))
        self.s1BTN.setText(_translate("cardaz_app", "select one"))
        self.sfilterBTN.setText(_translate("cardaz_app", "Sel w/Filter"))
        self.insBTN.setText(_translate("cardaz_app", "Insert"))
        self.upBTN.setText(_translate("cardaz_app", "update"))
        self.exitBTN.setText(_translate("cardaz_app", "back to login"))
        self.remBTN.setText(_translate("cardaz_app", "Remove"))

from pyqtgraph.pyqtgraph import PlotWidget
