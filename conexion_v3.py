from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Conexion:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setDatabaseName('laberp_v3')
        self.db.setHostName('localhost')
        #self.db.setHostName(DATABASE_URL)
        self.db.setPort(5432)
        self.db.setUserName('')
        self.db.setPassword('')
       
    
    def conectar(self):
        if self.db.open()==True:
            print('Base de datos abierta correctamente')

            return True
        else:
            print("Error al conectar a la base de datos")
            print(self.db.lastError().text())

            return False

    def desconectar(self):
        self.db.close()
        if self.db.isOpen()==False:
            print('Base de datos cerrada correctamente')
            return True
        else:
            
            print('Sigue abierta')
            print(self.db.lastError().text())
            
            return False
