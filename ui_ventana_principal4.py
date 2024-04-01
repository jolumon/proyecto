# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal4vKCGVC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1099, 681)
        MainWindow.setStyleSheet(u"QPushButton:hover{\n"
"	font: 700 12pt \"Cascadia Code\";\n"
"\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_modulos = QFrame(self.frame)
        self.fr_modulos.setObjectName(u"fr_modulos")
        self.fr_modulos.setMaximumSize(QSize(200, 16777215))
        self.fr_modulos.setStyleSheet(u"background-color: rgb(188, 239, 233);")
        self.fr_modulos.setFrameShape(QFrame.StyledPanel)
        self.fr_modulos.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_modulos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_clientes = QPushButton(self.fr_modulos)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 0))
        self.btn_clientes.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.btn_clientes)

        self.btn_materias_primas = QPushButton(self.fr_modulos)
        self.btn_materias_primas.setObjectName(u"btn_materias_primas")
        self.btn_materias_primas.setMinimumSize(QSize(0, 0))
        self.btn_materias_primas.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.btn_materias_primas)

        self.btn_productos = QPushButton(self.fr_modulos)
        self.btn_productos.setObjectName(u"btn_productos")
        self.btn_productos.setMinimumSize(QSize(0, 0))
        self.btn_productos.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.btn_productos)

        self.btn_proveedores = QPushButton(self.fr_modulos)
        self.btn_proveedores.setObjectName(u"btn_proveedores")
        self.btn_proveedores.setMinimumSize(QSize(0, 0))
        self.btn_proveedores.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.btn_proveedores)


        self.horizontalLayout_2.addWidget(self.fr_modulos)

        self.fr_informacion = QFrame(self.frame)
        self.fr_informacion.setObjectName(u"fr_informacion")
        self.fr_informacion.setFrameShape(QFrame.StyledPanel)
        self.fr_informacion.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_informacion)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.fr_informacion)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(188, 239, 233);")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.fr_informacion)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pricipal", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_materias_primas.setText(QCoreApplication.translate("MainWindow", u"Materias Primas", None))
        self.btn_productos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.btn_proveedores.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a labERP", None))
    # retranslateUi

