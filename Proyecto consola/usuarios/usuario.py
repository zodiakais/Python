import datetime
import hashlib
import usuarios.conexion as conexion
connect = conexion.conexion()
database = connect[0]
cursor = connect[1]


class Usuario:
    
    ### CONTRUCTOR
    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        
    def registro(self):
        fecha = datetime.datetime.now()
        ###CIFRADO DE CONTRASEÑA CON HASHLIB
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))
        sql = "INSERT INTO users VALUES(null,%s,%s,%s,%s,%s)"
        users= (self.nombre,self.apellido,self.email,cifrado.hexdigest(),fecha)
        try:
            cursor.execute(sql,users)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result=[0,self]
            
        return [cursor.rowcount,self]
    
    def identificar(self):
        ###CONSULTAMOS LA EXISTENCIA DEL USUARIO
        
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
         
        ###CIFRADO DE CONTRASEÑA CON HASHLIB
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))
        
        ###DATOS PARA LA CONSULTA
        usuario = (self.email,cifrado.hexdigest())
        
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        
         
        return result