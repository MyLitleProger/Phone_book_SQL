# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_GeneralWindow(object):
    def setupUi(self, GeneralWindow):
        if not GeneralWindow.objectName():
            GeneralWindow.setObjectName(u"GeneralWindow")
        GeneralWindow.resize(728, 534)
        GeneralWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.layoutWidget = QWidget(GeneralWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QRect(9, 9, 710, 54))
        self.layoutWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.layoutWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton.setIconSize(QSize(16, 27))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_2.setIconSize(QSize(16, 27))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_3.setIconSize(QSize(16, 27))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.tableView = QTableView(GeneralWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(9, 69, 711, 461))
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet(u"QTableView{\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView::section {\n"
"bacground-color: rgba(53,53,53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.retranslateUi(GeneralWindow)

        QMetaObject.connectSlotsByName(GeneralWindow)
    # setupUi

    def retranslateUi(self, GeneralWindow):
        GeneralWindow.setWindowTitle(QCoreApplication.translate("GeneralWindow", u"Table View", None))
        self.pushButton.setText(QCoreApplication.translate("GeneralWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("GeneralWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("GeneralWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

