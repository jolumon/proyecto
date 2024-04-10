import sys
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtCore import Qt
from proveedores.view.ui_proveedor_detalle import Ui_Form
from auxiliares import VentanaEmergenteBorrar


class VentanaDetalle(QWidget, Ui_Form):
    def __init__(self, ventana_proveedor):
        super().__init__()

        self.setupUi(self)

        self.setWindowModality(Qt.ApplicationModal)
        self.ventana_proveedor = ventana_proveedor

        self.showMaximized()

    # Signals and Slots

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_borrar.clicked.connect(self.borrar_proveedor)
        self.btn_actualizar.clicked.connect(self.actualizar_proveedor)

    def closeEvent(self, event):
        # Cuando se cierra la ventana secundaria, se muestra la ventana principal
        self.ventana_proveedor.show()
        event.accept()

    def borrar_proveedor(self):

        ventana_confirmacion = VentanaEmergenteBorrar()
        respuesta = ventana_confirmacion.exec()

        if respuesta:

            codigo = int(self.le_codigo.text())
            print(f'Código:{codigo}')
            print(type(codigo))
            query = QSqlQuery()
            query.prepare(
                "DELETE FROM proveedores WHERE id_prov=:codigo")
            query.bindValue(":codigo", codigo)
            query.exec()

            self.limpiar_datos()
            self.ventana_proveedor.initial_query.exec("select * from proveedores where activo_prov=true order by id_prov")
            self.ventana_proveedor.model.setQuery(self.ventana_proveedor.initial_query)
        
            self.ventana_proveedor.tv_proveedores.selectRow(0)
            # self.ventana_proveedor.model.select()
            self.close()

    def limpiar_datos(self):
        self.le_codigo.setText("")
        self.le_nombre.setText("")
        self.le_direccion.setText("")
        self.le_codigo_postal.setText("")
        self.le_poblacion.setText("")
        self.le_provincia.setText("")
        self.le_telefono.setText("")
        self.le_contacto.setText("")
        self.le_movil.setText("")
        self.le_email.setText("")

    def actualizar_proveedor(self):

        codigo = int(
            self.le_codigo.text())  # Lo paso a entero para que coincida con el tipo de datos de la bd
        # codigo = self.model.index(fila, 0).data()->Aquí no conozco fila, tendría que hacerla global
        nombre = self.le_nombre.text()
        direccion = self.le_direccion.text()
        codigo_postal = self.le_codigo_postal.text()
        poblacion = self.le_poblacion.text()
        provincia = self.le_provincia.text()
        telefono = self.le_telefono.text()
        contacto = self.le_contacto.text()
        movil = self.le_movil.text()
        email = self.le_email.text()
        print(type(codigo))
        print(f'{codigo},{nombre},{direccion},{codigo_postal},{poblacion},{provincia},{telefono},{email},{contacto}')

        query = QSqlQuery()
        # query.prepare(
        #     "UPDATE clientes SET nombre_clientes=:nombre,direccion_clientes=:direccion,codigo_postal=:codigo_postal,"
        #     "poblacion=:poblacion,provincia=:provincia, telefono=:telefono,email=:email,contacto=:contacto"
        #     "WHERE id_clientes=:codigo")
        query.prepare(
            f'UPDATE proveedores SET nombre_prov=:nombre,direccion_prov=:direccion,cp_prov=:codigo_postal,poblacion_prov=:poblacion,provincia_prov=:provincia, telefono_prov=:telefono,contacto_prov=:contacto,movil_prov=:movil,email_prov=:email WHERE id_prov=:codigo')

        query.bindValue(":codigo", codigo)
        query.bindValue(":nombre", nombre)
        query.bindValue(":direccion", direccion)
        query.bindValue(":codigo_postal", codigo_postal)
        query.bindValue(":poblacion", poblacion)
        query.bindValue(":provincia", provincia)
        query.bindValue(":telefono", telefono)
        query.bindValue(":contacto", contacto)
        query.bindValue(":movil",movil)
        query.bindValue(":email", email)

        query.exec()

        self.close()

        self.ventana_proveedor.initial_query.exec("select * from proveedores where activo_prov=true order by id_prov")
        self.ventana_proveedor.model.setQuery(self.ventana_proveedor.initial_query)
        
        self.ventana_proveedor.tv_proveedores.selectRow(0)
        
