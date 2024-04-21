# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materias_primas_detalle2jkUwQy.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1110, 758)
        Form.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(6, 191, 249);\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_detalle = QWidget()
        self.tab_detalle.setObjectName(u"tab_detalle")
        self.verticalLayout_3 = QVBoxLayout(self.tab_detalle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_codigo_det = QLabel(self.tab_detalle)
        self.lbl_codigo_det.setObjectName(u"lbl_codigo_det")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_codigo_det)

        self.le_codigo_det = QLineEdit(self.tab_detalle)
        self.le_codigo_det.setObjectName(u"le_codigo_det")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_codigo_det)

        self.lbl_nombre_det = QLabel(self.tab_detalle)
        self.lbl_nombre_det.setObjectName(u"lbl_nombre_det")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_nombre_det)

        self.le_nombre_det = QLineEdit(self.tab_detalle)
        self.le_nombre_det.setObjectName(u"le_nombre_det")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_nombre_det)

        self.lbl_cantidad_det = QLabel(self.tab_detalle)
        self.lbl_cantidad_det.setObjectName(u"lbl_cantidad_det")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_cantidad_det)

        self.le_cantidad_det = QLineEdit(self.tab_detalle)
        self.le_cantidad_det.setObjectName(u"le_cantidad_det")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_cantidad_det)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_actualizar_det = QPushButton(self.tab_detalle)
        self.btn_actualizar_det.setObjectName(u"btn_actualizar_det")

        self.horizontalLayout_2.addWidget(self.btn_actualizar_det)

        self.btn_borrar_det = QPushButton(self.tab_detalle)
        self.btn_borrar_det.setObjectName(u"btn_borrar_det")
        self.btn_borrar_det.setStyleSheet(u"background-color: rgb(254, 20, 20);")

        self.horizontalLayout_2.addWidget(self.btn_borrar_det)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.tab_detalle)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tv_entradas_mp_det = QTableView(self.groupBox)
        self.tv_entradas_mp_det.setObjectName(u"tv_entradas_mp_det")

        self.verticalLayout_2.addWidget(self.tv_entradas_mp_det)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cerrar_det = QPushButton(self.tab_detalle)
        self.btn_cerrar_det.setObjectName(u"btn_cerrar_det")

        self.horizontalLayout.addWidget(self.btn_cerrar_det)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_detalle, "")
        self.tab_entrada = QWidget()
        self.tab_entrada.setObjectName(u"tab_entrada")
        self.verticalLayout_9 = QVBoxLayout(self.tab_entrada)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_exterior = QFrame(self.tab_entrada)
        self.frame_exterior.setObjectName(u"frame_exterior")
        self.frame_exterior.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_exterior.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_exterior)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_form = QFrame(self.frame_exterior)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_form.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_fecha_entrada = QLabel(self.frame_form)
        self.lbl_fecha_entrada.setObjectName(u"lbl_fecha_entrada")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_fecha_entrada)

        self.lbl_codigo_entrada = QLabel(self.frame_form)
        self.lbl_codigo_entrada.setObjectName(u"lbl_codigo_entrada")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_codigo_entrada)

        self.lbl_proveedor_entrada = QLabel(self.frame_form)
        self.lbl_proveedor_entrada.setObjectName(u"lbl_proveedor_entrada")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_proveedor_entrada)

        self.lbl_nombre_entrada = QLabel(self.frame_form)
        self.lbl_nombre_entrada.setObjectName(u"lbl_nombre_entrada")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_nombre_entrada)

        self.le_codigo_entrada = QLineEdit(self.frame_form)
        self.le_codigo_entrada.setObjectName(u"le_codigo_entrada")
        self.le_codigo_entrada.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_codigo_entrada)

        self.le_nombre_entrada = QLineEdit(self.frame_form)
        self.le_nombre_entrada.setObjectName(u"le_nombre_entrada")
        self.le_nombre_entrada.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_nombre_entrada)

        self.lbl_lote_entrada = QLabel(self.frame_form)
        self.lbl_lote_entrada.setObjectName(u"lbl_lote_entrada")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbl_lote_entrada)

        self.le_proveedor_entrada = QLineEdit(self.frame_form)
        self.le_proveedor_entrada.setObjectName(u"le_proveedor_entrada")
        self.le_proveedor_entrada.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.le_proveedor_entrada)

        self.le_lote_entrada = QLineEdit(self.frame_form)
        self.le_lote_entrada.setObjectName(u"le_lote_entrada")
        self.le_lote_entrada.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.le_lote_entrada)

        self.lbl_fecha_caducidad = QLabel(self.frame_form)
        self.lbl_fecha_caducidad.setObjectName(u"lbl_fecha_caducidad")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbl_fecha_caducidad)

        self.de_f_caducidad = QDateEdit(self.frame_form)
        self.de_f_caducidad.setObjectName(u"de_f_caducidad")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.de_f_caducidad)

        self.lbl_cantidad_entrada = QLabel(self.frame_form)
        self.lbl_cantidad_entrada.setObjectName(u"lbl_cantidad_entrada")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_cantidad_entrada)

        self.lbl_precio_entrada = QLabel(self.frame_form)
        self.lbl_precio_entrada.setObjectName(u"lbl_precio_entrada")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lbl_precio_entrada)

        self.le_cantidad_entrada = QLineEdit(self.frame_form)
        self.le_cantidad_entrada.setObjectName(u"le_cantidad_entrada")
        self.le_cantidad_entrada.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.le_cantidad_entrada)

        self.le_precio_entrada = QLineEdit(self.frame_form)
        self.le_precio_entrada.setObjectName(u"le_precio_entrada")
        self.le_precio_entrada.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.le_precio_entrada.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.le_precio_entrada)

        self.le_f_entrada = QLineEdit(self.frame_form)
        self.le_f_entrada.setObjectName(u"le_f_entrada")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_f_entrada)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.verticalLayout_4.addWidget(self.frame_form)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_cerrar_entrada = QPushButton(self.frame_exterior)
        self.btn_cerrar_entrada.setObjectName(u"btn_cerrar_entrada")

        self.horizontalLayout_5.addWidget(self.btn_cerrar_entrada)

        self.btn_guardar_entrada = QPushButton(self.frame_exterior)
        self.btn_guardar_entrada.setObjectName(u"btn_guardar_entrada")

        self.horizontalLayout_5.addWidget(self.btn_guardar_entrada)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.frame_exterior)

        self.tabWidget.addTab(self.tab_entrada, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Detalle Materia Prima", None))
        self.lbl_codigo_det.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.lbl_nombre_det.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lbl_cantidad_det.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.btn_actualizar_det.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.btn_borrar_det.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Entradas", None))
        self.btn_cerrar_det.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detalle), QCoreApplication.translate("Form", u"Detalle", None))
        self.lbl_fecha_entrada.setText(QCoreApplication.translate("Form", u"Fecha", None))
        self.lbl_codigo_entrada.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.lbl_proveedor_entrada.setText(QCoreApplication.translate("Form", u"Proveedor", None))
        self.lbl_nombre_entrada.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lbl_lote_entrada.setText(QCoreApplication.translate("Form", u"Lote", None))
        self.le_lote_entrada.setText("")
        self.le_lote_entrada.setPlaceholderText(QCoreApplication.translate("Form", u"Campo obligatorio", None))
        self.lbl_fecha_caducidad.setText(QCoreApplication.translate("Form", u"Fecha caducidad", None))
        self.de_f_caducidad.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.lbl_cantidad_entrada.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.lbl_precio_entrada.setText(QCoreApplication.translate("Form", u"Precio", None))
        self.le_cantidad_entrada.setPlaceholderText(QCoreApplication.translate("Form", u"Campo obligatorio", None))
        self.le_precio_entrada.setInputMask("")
        self.le_precio_entrada.setText("")
        self.le_precio_entrada.setPlaceholderText(QCoreApplication.translate("Form", u"Campo obligatorio", None))
        self.btn_cerrar_entrada.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.btn_guardar_entrada.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_entrada), QCoreApplication.translate("Form", u"Entrada", None))
    # retranslateUi

