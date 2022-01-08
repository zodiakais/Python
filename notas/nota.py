import datetime
import re
import usuarios.conexion as conexion

connect = conexion.conexion()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self,usuario_id,titulo="",descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    def guardar(self):
        
        sql = "INSERT INTO notes VALUES(null,%s,%s,%s,NOW())"
        nota = (self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        
        return [cursor.rowcount,self]
    def listar(self):
        
        sql = f"SELECT * FROM notes WHERE USER_ID={self.usuario_id}"
        result = cursor.fetchall()
        
        return result
        