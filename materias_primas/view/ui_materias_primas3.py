# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materias_primas3yIVwtJ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.WindowModal)
        Form.resize(1017, 734)
        Form.setStyleSheet(u"QPushButton{background-color: rgb(6, 191, 249);}\n"
"")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_detalle_mp = QWidget()
        self.tab_detalle_mp.setObjectName(u"tab_detalle_mp")
        self.verticalLayout_2 = QVBoxLayout(self.tab_detalle_mp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_buscar_mp = QLineEdit(self.tab_detalle_mp)
        self.le_buscar_mp.setObjectName(u"le_buscar_mp")
        self.le_buscar_mp.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.le_buscar_mp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tv_mat_primas = QTableView(self.tab_detalle_mp)
        self.tv_mat_primas.setObjectName(u"tv_mat_primas")

        self.verticalLayout_2.addWidget(self.tv_mat_primas)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_ver_detalle_mp = QPushButton(self.tab_detalle_mp)
        self.btn_ver_detalle_mp.setObjectName(u"btn_ver_detalle_mp")

        self.horizontalLayout_4.addWidget(self.btn_ver_detalle_mp)

        self.btn_cerrar_listado_mp = QPushButton(self.tab_detalle_mp)
        self.btn_cerrar_listado_mp.setObjectName(u"btn_cerrar_listado_mp")

        self.horizontalLayout_4.addWidget(self.btn_cerrar_listado_mp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_detalle_mp, "")
        self.tab_entradas_mp = QWidget()
        self.tab_entradas_mp.setObjectName(u"tab_entradas_mp")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_entradas_mp)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tv_entradas_list = QTableView(self.tab_entradas_mp)
        self.tv_entradas_list.setObjectName(u"tv_entradas_list")

        self.horizontalLayout_5.addWidget(self.tv_entradas_list)

        self.tabWidget.addTab(self.tab_entradas_mp, "")
        self.tab_nuevo_mp = QWidget()
        self.tab_nuevo_mp.setObjectName(u"tab_nuevo_mp")
        self.verticalLayout_8 = QVBoxLayout(self.tab_nuevo_mp)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_proveedor_nueva = QLabel(self.tab_nuevo_mp)
        self.lbl_proveedor_nueva.setObjectName(u"lbl_proveedor_nueva")

        self.gridLayout.addWidget(self.lbl_proveedor_nueva, 1, 0, 1, 1)

        self.btn_prov_new_nueva = QPushButton(self.tab_nuevo_mp)
        self.btn_prov_new_nueva.setObjectName(u"btn_prov_new_nueva")

        self.gridLayout.addWidget(self.btn_prov_new_nueva, 1, 2, 1, 1)

        self.cb_proveedor_nueva = QComboBox(self.tab_nuevo_mp)
        self.cb_proveedor_nueva.setObjectName(u"cb_proveedor_nueva")

        self.gridLayout.addWidget(self.cb_proveedor_nueva, 1, 1, 1, 1)

        self.lbl_nombre_nueva = QLabel(self.tab_nuevo_mp)
        self.lbl_nombre_nueva.setObjectName(u"lbl_nombre_nueva")

        self.gridLayout.addWidget(self.lbl_nombre_nueva, 0, 0, 1, 1)

        self.le_nombre_nueva = QLineEdit(self.tab_nuevo_mp)
        self.le_nombre_nueva.setObjectName(u"le_nombre_nueva")
        self.le_nombre_nueva.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_nombre_nueva, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.btn_cancelar_nueva_mp = QPushButton(self.tab_nuevo_mp)
        self.btn_cancelar_nueva_mp.setObjectName(u"btn_cancelar_nueva_mp")

        self.horizontalLayout_9.addWidget(self.btn_cancelar_nueva_mp)

        self.btn_guardar_nueva_mp = QPushButton(self.tab_nuevo_mp)
        self.btn_guardar_nueva_mp.setObjectName(u"btn_guardar_nueva_mp")

        self.horizontalLayout_9.addWidget(self.btn_guardar_nueva_mp)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_nuevo_mp, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Materias Primas", None))
        self.le_buscar_mp.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar por nombre...", None))
        self.btn_ver_detalle_mp.setText(QCoreApplication.translate("Form", u"Ver", None))
        self.btn_cerrar_listado_mp.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detalle_mp), QCoreApplication.translate("Form", u"Stock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_entradas_mp), QCoreApplication.translate("Form", u"Entradas", None))
        self.lbl_proveedor_nueva.setText(QCoreApplication.translate("Form", u"Proveedor", None))
        self.btn_prov_new_nueva.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.lbl_nombre_nueva.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.btn_cancelar_nueva_mp.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btn_guardar_nueva_mp.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nuevo_mp), QCoreApplication.translate("Form", u"Nueva", None))
    # retranslateUi

