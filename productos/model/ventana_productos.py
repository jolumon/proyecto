from productos.view.ui_ventana_productos import Ui_Form
from productos.model.ventana_detalle_prod import VentanaDetalle
from PySide6.QtCore import Qt, QSortFilterProxyModel,QDate
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel, QSqlRelationalTableModel, QSqlRelation
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableView


class VentanaProducto(QWidget, Ui_Form):
    def __init__(self, ventana_principal):
        super().__init__()

        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()
        self.ventana_principal = ventana_principal

        # Crear un modelo de tabla

        self.initial_query = QSqlQuery()
        self.initial_query.exec(
            "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_cli  from productos p inner join clientes c on p.cliente_prod =c.id_cli  where p.activo_prod=true order by p.nombre_prod asc")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.initial_query)

        # Crear un model de tabla

        # self.model = QSqlTableModel()
        # self.model.setTable('productos')
        # self.model = QSqlRelationalTableModel()
        # self.model.setTable('productos')
        # self.model.setRelation(3,QSqlRelation("clientes", "id_clientes", "nombre_clientes"))

        # self.model.select()

        # self.model.setSort(0, Qt.AscendingOrder)  ->No ordena

        # No haría falta poner la siguiente linea pero es la única forma que sale ordenado
        # self.model.setQuery(
        #     "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_clientes  from productos p inner join clientes c on p.cliente_prod =c.id_clientes  where p.activo_prod=true order by p.id_prod asc ")
        self.model.setHeaderData(0, Qt.Horizontal, str("Código"))
        self.model.setHeaderData(1, Qt.Horizontal, str("Nombre"))
        self.model.setHeaderData(2, Qt.Horizontal, str("Linea"))
        self.model.setHeaderData(3, Qt.Horizontal, str("Cliente"))

        # Crear un filtro para la búsqueda
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Crear un cuadro de texto para la búsqueda

        self.le_buscar_prod.setPlaceholderText("Buscar por nombre...")
        self.le_buscar_prod.textChanged.connect(self.filter)

        # Crear una tabla para mostrar los datos
        self.tv_productos.setModel(self.proxy_model)

        self.tv_productos.setSelectionBehavior(QTableView.SelectRows)
        self.tv_productos.setSelectionMode(QTableView.SingleSelection)

        self.tv_productos.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
        # Seleccionar filas completas
        self.tv_productos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_productos.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Seleccionar filas completas

        # Configurar la vista de tabla
        self.tv_productos.resizeRowsToContents()
        self.tv_productos.resizeColumnsToContents()
        # Amplia el tamaño de la tabla a toda la pantalla
        self.tv_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tv_productos.selectRow(0)

    # Mostrar clientes en el comboBox
        self.diccionario_clientes = {}

        query_clientes = QSqlQuery()
        query_clientes.prepare(
            f'select id_cli, nombre_cli from clientes where activo_cli=true order by nombre_cli')

        if query_clientes.exec():
            while query_clientes.next():
                cliente_id = query_clientes.value(0)
                nombre = query_clientes.value(1)
                self.cb_cliente_prod.addItem(nombre)
                self.diccionario_clientes[nombre] = cliente_id

        self.cb_cliente_prod.setCurrentIndex(-1)

        # Signal and Slots pestaña listado productos
        self.btn_cerrar_listado.clicked.connect(self.close)
        self.btn_ver_prod_listado.clicked.connect(self.ver_detalle_producto)

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
        text = self.le_buscar_prod.text()
        # Usar setFilterFixedString en lugar de setFilterRegExp
        self.proxy_model.setFilterFixedString(text)
        # Filtrar por la columna "nombre_persona"
        self.proxy_model.setFilterKeyColumn(1)
        self.proxy_model.invalidate()  # Asegurarse de que el proxy model se actualice

    def ver_detalle_producto(self):
        # Se crea la ventana de detalle del cliente
        self.ventana_detalle = VentanaDetalle(self)
        selected_index = self.tv_productos.selectedIndexes()
        
        # print(f'Selected index: {selected_index}')
        if selected_index:

            row = selected_index[0].row()
            id_pers_index = self.proxy_model.mapToSource(selected_index[0])

            codigo = self.model.data(self.model.index(id_pers_index.row(), 0))
            nombre = self.model.data(self.model.index(id_pers_index.row(), 1))
            linea = self.model.data(
                self.model.index(id_pers_index.row(), 2))
            cliente = self.model.data(
                self.model.index(id_pers_index.row(), 3))

            print(f'Cliente:{cliente}')#Este cliente es correcto
            
            # establecemos los campos con los valores seleccionados
            self.ventana_detalle.le_codigo_det.setText(str(codigo))
            self.ventana_detalle.le_nombre_det.setText(nombre)
            self.ventana_detalle.le_linea_det.setText(linea)
            
    #         cliente_nombre_consulta=QSqlQuery()
    #         cliente_nombre_consulta.prepare(f'select nombre_clientes from clientes where id_clientes=:cliente')
    #         cliente_nombre_consulta.bindValue(":cliente",cliente)
            
    #         if cliente_nombre_consulta.exec_():
    # # Verificar si se obtuvieron resultados
    #             if cliente_nombre_consulta.next():
    #                 # Obtener el nombre del cliente
    #                 nombre_cliente = cliente_nombre_consulta.value(0)
    #                 print(f"Nombre del cliente con ID {cliente}: {nombre_cliente}")
    #             else:
    #                 print(f"No se encontró un cliente con ID {cliente}")
    #         else:
    #             # Manejar errores en la ejecución de la consulta
    #             print(f"Error en la consulta: {cliente_nombre_consulta.lastError().text()}")
            
            # cliente_nombre_consulta.exec()
            # cliente_cb_detalle= cliente_nombre_consulta.value(0)#No es correcto
            # print(f'Codigo cliente:{cliente_cb_detalle}')
            # self.ventana_detalle.cb_cliente.setCurrentText(cliente_cb_detalle)
            
            
            # self.ventana_detalle.cb_cliente.setCurrentText(str(cliente_nombre_consulta.value(0)))
            
            self.ventana_detalle.cb_cliente.setCurrentText(cliente)
            
            
            self.query_composicion = QSqlQuery()
            self.query_composicion.prepare(
                "select mp.nombre_mp,c.porcentaje_mp_comp from materias_primas mp inner join composiciones c on mp.id_mp = c.id_mp_comp inner join productos p on c.id_prod_comp = p.id_prod where p.id_prod = :codigo order by c.porcentaje_mp_comp desc")
            self.query_composicion.bindValue(':codigo', codigo)
            self.query_composicion.exec()

            # self.model2 = QSqlRelationalTableModel()

            self.model2 = QSqlQueryModel()
            self.model2.setQuery(self.query_composicion)

            self.model2.setHeaderData(0, Qt.Horizontal, str("Código"))
            self.model2.setHeaderData(1, Qt.Horizontal, str("Producto"))
            # self.model2.setHeaderData(2, Qt.Horizontal, str("Linea"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_composicion_prod.setModel(self.model2)
            self.ventana_detalle.tv_composicion_prod.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_composicion_prod.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_composicion_prod.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_composicion_prod.resizeRowsToContents()
            self.ventana_detalle.tv_composicion_prod.resizeColumnsToContents()
            self.ventana_detalle.tv_composicion_prod.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)

    
        # Ver las fabricaciones del producto en la pestaña Nueva Fabricación
        
            self.ventana_detalle.le_codigo_fab.setText(str(codigo))
            self.ventana_detalle.le_producto_fab.setText(nombre)
            fecha_entrada= QDate.currentDate()
            self.ventana_detalle.de_fecha_fab.setDate(
                fecha_entrada)
            
        
            self.query_fabricaciones = QSqlQuery()
            # self.query_fabricaciones.prepare(
            #     "select f.fecha_fab ,f.lote_fab ,f.cantidad_fab  ,f.fecha_cad_fab,e.nombre_eq  from productos p inner join fabricaciones f on p.id_prod = f.id_prod_fab inner join equipos e on f.equipo_fab = e.id_eq where p.id_prod = :codigo order by f.fecha_fab desc")
            self.query_fabricaciones.prepare(
                """select of2.fecha_ofab ,p.nombre_prod,of2.lote_ofab ,of2.cantidad_ofab ,e.nombre_eq  from ordenes_fab of2 
                    inner join productos p on of2.id_prod_ofab =p.id_prod
                    inner join equipos e on e.id_eq =of2.equipo_ofab 
                    where of2.id_prod_ofab = 1 
                    order by of2.fecha_ofab desc""")
            self.query_fabricaciones.bindValue(':codigo', codigo)
            self.query_fabricaciones.exec()
