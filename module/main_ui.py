# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_code = QPlainTextEdit(self.centralwidget)
        self.input_code.setObjectName(u"input_code")
        self.input_code.setGeometry(QRect(10, 30, 441, 261))
        self.input_code.setCursorWidth(1)
        self.button_compile = QPushButton(self.centralwidget)
        self.button_compile.setObjectName(u"button_compile")
        self.button_compile.setGeometry(QRect(10, 300, 75, 24))
        self.output_messages = QPlainTextEdit(self.centralwidget)
        self.output_messages.setObjectName(u"output_messages")
        self.output_messages.setEnabled(True)
        self.output_messages.setGeometry(QRect(10, 360, 891, 64))
        self.output_messages.setReadOnly(True)
        self.output_messages.setCursorWidth(0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 340, 101, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 10, 101, 16))
        self.output_table_result = QTableWidget(self.centralwidget)
        self.output_table_result.setObjectName(u"output_table_result")
        self.output_table_result.setGeometry(QRect(470, 30, 431, 261))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 923, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_compile.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mensajes (Logs)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Editor", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Analisis Lexico", None))
    # retranslateUi

