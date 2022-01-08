import notas.nota as modelo
class Acciones:
    def crear(self,usuario):
        print(f"CREANDO NOTA DE {usuario[1]}")
        titulo = input("INTRODUCE EL TITULO:")
        descripcion = input("CONTENIDO DE LA NOTA:\n")
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nSE HA INGRESADO LA NOTA CON EXITO: {nota.titulo}")
        else:
            print("\nHA OCURRIDO UN ERROR AL CREAR UNA NOTA")
    def mostrar(self,usuario):
        print(f"ESTAS SON LAS NOTAS DE {usuario[1]}")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        print(notas)