#                select f.fecha_fab ,f.lote_fab ,f.cantidad_fab  ,f.fecha_cad_fab,e.nombre_eq  from productos p inner join fabricaciones f on p.id_prod = f.id_prod_fab inner join equipos e on f.equipo_fab = e.id_eq where p.id_prod = 1 order by f.fecha_fab desc
            # self.model2 = QSqlRelationalTableModel()

            self.model_fab = QSqlQueryModel()
            self.model_fab.setQuery(self.query_fabricaciones)

            self.model_fab.setHeaderData(0, Qt.Horizontal, str("Fecha fabricación"))
            self.model_fab.setHeaderData(1, Qt.Horizontal, str("Producto"))
            self.model_fab.setHeaderData(2, Qt.Horizontal, str("Lote"))
            self.model_fab.setHeaderData(3, Qt.Horizontal, str("Cantidad"))
            # self.model_fab.setHeaderData(3, Qt.Horizontal, str("Caducidad"))
            self.model_fab.setHeaderData(4, Qt.Horizontal, str("Equipo"))
            # self.model2.setHeaderData(2, Qt.Horizontal, str("Linea"))

            # Crear una vista de tabla
            self.ventana_detalle.tv_fab_historico.setModel(self.model_fab)
            self.ventana_detalle.tv_fab_historico.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
            self.ventana_detalle.tv_fab_historico.setSelectionMode(
                QAbstractItemView.SingleSelection)  # Seleccionar filas completas
            self.ventana_detalle.tv_fab_historico.setSelectionBehavior(
                QAbstractItemView.SelectRows)  # Seleccionar filas completas

            # Configurar la vista de tabla
            self.ventana_detalle.tv_fab_historico.resizeRowsToContents()
            self.ventana_detalle.tv_fab_historico.resizeColumnsToContents()
            self.ventana_detalle.tv_fab_historico.horizontalHeader(
            ).setSectionResizeMode(QHeaderView.Stretch)
        
        
    

            self.ventana_detalle.show()

            self.hide()
            # Se puede quitar el else-->Habrá que hacerlo
        else:
            print('No entra en if del selected_index')

    def obtener_clave_principal(self):
        nombre_seleccionado = self.cb_cliente_prod.currentText()
        clave_principal = self.diccionario_clientes.get(nombre_seleccionado)

        print(f'Nombre seleccionado: {nombre_seleccionado}')
        print(f'Clave principal: {clave_principal}')

        return clave_principal

    def guardar_nuevo(self):
        # Recuperar datos de los lineEdit
        nombre = self.le_nombre_prod.text()
        linea = self.le_linea_prod.text()
        cliente_id = int(self.obtener_clave_principal())

        # Crear y preparacion de la sentencia sql
        query = QSqlQuery()
        query.prepare(
            f'insert into productos (nombre_prod,linea_prod, cliente_prod) values (:nombre, :linea,:cliente_id)')

        query.bindValue(":nombre", nombre)
        query.bindValue(":linea", linea)
        query.bindValue(":cliente_id", cliente_id)

        query.exec()

        # Limpiar datos introducidos
        self.le_nombre_prod.setText("")
        self.le_linea_prod.setText("")
        self.cb_cliente_prod.setCurrentIndex(-1)
        # Cambiar a la pestaña de listado productos
        self.tabWidget.setCurrentIndex(1)

        self.initial_query.exec(
                "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_cli  from productos p inner join clientes c on p.cliente_prod =c.id_cli  where p.activo_prod=true order by p.id_prod asc")
        self.model.setQuery(self.initial_query)
        

        # No hay forma de actualizar el tableView de productos. No funciona nada de lo que
        # a continuación indico:
        # self.model.select()->No salen los datos.tableView en blanco
        # self.proxy_model.invalidate()->No observo nada. Salen los datos pero sin el último introducido
