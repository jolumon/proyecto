from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Conexion:
    def __init__(self):
        #DATABASE_URL='postgresql://postgres:7taYLsi4hFrE@ep-wandering-sound-a2wgvsk5.eu-central-1.aws.neon.tech/labERP_dam?sslmode=require'
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setDatabaseName('laberp2')
        self.db.setHostName('localhost')
        #self.db.setHostName(DATABASE_URL)
        self.db.setPort(5432)
        self.db.setUserName('postgres')
        self.db.setPassword('postgres')
       
    # DATABASE_URL=postgres://[user]:[password]@[neon_hostname]/[dbname]?sslmode=require
    # postgresql://postgres:7taYLsi4hFrE@ep-wandering-sound-a2wgvsk5.eu-central-1.aws.neon.tech/labERP_dam?sslmode=require
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
