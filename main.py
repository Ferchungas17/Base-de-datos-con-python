from config.db import Database
from services.usuario_service import UsuarioService
from services.tarea_service import TareaService

from models.usuario import Usuario
from models.tarea import Tarea

def menu_tareas(service:TareaService):
    while True:
        print(" --- CRUD TAREAS ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Volver")
        
        opcion = input("opcion")

        if opcion == "1":
            titulo = input("Titulo:")
            descripcion = input("Descripcion: ")
            usuario_id = int(input("ID Usuario: "))
            service.crear_tarea(Tarea(titulo, descripcion, usuario_id))

        elif opcion == "2":
            tareas = service.listar_tarea()
            for t in tareas:
                print(f"{t[0]} | {t[1]} | {t[2]} | Usuario: {t[3]}")

        elif opcion == "3":
            id = int(input("ID tarea: "))
            titulo= input("Nuevo titulo: ")
            descripcion = input("Nueva descripcion: ")
            usuario_id = int(input("Nuevo ID usuario: "))
            service.actualizar_tarea(Tarea(titulo, descripcion, usuario_id, id))

        elif opcion == "4":
            id= int(input("ID tarea a eliminar: "))
            service.eliminar_tarea(id)

        elif opcion =="5":
            break



def main():
    db = Database()
    db.connect()

    #servicios
    usuario_service = UsuarioService(db)
    tarea_service = TareaService(db)

    while True:
        print("--- SISTEMA CRUD ---") 
        print("1. usuarios")
        print("2. Tareas")
        print("3. Salir")
        opcion = input("Opcion: ")

      #Codigo original usuarios  
        if opcion =="1":
            while True:
                print("--- CRUD Usuarios ---")
                print("1. Crear")
                print("2. Listar")
                print("3. Actualizar")
                print("4. Eliminar")
                print("5. Salir")
                
                op = input("Opción: ")
                
                if op == "1":
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    usuario = Usuario(nombre, email)
                    usuario_service.crear_usuario(usuario)

                elif op == "2":
                    usuarios = usuario_service.listar_usuario()
                    for u in usuarios:
                        print(u)

                elif op == "3":
                    id = int(input("ID: "))
                    nombre = input("Nuevo nombre: ")
                    email = input("Nuevo email: ")
                    usuarios = usuario(nombre, email, id)
                    usuario_service.actualizar_Usuario(usuario)

                elif op == "4":
                    id = int(input("ID a eliminar: "))
                    usuario_service.eliminar_usuario(id)

                elif op == "5":
                    db.close()
                    break
        #Nuevo: Tareas
        elif opcion == "2":
            menu_tareas(tarea_service)
        elif opcion == "3":
            db.close()
            break
        
        else:
            print("opcion invalida")


if __name__ == "__main__":
    main()