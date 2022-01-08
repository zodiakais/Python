from logging import exception
import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nINICIANDO REGISTRO DE USUARIO:")
        nombre = input("INGRESA TU NOMBRE:" )
        apellido = input("INGRESA TU APELLIDO: ")
        email = input("INGRESA TU EMAIL: ")
        password = input("INGRESA TU CONTRASEÑA: ") 
        
        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registro()
        
        if registro[0] >=1:
            print(f"LISTO! {registro[1].nombre} TE HAS REGISTRADO CON CORREO: {registro[1].email}")
        else:
            print("NO ES POSIBLE REGISTRAR TU CUENTA")
    def login(self):
        print("INICIANDO APLICACION")
        try:
            email = input("INGRESA TU EMAIL: ")
            password = input("INGRESA TU CONTRASEÑA: ")
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"BIENVENIDO {login[1]}, FECHA DE REGISTRO: {login[5]}")
                self.siguienteAccion(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"ERROR AL INGRESAR, VUELVE A INTENTARLO: {type(e).__name__}")
    def siguienteAccion(self,usuario):
        print('''
            ACCIONES DISPONIBLES:
            -CREAR NOTA (CREAR)
            -MOSTRAR NOTAS(MOSTRAR)
            -ELIMINAR NOTAS(ELIMINAR)  
            -SALUR
            ''')
        
        accion = input("\nINGRESA UNA OPCION: ")
        do = notas.acciones.Acciones()
        
        if accion == "CREAR":
            print("CREAR")
            do.crear(usuario)    
            self.siguienteAccion(usuario)
        elif accion == "MOSTRAR":
            print("LISTADO DE NOTAS")
            do.mostrar()
            self.siguienteAccion(usuario)
        elif accion == "ELIMINAR":
            print("QUE NOTA VAS A ELIMINAR:")
            self.siguienteAccion(usuario)
        elif accion == "SALIR":
            print(f"HASTA PRONTO {usuario[1]}")
            exit()