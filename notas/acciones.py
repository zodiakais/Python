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
        
        for nota in notas:
            print("\n*****************************")
            print(f"TITULO: {nota[2]}")
            print(f"CONTENIDO:\n {nota[3]}")
            print("\n*****************************")
    def borrar(self,usuario):
        print("\nQUE NOTA VAS A ELIMINAR:")
        
        titulo = input("INTRODUCE EL TITULO DE LA NOTA HA BORRAR: ")
        
        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"SE HA ELIMINADO LA NOTA: {nota.titulo}")
        else:
            print("ERROR AL BORRAR LA NOTA, VUELVE A INTENTAR: ")