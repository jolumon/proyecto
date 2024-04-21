import sys

from clientes.model.ventana_clientes import VentanaCliente
from materias_primas.model.ventana_mp import VentanaMateriasPrimas
from proveedores.model.ventana_proveedores import VentanaProveedor
from productos.model.ventana_productos import VentanaProducto
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Qt
from ui_ventana_principal4 import Ui_MainWindow
from conexion import Conexion
# from qt_material import apply_stylesheet


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana de bienvenida del proyecto
        Muestra 4 botones que al pulsar sobre cualquiera de ellos
        mostrará el módulo en cuestión en una nueva ventana"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Principal: labERP")
        self.showMaximized()

        self.conexion = Conexion()
        self.conexion.conectar()

        # Signals and Slots

        self.btn_clientes.clicked.connect(self.ventana_clientes)
        self.btn_materias_primas.clicked.connect(self.ventana_materias_primas)
        self.btn_productos.clicked.connect(self.ventana_productos)
        self.btn_proveedores.clicked.connect(self.ventana_proveedores)

    def ventana_clientes(self):
        """
        Crea una ventana del tipo VentanaCliente y la muestra. Oculta la ventana principal.
        """
        # self.hide()
        self.ventana_cliente = VentanaCliente(self)
        self.ventana_cliente.show()
        self.hide()

    def ventana_materias_primas(self):
        """
        Crea una ventana del tipo VentanaMateriasPrimas y la muestra. Oculta la ventana principal.
        """
        # self.hide()
        self.ventana_materia_prima = VentanaMateriasPrimas(self)
        self.ventana_materia_prima.show()
        self.hide()

    def ventana_productos(self):
        """
        Crea una ventana del tipo VentanaProducto y la muestra. Oculta la ventana principal.
        """
        self.ventana_producto = VentanaProducto(self)
        self.ventana_producto.show()
        self.hide()

    def ventana_proveedores(self):
        """
        Crea una ventana del tipo VentanaProveedor y la muestra. Oculta la ventana principal.
        """
        self.ventana_proveedor = VentanaProveedor(self)
        self.ventana_proveedor.show()
        self.hide()

    def closeEvent(self, event):
        """Cuando se cierra la ventana principal, se cierra la conexion."""
        event.accept()
        self.conexion.desconectar()


if __name__ == '__main__':
    app = QApplication([])
    # apply_stylesheet(app,theme="light_lightgreen.xml")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
