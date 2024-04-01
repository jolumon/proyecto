# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_detallevQmqKr.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(1144, 594)
        Form.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(6, 191, 249);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.lbl_codigo = QLabel(Form)
        self.lbl_codigo.setObjectName(u"lbl_codigo")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_codigo)

        self.le_codigo = QLineEdit(Form)
        self.le_codigo.setObjectName(u"le_codigo")
        self.le_codigo.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_codigo)

        self.lbl_nombre = QLabel(Form)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_nombre)

        self.le_nombre = QLineEdit(Form)
        self.le_nombre.setObjectName(u"le_nombre")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_nombre)

        self.lbl_direccion = QLabel(Form)
        self.lbl_direccion.setObjectName(u"lbl_direccion")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_direccion)

        self.le_direccion = QLineEdit(Form)
        self.le_direccion.setObjectName(u"le_direccion")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_direccion)

        self.lbl_codigo_postal = QLabel(Form)
        self.lbl_codigo_postal.setObjectName(u"lbl_codigo_postal")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_codigo_postal)

        self.le_codigo_postal = QLineEdit(Form)
        self.le_codigo_postal.setObjectName(u"le_codigo_postal")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.le_codigo_postal)

        self.lbl_poblacion = QLabel(Form)
        self.lbl_poblacion.setObjectName(u"lbl_poblacion")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbl_poblacion)

        self.le_poblacion = QLineEdit(Form)
        self.le_poblacion.setObjectName(u"le_poblacion")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.le_poblacion)

        self.lbl_provincia = QLabel(Form)
        self.lbl_provincia.setObjectName(u"lbl_provincia")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbl_provincia)

        self.le_provincia = QLineEdit(Form)
        self.le_provincia.setObjectName(u"le_provincia")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.le_provincia)

        self.lbl_telefono = QLabel(Form)
        self.lbl_telefono.setObjectName(u"lbl_telefono")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_telefono)

        self.le_telefono = QLineEdit(Form)
        self.le_telefono.setObjectName(u"le_telefono")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.le_telefono)

        self.lbl_email = QLabel(Form)
        self.lbl_email.setObjectName(u"lbl_email")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lbl_email)

        self.le_email = QLineEdit(Form)
        self.le_email.setObjectName(u"le_email")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.le_email)

        self.lbl_contacto = QLabel(Form)
        self.lbl_contacto.setObjectName(u"lbl_contacto")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lbl_contacto)

        self.le_contacto = QLineEdit(Form)
        self.le_contacto.setObjectName(u"le_contacto")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.le_contacto)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_actualizar = QPushButton(Form)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.horizontalLayout.addWidget(self.btn_actualizar)

        self.btn_borrar = QPushButton(Form)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.horizontalLayout.addWidget(self.btn_borrar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tv_productos = QTableView(self.groupBox)
        self.tv_productos.setObjectName(u"tv_productos")

        self.verticalLayout.addWidget(self.tv_productos)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_cerrar = QPushButton(Form)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setStyleSheet(u"background-color: rgb(22, 183, 40);")

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Detalle cliente", None))
        self.lbl_codigo.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.lbl_nombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lbl_direccion.setText(QCoreApplication.translate("Form", u"Direcci\u00f3n", None))
        self.lbl_codigo_postal.setText(QCoreApplication.translate("Form", u"C\u00f3digo Postal", None))
        self.lbl_poblacion.setText(QCoreApplication.translate("Form", u"Poblaci\u00f3n", None))
        self.lbl_provincia.setText(QCoreApplication.translate("Form", u"Provincia", None))
        self.lbl_telefono.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono", None))
        self.lbl_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.lbl_contacto.setText(QCoreApplication.translate("Form", u"Contacto", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.btn_borrar.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Productos", None))
        self.btn_cerrar.setText(QCoreApplication.translate("Form", u"Salir", None))
    # retranslateUi

