# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_productos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(1017, 881)
        Form.setStyleSheet(u"QPushButton{background-color: rgb(6, 191, 249);}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_nuevo_producto = QWidget()
        self.tab_nuevo_producto.setObjectName(u"tab_nuevo_producto")
        self.verticalLayout = QVBoxLayout(self.tab_nuevo_producto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_nombre_prod = QLabel(self.tab_nuevo_producto)
        self.lbl_nombre_prod.setObjectName(u"lbl_nombre_prod")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_nombre_prod)

        self.le_nombre_prod = QLineEdit(self.tab_nuevo_producto)
        self.le_nombre_prod.setObjectName(u"le_nombre_prod")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nombre_prod)

        self.lbl_linea_prod = QLabel(self.tab_nuevo_producto)
        self.lbl_linea_prod.setObjectName(u"lbl_linea_prod")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_linea_prod)

        self.le_linea_prod = QLineEdit(self.tab_nuevo_producto)
        self.le_linea_prod.setObjectName(u"le_linea_prod")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_linea_prod)

        self.lbl_cliente_prod = QLabel(self.tab_nuevo_producto)
        self.lbl_cliente_prod.setObjectName(u"lbl_cliente_prod")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_cliente_prod)

        self.cb_cliente_prod = QComboBox(self.tab_nuevo_producto)
        self.cb_cliente_prod.setObjectName(u"cb_cliente_prod")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_cliente_prod)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_cancelar_nuevo = QPushButton(self.tab_nuevo_producto)
        self.btn_cancelar_nuevo.setObjectName(u"btn_cancelar_nuevo")

        self.horizontalLayout_2.addWidget(self.btn_cancelar_nuevo)

        self.btn_guardar_nuevo = QPushButton(self.tab_nuevo_producto)
        self.btn_guardar_nuevo.setObjectName(u"btn_guardar_nuevo")

        self.horizontalLayout_2.addWidget(self.btn_guardar_nuevo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_nuevo_producto, "")
        self.tab_detalle_producto = QWidget()
        self.tab_detalle_producto.setObjectName(u"tab_detalle_producto")
        self.verticalLayout_2 = QVBoxLayout(self.tab_detalle_producto)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_buscar_prod = QLineEdit(self.tab_detalle_producto)
        self.le_buscar_prod.setObjectName(u"le_buscar_prod")
        self.le_buscar_prod.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.le_buscar_prod)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tv_productos = QTableView(self.tab_detalle_producto)
        self.tv_productos.setObjectName(u"tv_productos")

        self.verticalLayout_2.addWidget(self.tv_productos)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_ver_prod_listado = QPushButton(self.tab_detalle_producto)
        self.btn_ver_prod_listado.setObjectName(u"btn_ver_prod_listado")

        self.horizontalLayout_4.addWidget(self.btn_ver_prod_listado)

        self.btn_cerrar_listado = QPushButton(self.tab_detalle_producto)
        self.btn_cerrar_listado.setObjectName(u"btn_cerrar_listado")
        self.btn_cerrar_listado.setStyleSheet(u"background-color: rgb(22, 183, 40);")

        self.horizontalLayout_4.addWidget(self.btn_cerrar_listado)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_detalle_producto, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Productos", None))
        self.lbl_nombre_prod.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lbl_linea_prod.setText(QCoreApplication.translate("Form", u"Linea", None))
        self.lbl_cliente_prod.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.btn_cancelar_nuevo.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btn_guardar_nuevo.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nuevo_producto), QCoreApplication.translate("Form", u"Nuevo", None))
        self.btn_ver_prod_listado.setText(QCoreApplication.translate("Form", u"Ver", None))
        self.btn_cerrar_listado.setText(QCoreApplication.translate("Form", u"Salir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detalle_producto), QCoreApplication.translate("Form", u"Listado Productos", None))
    # retranslateUi

