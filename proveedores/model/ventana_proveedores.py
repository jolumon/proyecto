import sys
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableView, QApplication
from proveedores.view.ui_ventana_proveedores2 import Ui_Form
from proveedores.model.ventana_detalle import VentanaDetalle
from PySide6.QtCore import Qt, QSortFilterProxyModel
from auxiliares import VentanaEmergenteVacio


class VentanaProveedor(QWidget, Ui_Form):
    def __init__(self, ventana_principal):
        super().__init__()
        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()
        self.ventana_principal = ventana_principal

        # Crear un model de tabla

        self.initial_query = QSqlQuery()
        self.initial_query.exec(
            "select * from proveedores where activo_prov=true order by id_prov")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.initial_query)

        # self.model = QSqlTableModel()
        # self.model.setTable('proveedores')
        # self.model.select()

        # self.model.setQuery("SELECT * FROM proveedores ORDER BY id_proveedor")
        self.model.setHeaderData(0, Qt.Horizontal, str("Código"))
        self.model.setHeaderData(1, Qt.Horizontal, str("Nombre"))
        self.model.setHeaderData(2, Qt.Horizontal, str("Dirección"))
        self.model.setHeaderData(3, Qt.Horizontal, str("Código postal"))
        self.model.setHeaderData(4, Qt.Horizontal, str("Población"))
        self.model.setHeaderData(5, Qt.Horizontal, str("Provincia"))
        self.model.setHeaderData(6, Qt.Horizontal, str("Teléfono"))
        self.model.setHeaderData(7, Qt.Horizontal, str("Contacto"))
        self.model.setHeaderData(8, Qt.Horizontal, str("Móvil"))
        self.model.setHeaderData(9, Qt.Horizontal, str("Email"))
        self.model.setHeaderData(10, Qt.Horizontal, str("Activo"))

        # Crear un filtro para la búsqueda
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Crear un cuadro de texto para la búsqueda

        self.le_buscar.setPlaceholderText("Buscar por nombre...")
        self.le_buscar.textChanged.connect(self.filter)

        # Crear una tabla para mostrar los datos

        self.tv_proveedores.setModel(self.proxy_model)
        self.tv_proveedores.setSelectionBehavior(QTableView.SelectRows)
        self.tv_proveedores.setSelectionMode(QTableView.SingleSelection)
        self.tv_proveedores.setColumnHidden(10,True)
        
        self.tv_proveedores.show()

        # Crear la vista de tabla y establecer el modelo
        # self.tv_proveedores.setModel(self.model)
        self.tv_proveedores.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
        # Seleccionar filas completas
        self.tv_proveedores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_proveedores.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Seleccionar filas completas

        # Configurar la vista de tabla
        self.tv_proveedores.resizeRowsToContents()
        self.tv_proveedores.resizeColumnsToContents()
        # Amplia el tamaño de la tabla a toda la pantalla
        self.tv_proveedores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tv_proveedores.selectRow(0)

        # Señales pestaña listado proveedores
        self.btn_cerrar_listado_proveedores.clicked.connect(self.close)
        self.btn_ver_listado_proveedor.clicked.connect(
            self.ver_detalle_proveedor2)

        # Señales pestana nuevo proveedor

        self.btn_guardar_nuevo_proveedor.clicked.connect(self.guardar_nuevo)
        self.btn_cancelar_nuevo_proveedor.clicked.connect(self.cambia_pestaña)

    def cambia_pestaña(self):
        self.tabWidget.setCurrentIndex(1)

    def closeEvent(self, event):
        # Cuando se cierra la ventana proveedores, se muestra la ventana principal
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
            contacto = self.le_contacto.text()
            movil = self.le_movil.text()
            email = self.le_email.text()

            # Crear y preparacion de la sentencia sql
            query = QSqlQuery()
            query.prepare(
                f'insert into proveedores (nombre_prov,direccion_prov,cp_prov,poblacion_prov,provincia_prov,telefono_prov,contacto_prov, movil_prov, email_prov) values (:nombre, :direccion, :codigo_postal, :poblacion, :provincia, :telefono, :contacto, :movil,:email)')

            query.bindValue(":nombre", nombre)
            query.bindValue(":direccion", direccion)
            query.bindValue(":codigo_postal", codigo_postal)
            query.bindValue(":poblacion", poblacion)
            query.bindValue(":provincia", provincia)
            query.bindValue(":telefono", telefono)
            query.bindValue(":contacto", contacto)
            query.bindValue(":movil", movil)
            query.bindValue(":email", email)

            query.exec()

            # Borrar datos introducidos
            self.le_nombre.setText("")
            self.le_direccion.setText("")
            self.le_codigo_postal.setText("")
            self.le_poblacion.setText("")
            self.le_provincia.setText("")
            self.le_telefono.setText("")
            self.le_email.setText("")
            self.lbl_contacto.setText("")

            # self.close()

            self.tabWidget.setCurrentIndex(1)

            self.initial_query.exec(
                "select * from proveedores where activo_prov=true order by id_prov")
            self.model.setQuery(self.initial_query)

            self.tv_proveedores.selectRow(0)

        else:
            ventana_confirmacion = VentanaEmergenteVacio()
            respuesta = ventana_confirmacion.exec()

    def ver_detalle_proveedor2(self):
        # Se crea la ventana de detalle del cliente
        self.ventana_detalle = VentanaDetalle(self)
        selected_index = self.tv_proveedores.selectedIndexes()
        print(f'Selected index: {selected_index}')
        if selected_index:
            # Obtenemos el número de fila de la celda seleccionada
            # print('Entra en el if del selected_index')
            row = selected_index[0].row()
            id_pers_index = self.proxy_model.mapToSource(selected_index[0])

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
            telefono = self.model.data(
                self.model.index(id_pers_index.row(), 6))
            contacto = self.model.data(
                self.model.index(id_pers_index.row(), 7))
            contacto = self.model.data(
                self.model.index(id_pers_index.row(), 7))
            movil = self.model.data(self.model.index(id_pers_index.row(), 8))
            email = self.model.data(self.model.index(id_pers_index.row(), 9))

            # establecemos los campos con los valores seleccionados
            self.ventana_detalle.le_codigo.setText(str(codigo))
            self.ventana_detalle.le_nombre.setText(nombre)
            self.ventana_detalle.le_direccion.setText(direccion)
            self.ventana_detalle.le_codigo_postal.setText(codigo_postal)
            self.ventana_detalle.le_poblacion.setText(poblacion)
            self.ventana_detalle.le_provincia.setText(provincia)
            self.ventana_detalle.le_telefono.setText(telefono)
            self.ventana_detalle.le_contacto.setText(contacto)
            self.ventana_detalle.le_movil.setText(movil)
            self.ventana_detalle.le_email.setText(email)

            self.query_materias_primas = QSqlQuery()
            self.query_materias_primas.prepare(
                "select distinct mp.id_mp,mp.nombre_mp,mp.cantidad_mp  from materias_primas mp inner join entradas ent on mp.id_mp = ent.id_mp_ent inner join proveedores p  on ent.id_prov_ent  = p.id_prov  where p.id_prov =:codigo")
            self.query_materias_primas.bindValue(':codigo', codigo)
            self.query_materias_primas.exec()

            self.model2 = QSqlQueryModel()
            self.model2.setQuery(self.query_materias_primas)

            self.model2.setHeaderData(0, Qt.Horizontal, str("Código"))
            self.model2.setHeaderData(1, Qt.Horizontal, str("Materia Prima"))
            self.model2.setHeaderData(2, Qt.Horizontal, str("Cantidad / kg"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_materias_primas.setModel(self.model2)
            self.ventana_detalle.tv_materias_primas.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_materias_primas.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_materias_primas.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_materias_primas.resizeRowsToContents()
            self.ventana_detalle.tv_materias_primas.resizeColumnsToContents()
            self.ventana_detalle.tv_materias_primas.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)

            self.ventana_detalle.show()
            # self.ventana_detalle.show()

            self.hide()

        # Se puede quitar el else-->Habrá que hacerlo
        else:
            print('No entra en if del selected_index')

    def ver_detalle_proveedor(self):
        # Se crea la ventana de detalle del cliente
        self.ventana_detalle = VentanaDetalle(self)
        selected_index = self.tv_proveedores.currentIndex()
        print(f'Selected index: {selected_index}')
        if selected_index.isValid():
            # Obtenemos el número de fila de la celda seleccionada
            # print('Entra en el if del selected_index')
            fila = selected_index.row()

            codigo = self.model.index(fila, 0).data()
            nombre = self.model.index(fila, 1).data()
            direccion = self.model.index(fila, 2).data()
            codigo_postal = self.model.index(fila, 3).data()
            poblacion = self.model.index(fila, 4).data()
            provincia = self.model.index(fila, 5).data()
            telefono = self.model.index(fila, 6).data()
            contacto = self.model.index(fila, 7).data()
            movil = self.model.index(fila, 8).data()
            email = self.model.index(fila, 9).data()
            # establecemos los campos con los valores seleccionados
            self.ventana_detalle.le_codigo.setText(str(codigo))
            self.ventana_detalle.le_nombre.setText(nombre)
            self.ventana_detalle.le_direccion.setText(direccion)
            self.ventana_detalle.le_codigo_postal.setText(codigo_postal)
            self.ventana_detalle.le_poblacion.setText(poblacion)
            self.ventana_detalle.le_provincia.setText(provincia)
            self.ventana_detalle.le_telefono.setText(telefono)
            self.ventana_detalle.le_contacto.setText(contacto)
            self.ventana_detalle.le_movil.setText(movil)
            self.ventana_detalle.le_email.setText(email)

            self.query_materias_primas = QSqlQuery()
            self.query_materias_primas.prepare(
                "select distinct mp.id_mp,mp.nombre_mp,mp.cantidad_mp  from materias_primas mp inner join entradas ent on mp.id_mp = ent.id_mp_ent inner join proveedores p  on ent.id_prov_ent  = p.id_prov  where p.id_prov = :codigo")
            self.query_materias_primas.bindValue(':codigo', codigo)
            self.query_materias_primas.exec()

            self.model2 = QSqlQueryModel()
            self.model2.setQuery(self.query_materias_primas)

            self.model2.setHeaderData(0, Qt.Horizontal, str("Código"))
            self.model2.setHeaderData(1, Qt.Horizontal, str("Materia Prima"))
            self.model2.setHeaderData(2, Qt.Horizontal, str("Cantidad / kg"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_materias_primas.setModel(self.model2)
            self.ventana_detalle.tv_materias_primas.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_materias_primas.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_materias_primas.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_materias_primas.resizeRowsToContents()
            self.ventana_detalle.tv_materias_primas.resizeColumnsToContents()
            self.ventana_detalle.tv_materias_primas.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)

            self.ventana_detalle.show()
            # self.ventana_detalle.show()

            self.hide()

        # Se puede quitar el else-->Habrá que hacerlo
        else:
            print('No entra en if del selected_index')
