# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_proveedores.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(1072, 658)
        Form.setStyleSheet(u"QPushButton{background-color: rgb(6, 191, 249);}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_nuevo = QWidget()
        self.tab_nuevo.setObjectName(u"tab_nuevo")
        self.verticalLayout = QVBoxLayout(self.tab_nuevo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_codigo = QLabel(self.tab_nuevo)
        self.lbl_codigo.setObjectName(u"lbl_codigo")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_codigo)

        self.le_codigo = QLineEdit(self.tab_nuevo)
        self.le_codigo.setObjectName(u"le_codigo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_codigo)

        self.lbl_nombre = QLabel(self.tab_nuevo)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_nombre)

        self.le_nombre = QLineEdit(self.tab_nuevo)
        self.le_nombre.setObjectName(u"le_nombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_nombre)

        self.lbl_direccion = QLabel(self.tab_nuevo)
        self.lbl_direccion.setObjectName(u"lbl_direccion")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_direccion)

        self.le_direccion = QLineEdit(self.tab_nuevo)
        self.le_direccion.setObjectName(u"le_direccion")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_direccion)

        self.lbl_codigo_postal = QLabel(self.tab_nuevo)
        self.lbl_codigo_postal.setObjectName(u"lbl_codigo_postal")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_codigo_postal)

        self.le_codigo_postal = QLineEdit(self.tab_nuevo)
        self.le_codigo_postal.setObjectName(u"le_codigo_postal")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_codigo_postal)

        self.lbl_poblacion = QLabel(self.tab_nuevo)
        self.lbl_poblacion.setObjectName(u"lbl_poblacion")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_poblacion)

        self.le_poblacion = QLineEdit(self.tab_nuevo)
        self.le_poblacion.setObjectName(u"le_poblacion")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_poblacion)

        self.lbl_provincia = QLabel(self.tab_nuevo)
        self.lbl_provincia.setObjectName(u"lbl_provincia")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_provincia)

        self.le_provincia = QLineEdit(self.tab_nuevo)
        self.le_provincia.setObjectName(u"le_provincia")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_provincia)

        self.lbl_telefono = QLabel(self.tab_nuevo)
        self.lbl_telefono.setObjectName(u"lbl_telefono")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_telefono)

        self.le_telefono = QLineEdit(self.tab_nuevo)
        self.le_telefono.setObjectName(u"le_telefono")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_telefono)

        self.lbl_movil = QLabel(self.tab_nuevo)
        self.lbl_movil.setObjectName(u"lbl_movil")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_movil)

        self.le_movil = QLineEdit(self.tab_nuevo)
        self.le_movil.setObjectName(u"le_movil")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_movil)

        self.lbl_email = QLabel(self.tab_nuevo)
        self.lbl_email.setObjectName(u"lbl_email")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_email)

        self.le_email = QLineEdit(self.tab_nuevo)
        self.le_email.setObjectName(u"le_email")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_email)

        self.le_contacto = QLineEdit(self.tab_nuevo)
        self.le_contacto.setObjectName(u"le_contacto")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.le_contacto)

        self.lbl_contacto = QLabel(self.tab_nuevo)
        self.lbl_contacto.setObjectName(u"lbl_contacto")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lbl_contacto)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_cancelar_nuevo = QPushButton(self.tab_nuevo)
        self.btn_cancelar_nuevo.setObjectName(u"btn_cancelar_nuevo")

        self.horizontalLayout_2.addWidget(self.btn_cancelar_nuevo)

        self.btn_guardar_nuevo = QPushButton(self.tab_nuevo)
        self.btn_guardar_nuevo.setObjectName(u"btn_guardar_nuevo")

        self.horizontalLayout_2.addWidget(self.btn_guardar_nuevo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_nuevo, "")
        self.tab_detalle = QWidget()
        self.tab_detalle.setObjectName(u"tab_detalle")
        self.verticalLayout_2 = QVBoxLayout(self.tab_detalle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_buscar = QLineEdit(self.tab_detalle)
        self.le_buscar.setObjectName(u"le_buscar")
        self.le_buscar.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.le_buscar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tv_proveedores = QTableView(self.tab_detalle)
        self.tv_proveedores.setObjectName(u"tv_proveedores")

        self.verticalLayout_2.addWidget(self.tv_proveedores)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_ver_listado = QPushButton(self.tab_detalle)
        self.btn_ver_listado.setObjectName(u"btn_ver_listado")

        self.horizontalLayout_4.addWidget(self.btn_ver_listado)

        self.btn_cerrar_listado = QPushButton(self.tab_detalle)
        self.btn_cerrar_listado.setObjectName(u"btn_cerrar_listado")

        self.horizontalLayout_4.addWidget(self.btn_cerrar_listado)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_detalle, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Proveedores", None))
        self.lbl_codigo.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.lbl_nombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lbl_direccion.setText(QCoreApplication.translate("Form", u"Direcci\u00f3n", None))
        self.lbl_codigo_postal.setText(QCoreApplication.translate("Form", u"C\u00f3digo Postal", None))
        self.lbl_poblacion.setText(QCoreApplication.translate("Form", u"Poblaci\u00f3n", None))
        self.lbl_provincia.setText(QCoreApplication.translate("Form", u"Provincia", None))
        self.lbl_telefono.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono", None))
        self.lbl_movil.setText(QCoreApplication.translate("Form", u"M\u00f3vil", None))
        self.lbl_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.lbl_contacto.setText(QCoreApplication.translate("Form", u"Contacto", None))
        self.btn_cancelar_nuevo.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btn_guardar_nuevo.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nuevo), QCoreApplication.translate("Form", u"Nuevo", None))
        self.btn_ver_listado.setText(QCoreApplication.translate("Form", u"Ver", None))
        self.btn_cerrar_listado.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detalle), QCoreApplication.translate("Form", u"Listado Proveedores", None))
    # retranslateUi

