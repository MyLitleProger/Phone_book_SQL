# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_record.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_RecordTableWindow(object):
    def setupUi(self, RecordTableWindow):
        if not RecordTableWindow.objectName():
            RecordTableWindow.setObjectName(u"RecordTableWindow")
        RecordTableWindow.resize(373, 463)
        RecordTableWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.BT_Save = QPushButton(RecordTableWindow)
        self.BT_Save.setObjectName(u"BT_Save")
        self.BT_Save.setEnabled(True)
        self.BT_Save.setGeometry(QRect(70, 390, 232, 52))
        self.BT_Save.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.BT_Save.setFont(font)
        self.BT_Save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton: hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton: pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.BT_Save.setIconSize(QSize(16, 27))
        self.widget = QWidget(RecordTableWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 341, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_name)

        self.LE_Name = QLineEdit(self.widget)
        self.LE_Name.setObjectName(u"LE_Name")
        self.LE_Name.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.LE_Name)

        self.label_family = QLabel(self.widget)
        self.label_family.setObjectName(u"label_family")
        self.label_family.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_family)

        self.LE_Family = QLineEdit(self.widget)
        self.LE_Family.setObjectName(u"LE_Family")
        self.LE_Family.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.LE_Family)

        self.label_phone = QLabel(self.widget)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_phone)

        self.LE_Phone = QLineEdit(self.widget)
        self.LE_Phone.setObjectName(u"LE_Phone")
        self.LE_Phone.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.LE_Phone)


        self.retranslateUi(RecordTableWindow)

        QMetaObject.connectSlotsByName(RecordTableWindow)
    # setupUi

    def retranslateUi(self, RecordTableWindow):
        RecordTableWindow.setWindowTitle(QCoreApplication.translate("RecordTableWindow", u"Record Table", None))
        self.BT_Save.setText(QCoreApplication.translate("RecordTableWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_name.setText(QCoreApplication.translate("RecordTableWindow", u"\u0418\u043c\u044f:", None))
        self.label_family.setText(QCoreApplication.translate("RecordTableWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_phone.setText(QCoreApplication.translate("RecordTableWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.LE_Phone.setInputMask(QCoreApplication.translate("RecordTableWindow", u"+7(999) 999 99 99", None))
    # retranslateUi

