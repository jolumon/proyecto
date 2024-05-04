# import sys
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableView
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel
from PySide6.QtCore import Qt, QSortFilterProxyModel
from clientes.view.ui_ventana_clientes2 import Ui_Form
from clientes.model.ventana_detalle import VentanaDetalle
from auxiliares import VentanaEmergenteVacio


class VentanaCliente(QWidget, Ui_Form):
    def __init__(self, ventana_principal):
        super().__init__()
        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()
        self.ventana_principal = ventana_principal

        # Crear un model de tabla

        self.initial_query = QSqlQuery()
        self.initial_query.exec(
            "select * from clientes where activo_cli=true order by nombre_cli")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.initial_query)
        
       #Cabeceras de la tabla
        cabeceras = ['Codigo','Nombre','Dirección','Código Postal', 'Población','Provincia','Teléfono','Email','Contacto','Activo']
        for i,cabecera in enumerate(cabeceras):
            self.model.setHeaderData(i, Qt.Horizontal,cabecera )

        # Crear un filtro para la búsqueda
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Crear un cuadro de texto para la búsqueda

        self.le_buscar.setPlaceholderText("Buscar por nombre...")
        self.le_buscar.textChanged.connect(self.filter)

        # Crear una tabla para mostrar los datos

        self.tv_clientes.setModel(self.proxy_model)
        self.tv_clientes.setSelectionBehavior(QTableView.SelectRows)
        self.tv_clientes.setSelectionMode(QTableView.SingleSelection)
        self.tv_clientes.setColumnHidden(9,True)
        self.tv_clientes.show()

        # Crear la vista de tabla y establecer el model

        # self.tv_clientes.setModel(self.model)
        self.tv_clientes.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
        # Seleccionar filas completas
        self.tv_clientes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_clientes.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Seleccionar filas completas

        # Configurar la vista de tabla
        self.tv_clientes.resizeRowsToContents()
        self.tv_clientes.resizeColumnsToContents()
        # Amplia el tamaño de la tabla a toda la pantalla
        self.tv_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tv_clientes.selectRow(0)

        # Signal and Slots pestaña listado clientes
        self.btn_cerrar_listado.clicked.connect(self.close)
        self.btn_ver_listado.clicked.connect(self.ver_detalle_cliente2)

        # Signals and slots pestaña nuevo

        self.btn_cancelar_nuevo.clicked.connect(self.cambia_pestaña)
        self.btn_guardar_nuevo.clicked.connect(self.guardar_nuevo)

    def cambia_pestaña(self):
        self.tabWidget.setCurrentIndex(1)

    def closeEvent(self, event):
        # Cuando se cierra la ventana secundaria, se muestra la ventana principal
        self.ventana_principal.show()
        event.accept()

    def filter(self):
        text = self.le_buscar.text()
        # Usar setFilterFixedString en lugar de setFilterRegExp
        self.proxy_model.setFilterFixedString(text)
        # Filtrar por la columna "nombre_persona"
        self.proxy_model.setFilterKeyColumn(1)
        self.proxy_model.invalidate()  # Asegurarse de que el proxy model se actualice

    def guardar_nuevo(self):

        # Recuperar datos de los lineEdit
        nombre = self.le_nombre.text()
        if len(nombre) > 0:
            direccion = self.le_direccion.text()
            codigo_postal = self.le_codigo_postal.text()
            poblacion = self.le_poblacion.text()
            provincia = self.le_poblacion.text()
            telefono = self.le_telefono.text()
            email = self.le_email.text()
            contacto = self.le_contacto.text()
            # Crear y preparacion de la sentencia sql
            query = QSqlQuery()
            query.prepare(
                "insert into clientes(nombre_cli,direccion_cli,codigo_postal_cli, poblacion_cli,provincia_cli, "
                "telefono_cli,email_cli,contacto_cli) "
                "values (:nombre, :direccion, :codigo_postal, :poblacion, :provincia, :telefono, :email, :contacto)"
            )

            query.bindValue(":nombre", nombre)
            query.bindValue(":direccion", direccion)
            query.bindValue(":codigo_postal", codigo_postal)
            query.bindValue(":poblacion", poblacion)
            query.bindValue(":provincia", provincia)
            query.bindValue(":telefono", telefono)
            query.bindValue(":email", email)
            query.bindValue(":contacto", contacto)

            query.exec()

            # Borrar datos introducidos
            self.le_nombre.setText("")
            self.le_direccion.setText("")
            self.le_codigo_postal.setText("")
            self.le_poblacion.setText("")
            self.le_provincia.setText("")
            self.le_telefono.setText("")
            self.le_email.setText("")
            self.le_contacto.setText("")

            # self.close()

            self.tabWidget.setCurrentIndex(1)

            self.initial_query.exec(
                "select * from clientes where activo_cli=true order by nombre_cli")
            self.model.setQuery(self.initial_query)
            # self.model.select()
            # self.tv_clientes.reset()
            self.tv_clientes.selectRow(0)
        else:
            ventana_confirmacion = VentanaEmergenteVacio()
            respuesta = ventana_confirmacion.exec()
            # if respuesta:
            #     pass

    def ver_detalle_cliente2(self):
        self.ventana_detalle = VentanaDetalle(self)
        selected = self.tv_clientes.selectedIndexes()
        if selected:
            row = selected[0].row()
            id_pers_index = self.proxy_model.mapToSource(selected[0])
            # Suponiendo que el id está en la primera columna
            codigo = self.model.data(self.model.index(id_pers_index.row(), 0))
            nombre = self.model.data(self.model.index(id_pers_index.row(), 1))
            direccion = self.model.data(
                self.model.index(id_pers_index.row(), 2))
            codigo_postal = self.model.data(
                self.model.index(id_pers_index.row(), 3))
            poblacion = self.model.data(
                self.model.index(id_pers_index.row(), 4))
            provincia = self.model.data(
                self.model.index(id_pers_index.row(), 5))
            email = self.model.data(self.model.index(id_pers_index.row(), 7))
            telefono = self.model.data(
                self.model.index(id_pers_index.row(), 6))
            contacto = self.model.data(
                self.model.index(id_pers_index.row(), 8))

            print(
                f'Código: {codigo}-Nombre: {nombre}-{direccion}-{codigo_postal}')

            # establecemos los campos con los valores seleccionados
            self.ventana_detalle.le_codigo.setText(str(codigo))
            self.ventana_detalle.le_nombre.setText(nombre)
            self.ventana_detalle.le_direccion.setText(direccion)
            self.ventana_detalle.le_codigo_postal.setText(codigo_postal)
            self.ventana_detalle.le_poblacion.setText(poblacion)
            self.ventana_detalle.le_provincia.setText(provincia)
            self.ventana_detalle.le_email.setText(email)
            self.ventana_detalle.le_telefono.setText(telefono)
            self.ventana_detalle.le_contacto.setText(contacto)

            self.query_productos = QSqlQuery()
            self.query_productos.prepare(
                "SELECT productos.id_prod,productos.nombre_prod, productos.linea_prod FROM productos INNER JOIN clientes on productos.cliente_prod=clientes.id_cli WHERE id_cli=:codigo ORDER BY productos.nombre_prod")
            self.query_productos.bindValue(':codigo', codigo)
            self.query_productos.exec()

            self.model2 = QSqlQueryModel()
            self.model2.setQuery(self.query_productos)

            self.model2.setHeaderData(0, Qt.Horizontal, str("Código"))
            self.model2.setHeaderData(1, Qt.Horizontal, str("Producto"))
            self.model2.setHeaderData(2, Qt.Horizontal, str("Linea"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_productos.setModel(self.model2)
            self.ventana_detalle.tv_productos.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_productos.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_productos.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_productos.resizeRowsToContents()
            self.ventana_detalle.tv_productos.resizeColumnsToContents()
            self.ventana_detalle.tv_productos.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)

            self.ventana_detalle.show()

            self.hide()