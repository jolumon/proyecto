from PySide6.QtSql import QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QMessageBox
from materias_primas.view.ui_materias_primas_detalle2 import Ui_Form
from PySide6.QtCore import Qt


class VentanaDetalle(QWidget, Ui_Form):
    def __init__(self, ventana_mp):
        super().__init__()
        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()

        self.ventana_mp = ventana_mp
        
        # Mostrar proveedores en el comboBox de la pestaña entrada
        self.diccionario_proveedores_entrada = {}

        query_proveedores_entrada = QSqlQuery()
        query_proveedores_entrada.prepare(
            f'select id_prov, nombre_prov from proveedores order by nombre_prov')

        if query_proveedores_entrada.exec():
            while query_proveedores_entrada.next():
                proveedor_id = query_proveedores_entrada.value(0)
                nombre = query_proveedores_entrada.value(1)
                self.cb_proveedor_entrada.addItem(nombre)
                self.diccionario_proveedores_entrada[nombre] = proveedor_id

        self.cb_proveedor_entrada.setCurrentIndex(-1)

        # Signals and Slots pestaña detalle

        self.btn_cerrar_det.clicked.connect(self.close)
        self.btn_borrar_det.clicked.connect(self.borrar_mp)
        self.btn_actualizar_det.clicked.connect(self.actualizar_det)

        # Signals and Slots pestaña entrada

        self.btn_cerrar_entrada.clicked.connect(self.cierra_pest_entrada)
        self.btn_guardar_entrada.clicked.connect(self.guardar_entrada)

    def cierra_pest_entrada(self):
        print(f'Dentror de cierra_pestaña_entrada')
        self.tabWidget.setCurrentIndex(0)

    def obtener_clave_principal(self):
        nombre_seleccionado = self.cb_proveedor_entrada.currentText()
        clave_principal = self.diccionario_proveedores_entrada.get(nombre_seleccionado)

        print(f'Nombre seleccionado: {nombre_seleccionado}')
        print(f'Clave principal: {clave_principal}')

        return clave_principal

    def guardar_entrada(self):
        """ Guarda el registro de una nueva entrada en la base de datos """

        id_materia_prima = int(self.le_codigo_entrada.text())
        
        # Hay que hacer un comboBox para que se pueda elegir el proveedor. Antes al ser solo un proveedor venia impuesto y no hacia falta seleccionarlo porque se ponia por defecto .
        
        
        
        id_proveedor = int(self.obtener_clave_principal())
        print(f'id_proveedor: {id_proveedor}')
        fecha_entrada = str(self.le_f_entrada.text())
        fecha_caducidad = str(self.de_f_caducidad.text())
        lote = self.le_lote_entrada.text()
        if self.le_cantidad_entrada.text() == "":
            self.le_cantidad_entrada.setText('0')
        cantidad = int(self.le_cantidad_entrada.text())
        precio = self.le_precio_entrada.text()

        query_insertar_nueva_entrada = QSqlQuery()
        query_insertar_nueva_entrada.prepare(
            f'insert into entradas (id_mp_ent,id_prov_ent,lote_ent,fecha_ent_ent,fecha_cad_ent,cantidad_ent,precio_ent) values (:id_materia_prima,:id_proveedor,:lote,:fecha_entrada,:fecha_caducidad,:cantidad,:precio)'
        )

        query_insertar_nueva_entrada.bindValue(
            ':id_materia_prima', id_materia_prima)
        query_insertar_nueva_entrada.bindValue(
            ':id_proveedor', id_proveedor)
        query_insertar_nueva_entrada.bindValue(
            ':fecha_entrada', fecha_entrada)
        query_insertar_nueva_entrada.bindValue(
            ':fecha_caducidad', fecha_caducidad)
        query_insertar_nueva_entrada.bindValue(':lote', lote)
        query_insertar_nueva_entrada.bindValue(':cantidad', cantidad)
        query_insertar_nueva_entrada.bindValue(':precio', precio)
        print(
            f'{id_materia_prima}-{id_proveedor}-{lote}-"{fecha_entrada}"-{fecha_caducidad}-{cantidad}-{precio}')
        print(type(id_materia_prima))
        print(type(id_proveedor))
        print(type(lote))
        print(type(fecha_entrada))
        print(type(fecha_caducidad))
        print(type(cantidad))
        print(type(precio))

        query_insertar_nueva_entrada.exec()
        print('Guardado')

        # Si muestro la pestaña 1 para que se vean lso datos de la entrada introducida, 
        # no sé cómo actualizar la vista de la tableView
        # self.tabWidget.setCurrentIndex(0)
        self.close()
        
        

    def borrar_mp(self):

        codigo = int(self.le_codigo_det.text())
        # print(type(codigo))
        query = QSqlQuery()
        query.prepare(
            "DELETE FROM materias_primas WHERE id_mp=:codigo")
        # query.bindValue(":nombre", nombre)
        query.bindValue(":codigo", codigo)
        query.exec()

        self.ventana_mp.model.select()

        self.close()
        # self.tabWidget.setCurrentIndex(0)
        # self.tableView.selectRow(0)

    def closeEvent(self, event):
        # Cuando se cierra la ventana secundaria, se muestra la ventana principal
        self.ventana_mp.show()
        event.accept()

    def actualizar_det(self):
        codigo = int(
            self.le_codigo_det.text())  # Lo paso a entero para que coincida con el tipo de datos de la bd
        # codigo = self.model.index(fila, 0).data()->Aquí no conozco fila, tendría que hacerla global
        nombre = self.le_nombre_det.text()
        cantidad = self.le_cantidad_det.text()
        proveedor = int(self.le_proveedor_det.text())

        print(type(codigo))
        print(f'{codigo},{nombre},{cantidad},{proveedor}')

        query = QSqlQuery()

        query.prepare(
            f'UPDATE materias_primas SET nombre_mp=:nombre,cantidad_mp=:cantidad, proveedor_mp=:proveedor WHERE id_mp=:codigo')

        query.bindValue(":codigo", codigo)
        query.bindValue(":nombre", nombre)
        query.bindValue(":cantidad", cantidad)
        query.bindValue(":proveedor", proveedor)

        query.exec()

        self.ventana_mp.model.select()

        self.close()

    def muestra_entradas_materia_prima(self):
        codigo = int(self.le_codigo.text())
        print(f'Código: {codigo}')
        self.model = QSqlQueryModel()
        self.model.setQuery(
            f'select e.fecha_ent_ent , e.lote_ent ,e.fecha_cad_ent ,e.cantidad_ent ,e.precio_ent ,p.nombre_prov from materias_primas mp inner join entradas e on mp.id_mp = e.id_mp_ent inner join proveedores p on p.id_prov = e.id_prov_ent where mp.id_mp = {codigo}')

        self.model.setHeaderData(0, Qt.Horizontal, str("Fecha Entrada"))
        self.model.setHeaderData(1, Qt.Horizontal, str("Lote"))
        self.model.setHeaderData(2, Qt.Horizontal, str("Fecha Caducidad"))
        self.model.setHeaderData(3, Qt.Horizontal, str("Cantidad / kg"))
        self.model.setHeaderData(4, Qt.Horizontal, str("Precio"))
        self.model.setHeaderData(5, Qt.Horizontal, str("Proveedor"))

        # Crear una vista de tabla
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Deshabilitar edición
        # Seleccionar filas completas
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Seleccionar filas completas

        # Configurar la vista de tabla
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)