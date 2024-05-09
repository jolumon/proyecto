from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class VentanaEmergenteBorrar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atención")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("¿Está seguro de la eliminación?"))

        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.botones.accepted.connect(self.accept)
        self.botones.rejected.connect(self.reject)

        self.layout.addWidget(self.botones)
        
class VentanaEmergenteVacio(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atención")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Se debe introducir un nombre"))

        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok)

        self.botones.accepted.connect(self.accept)
        # self.botones.rejected.connect(self.reject)

        self.layout.addWidget(self.botones)
    
class VentanaEmergenteFechaIncorrecta(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atención")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("La fecha de caducidad debe ser mayor que la fecha de entrada"))

        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok)

        self.botones.accepted.connect(self.accept)
        # self.botones.rejected.connect(self.reject)

        self.layout.addWidget(self.botones)

class VentanaEmergenteFaltaMPs(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atención")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Falta algun componente de la composicioñin"))

        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok)

        self.botones.accepted.connect(self.accept)
        # self.botones.rejected.connect(self.reject)

        self.layout.addWidget(self.botones)
        
class VentanaMPExistente(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atención")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Ya existe esta materia prima"))

        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok)

        self.botones.accepted.connect(self.accept)
        # self.botones.rejected.connect(self.reject)

        self.layout.addWidget(self.botones)