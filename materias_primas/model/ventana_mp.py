from typing import Optional
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableView 
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel
from PySide6.QtCore import Qt, QSortFilterProxyModel,QDate
from materias_primas.view.ui_materias_primas import Ui_Form
from materias_primas.model.ventana_detalle_mp import VentanaDetalle



class VentanaMateriasPrimas(QWidget, Ui_Form):
    def __init__(self, ventana_principal):
        super().__init__()
        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()
        self.ventana_principal = ventana_principal

        # Crear un modelo de tabla

        self.model = QSqlTableModel()
        self.model.setTable('materias_primas')

        self.model.select()

        self.model.setQuery(
            "SELECT * FROM materias_primas where activo_mp=true order by id_mp asc")
        self.model.setHeaderData(0, Qt.Horizontal, str("Código"))
        self.model.setHeaderData(1, Qt.Horizontal, str("Nombre"))
        self.model.setHeaderData(2, Qt.Horizontal, str("Cantidad total / kg"))
        # self.model.setHeaderData(3, Qt.Horizontal, str("Proveedor"))
        self.model.setHeaderData(3, Qt.Horizontal, str("Activo"))

 # Crear un filtro para la búsqueda
        self.proxy_model_mp = QSortFilterProxyModel()
        self.proxy_model_mp.setSourceModel(self.model)

        # Crear un cuadro de texto para la búsqueda

        self.le_buscar_mp.setPlaceholderText("Buscar por nombre...")
        self.le_buscar_mp.textChanged.connect(self.filter)

        # Crear una tabla para mostrar los datos

        self.tv_mat_primas.setModel(self.proxy_model_mp)
        self.tv_mat_primas.setSelectionBehavior(QTableView.SelectRows)
        self.tv_mat_primas.setSelectionMode(QTableView.SingleSelection)

        # Crear la vista de tabla y establecer el modelo
        # self.tv_mat_primas.setModel(self.model)
        self.tv_mat_primas.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
        self.tv_mat_primas.setSelectionMode(
            QAbstractItemView.SingleSelection)  # Seleccionar filas completas
        self.tv_mat_primas.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Seleccionar filas completas
        self.tv_mat_primas.selectRow(0)
        # Configurar la vista de tabla
        self.tv_mat_primas.resizeColumnsToContents()
        self.tv_mat_primas.resizeRowsToContents()
        self.tv_mat_primas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Mostrar proveedores en el comboBox
        self.diccionario_proveedores = {}

        query_proveedores = QSqlQuery()
        query_proveedores.prepare(
            f'select id_prov, nombre_prov from proveedores order by id_prov')

        if query_proveedores.exec():
            while query_proveedores.next():
                proveedor_id = query_proveedores.value(0)
                nombre = query_proveedores.value(1)
                self.cb_proveedor_nueva.addItem(nombre)
                self.diccionario_proveedores[nombre] = proveedor_id

        self.cb_proveedor_nueva.setCurrentIndex(-1)

        # Signal and Slots para pestaña Nueva
        self.btn_guardar_nueva_mp.clicked.connect(self.guardar_nueva_mp)
        self.btn_cancelar_nueva_mp.clicked.connect(self.cambia_pestaña)

        # Signal and Slots para pestaña Listado
        self.btn_ver_detalle_mp.clicked.connect(self.ver_detalle_producto)
        self.btn_cerrar_listado_mp.clicked.connect(self.close)

    def filter(self):
        text = self.le_buscar_mp.text()
        # Usar setFilterFixedString en lugar de setFilterRegExp
        self.proxy_model_mp.setFilterFixedString(text)
        # Filtrar por la columna "nombre_persona"
        self.proxy_model_mp.setFilterKeyColumn(1)
        self.proxy_model_mp.invalidate()  # Asegurarse de que el proxy model se actualice

    def ver_detalle_producto(self):

        self.ventana_detalle = VentanaDetalle(self)
        selected_index = self.tv_mat_primas.currentIndex()
        print(f'Selected index: {selected_index}')
        if selected_index.isValid():
            # Obtenemos el número de fila de la celda seleccionada
            # print('Entra en el if del selected_index')
            fila = selected_index.row()
            print(f'Fila: {fila}')

            codigo = self.model.index(fila, 0).data()
            nombre = self.model.index(fila, 1).data()
            cantidad = self.model.index(fila, 2).data()
            # proveedor = self.model.index(fila, 3).data()

            # establecemos los campos con los valores seleccionados
            self.ventana_detalle.le_codigo_det.setText(str(codigo))
            self.ventana_detalle.le_nombre_det.setText(nombre)
            self.ventana_detalle.le_cantidad_det.setText(str(cantidad))
            # self.ventana_detalle.le_proveedor_det.setText(str(proveedor))
            
            self.ventana_detalle.le_codigo_entrada.setText(str(codigo))
            self.ventana_detalle.le_nombre_entrada.setText(nombre)
            # self.ventana_detalle.le_cantidad_entrada.setText(str(cantidad))
            # self.ventana_detalle.le_proveedor_entrada.setText(str(proveedor))
            self.ventana_detalle.le_f_entrada.setText(str(QDate.currentDate().toString('dd-MM-yyyy')))
            
            

            self.query_productos = QSqlQuery()
            self.query_productos.prepare(
                "SELECT productos.id_prod,productos.nombre_prod, productos.linea_prod FROM productos INNER JOIN clientes on productos.cliente_prod=clientes.id_cli WHERE id_cli=:codigo ORDER BY productos.id_prod")
            self.query_productos.bindValue(':codigo', codigo)
            self.query_productos.exec()

            # Se crea el modelo para mostrar los datos de las entradas del producto seleccionado
            self.model3 = QSqlQueryModel()
            self.model3.setQuery(
                f'select e.fecha_ent_ent , e.lote_ent ,e.fecha_cad_ent ,e.cantidad_ent ,e.precio_ent ,p.nombre_prov from materias_primas mp inner join entradas e on mp.id_mp = e.id_mp_ent inner join proveedores p on p.id_prov = e.id_prov_ent where mp.id_mp = {codigo}')

            self.model3.setHeaderData(0, Qt.Horizontal, str("Fecha Entrada"))
            self.model3.setHeaderData(1, Qt.Horizontal, str("Lote"))
            self.model3.setHeaderData(2, Qt.Horizontal, str("Fecha Caducidad"))
            self.model3.setHeaderData(3, Qt.Horizontal, str("Cantidad / kg"))
            self.model3.setHeaderData(4, Qt.Horizontal, str("Precio"))
            self.model3.setHeaderData(5, Qt.Horizontal, str("Proveedor"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_entradas_mp_det.setModel(self.model3)
            self.ventana_detalle.tv_entradas_mp_det.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_entradas_mp_det.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_entradas_mp_det.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_entradas_mp_det.resizeRowsToContents()
            self.ventana_detalle.tv_entradas_mp_det.resizeColumnsToContents()
            self.ventana_detalle.tv_entradas_mp_det.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)

            self.ventana_detalle.show()

            self.hide()
            # Se puede quitar el else-->Habrá que hacerlo
        else:
            print('No entra en if del selected_index')

        print(f'Dentro de ver_detalle_producto')

    def obtener_clave_principal(self):
        nombre_seleccionado = self.cb_proveedor_nueva.currentText()
        clave_principal = self.diccionario_proveedores.get(nombre_seleccionado)

        print(f'Nombre seleccionado: {nombre_seleccionado}')
        print(f'Clave principal: {clave_principal}')

        return clave_principal

    def cambia_pestaña(self):
        self.tabWidget.setCurrentIndex(0)

    def closeEvent(self, event):
        # Cuando se cierra la ventana secundaria, se muestra la ventana principal
        self.ventana_principal.show()
        event.accept()

    def guardar_nueva_mp(self):
        # Recuperar datos de los lineEdit y comboBox
        nombre = self.le_nombre_nueva.text()
        # cantidad = self.ventana_nueva_materia_prima.le_cantidad.text()

        proveedor = int(self.obtener_clave_principal())

        # Crear y preparacion de la sentencia sql
        query = QSqlQuery()
        query.prepare(
            f'insert into materias_primas (nombre_mp,cantidad_mp, proveedor_mp) values (:nombre, :cantidad,:proveedor)')

        query.bindValue(":nombre", nombre)
        # query.bindValue(":cantidad", cantidad)
        query.bindValue(":proveedor", proveedor)

        query.exec()

        self.tabWidget.setCurrentIndex(0)
        self.model.select()

        self.le_nombre_nueva.setText('')
        self.cb_proveedor_nueva.setCurrentIndex(-1)