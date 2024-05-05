from PySide6.QtWidgets import QWidget

from productos.view.ui_ventana_producto_detalle3 import Ui_Form
from auxiliares import VentanaEmergenteBorrar
from PySide6.QtSql import QSqlQuery


class VentanaDetalle(QWidget, Ui_Form):
    def __init__(self, ventana_producto):
        super().__init__()
        self.setupUi(self)

        self.ventana_producto = ventana_producto

        self.showMaximized()

        # Mostrar equipos en el comboBox
        self.diccionario_equipos = {}

        query_equipos = QSqlQuery()
        query_equipos.prepare(
            f'select id_eq, nombre_eq from equipos where activo_eq = true order by id_eq')

        if query_equipos.exec():
            while query_equipos.next():
                equipo_id = query_equipos.value(0)
                nombre = query_equipos.value(1)
                self.cb_equipo_fab.addItem(nombre)
                self.diccionario_equipos[nombre] = equipo_id

        self.cb_equipo_fab.setCurrentIndex(-1)
        
        # Mostrar clientes en el comboBox
        
        self.diccionario_clientes_act = {}

        query_clientes_actualizar = QSqlQuery()
        query_clientes_actualizar.prepare(
            f'select id_cli, nombre_cli from clientes where activo_cli=true order by nombre_cli')

        if query_clientes_actualizar.exec():
            while query_clientes_actualizar.next():
                cliente_id = query_clientes_actualizar.value(0)
                nombre_cli = query_clientes_actualizar.value(1)
                self.cb_cliente.addItem(nombre_cli)
                self.diccionario_clientes_act[nombre_cli] = cliente_id
        
        
        

        # Signals and Slots

        self.btn_cerrar_det.clicked.connect(self.close)
        self.btn_cerrar_fab.clicked.connect(self.close)
        self.btn_borrar_det.clicked.connect(self.borrar_producto)
        self.btn_actualizar_det.clicked.connect(self.actualizar_producto)
        self.btn_imprimir_fab.clicked.connect(self.imprimir_fab)
        self.btn_add_fab.clicked.connect(self.add_fab)

    def closeEvent(self, event):
        # Cuando se cierra la ventana secundaria, se muestra la ventana principal
        self.ventana_producto.show()
        event.accept()

    def borrar_producto(self):
        print(f'Borrado')
        ventana_confirmacion = VentanaEmergenteBorrar()
        respuesta = ventana_confirmacion.exec()

        if respuesta:

            codigo = int(self.le_codigo_det.text())
            # print(type(codigo))
            query = QSqlQuery()
            query.prepare(
                "DELETE FROM productos WHERE id_prod=:codigo")
            # query.bindValue(":nombre", nombre)
            query.bindValue(":codigo", codigo)
            query.exec()

            self.ventana_producto.initial_query.exec(
                "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_cli  from productos p inner join clientes c on p.cliente_prod =c.id_cli  where p.activo_prod=true order by p.id_prod asc")
            self.ventana_producto.model.setQuery(
                self.ventana_producto.initial_query)

            self.close()
            self.ventana_producto.tabWidget.setCurrentIndex(1)
            self.ventana_producto.tv_productos.selectRow(0)

    def add_fab(self):
        
        codigo = int(self.le_codigo_det.text())

        self.de_fecha_fab.setDisplayFormat("dd-MM-yyyy")
        self.de_fecha_cad_fab.setDisplayFormat("dd-MM-yyyy")

        fecha_fab = self.de_fecha_fab.date().toString("dd-MM-yyyy")
        # print(f'{type(fecha_fab)}-{fecha_fab}')
        fecha_cad_fab = self.de_fecha_cad_fab.date().toString("dd-MM-yyyy")
        # print(f'{type(fecha_fab)}-{fecha_cad_fab}')
        lote = self.le_lote_fab.text()
        # print(f'{lote}')
        equipo = self.obtener_clave_principal_equipo()
        # print(f'{equipo}')
        cantidad = int(self.le_cantidad_fab.text())
        # print(f'{cantidad}')

        query_add_fab = QSqlQuery()
        query_add_fab.prepare(
            f'insert into fabricaciones (id_prod_fab,fecha_fab, lote_fab,fecha_cad_fab, equipo_fab, cantidad_fab ) values (:id_prod_fab,:fecha_fab, :lote_fab,:fecha_cad_fab, :equipo_fab, :cantidad_fab )')
        query_add_fab.bindValue(":id_prod_fab", codigo)
        query_add_fab.bindValue(":fecha_fab", fecha_fab)
        query_add_fab.bindValue(":lote_fab", lote)
        query_add_fab.bindValue(":fecha_cad_fab", fecha_cad_fab)
        query_add_fab.bindValue(":equipo_fab", equipo)
        query_add_fab.bindValue(":cantidad_fab", cantidad)

        # print(f'{codigo}-{str(self.de_fecha_fab.date().toString("dd/MM/yyyy"))}-{self.le_lote_fab.text()}-{str(self.de_fecha_cad_fab.date().toString())}-{self.cb_equipo_fab.currentText()}-{self.le_cantidad_fab.text()}')

        query_add_fab.exec()
        print('Añadida fabricación')

        self.ventana_producto.initial_query.exec(
            "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_cli  from productos p inner join clientes c on p.cliente_prod =c.id_cli  where p.activo_prod=true order by p.id_prod asc")
        self.ventana_producto.model.setQuery(
            self.ventana_producto.initial_query)

        self.close()
        self.ventana_producto.tabWidget.setCurrentIndex(1)
        self.ventana_producto.tv_productos.selectRow(0)

    def obtener_clave_principal_equipo(self):
        nombre_seleccionado = self.cb_equipo_fab.currentText()
        clave_principal = self.diccionario_equipos.get(nombre_seleccionado)

        print(f'Nombre seleccionado: {nombre_seleccionado}')
        print(f'Clave principal: {clave_principal}')

        return clave_principal

    def actualizar_producto(self):
        
        codigo = int(self.le_codigo_det.text())
        nombre = self.le_nombre_det.text()
        linea = self.le_linea_det.text()
        
        # Mostrar clientes en el comboBox
        self.diccionario_clientes_act = {}

        query_clientes_actualizar = QSqlQuery()
        query_clientes_actualizar.prepare(
            f'select id_cli, nombre_cli from clientes where activo_cli=true order by nombre_cli')

        if query_clientes_actualizar.exec():
            while query_clientes_actualizar.next():
                cliente_id = query_clientes_actualizar.value(0)
                nombre_cli = query_clientes_actualizar.value(1)
                self.cb_cliente.addItem(nombre_cli)
                self.diccionario_clientes_act[nombre_cli] = cliente_id
        
        # cliente = self.cb_cliente.currentText()
        
        
        cliente_ids = int(self.obtener_clave_principal())
        
        query_actualizar = QSqlQuery()
        query_actualizar.prepare(f'update productos set nombre_prod=:nombre,linea_prod=:linea, cliente_prod=:cliente_id where id_prod = :codigo')
        query_actualizar.bindValue(":nombre",nombre)
        query_actualizar.bindValue(":linea",linea)
        query_actualizar.bindValue(":cliente_id",cliente_ids)
        query_actualizar.bindValue(":codigo", codigo)
        
        query_actualizar.exec()
        
        print(f'Nombre:{nombre}')
        print(f'Linea:{linea}')
        print(f'Cliente_ids:{cliente_ids}')
        print(f'Cliente_id:{cliente_id}')
        print(f'Código: {codigo}')
        
        print(f'{type(nombre)}-{type(linea)}-{type(cliente_ids)}-{type(codigo)}')
        
        self.ventana_producto.initial_query.exec(
            "select p.id_prod,p.nombre_prod , p.linea_prod , c.nombre_cli  from productos p inner join clientes c on p.cliente_prod =c.id_cli  where p.activo_prod=true order by p.id_prod asc")
        self.ventana_producto.model.setQuery(
            self.ventana_producto.initial_query)

        self.close()
        self.ventana_producto.tabWidget.setCurrentIndex(1)
        self.ventana_producto.tv_productos.selectRow(0)
        
        
        
        
        
        
        
        
        
        
        print(f'Actualizado')
    
    def obtener_clave_principal(self):
        nombre_seleccionado = self.cb_cliente.currentText()
        clave_principal = self.diccionario_clientes_act.get(nombre_seleccionado)

        print(f'Nombre seleccionado: {nombre_seleccionado}')
        print(f'Clave principal: {clave_principal}')

        return clave_principal

    def imprimir_fab(self):
        print('Impresión realizada')
