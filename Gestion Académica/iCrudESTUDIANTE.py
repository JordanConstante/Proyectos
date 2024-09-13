from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla, gotoxy, red_color, reset_color, green_color, yellow_color
from clsJson import JsonFile
from estudiante import Estudiante
import time
import os

path, file = os.path.split(__file__)

class CrudEstudiante(ICrud):
    json_file = JsonFile(f"{path}/archivos/Estudiantes.json")

    def create(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{green_color}********** Crear nuevo Estudiante **********{reset_color}")
        estudiantes = self.json_file.read()
        id_estudiante = max([estudiante["Id"] for estudiante in estudiantes], default=0) + 1
        gotoxy(10, 4); nombre = input(f"{yellow_color}Ingrese el nombre del estudiante: {reset_color}")
        gotoxy(10, 5); active = input(f"{yellow_color}El estudiante está activo? (si/no): {reset_color}").lower()
        active = True if active == 'si' else False
        estudiante_nuevo = Estudiante(id_estudiante, nombre, active)
        estudiantes.append(estudiante_nuevo.getJson())
        self.json_file.save(estudiantes)

        gotoxy(40, 7); print(f"{green_color}Estudiante Creado exitosamente!{reset_color}")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Actualización de Estudiante **********{reset_color}")
        estudiantes = self.json_file.read()
        if estudiantes:
            gotoxy(10, 4); id_estudiante = int(input(f"{yellow_color}Ingrese el ID del estudiante: {reset_color}"))
            for estudiante in estudiantes:
                if estudiante['Id'] == id_estudiante:
                    # Mostrar la información actual del estudiante
                    gotoxy(10, 6); print(f"{green_color}Estudiante: {estudiante['Id']}   Nombre: {estudiante['Nombre']}   Activo: {estudiante['Active']}{reset_color}")
                    
                    # Solicitar los nuevos datos
                    gotoxy(10, 8); estudiante['Nombre'] = input(f"{yellow_color}Ingrese el nombre del estudiante: {reset_color}")
                    gotoxy(10, 9); active = input(f"{yellow_color}El estudiante está activo? (si/no): {reset_color}").lower()
                    active = True if active == 'si' else False
                    estudiante['Active'] = active
                    
                    # Guardar el estudiante actualizado
                    self.json_file.save(estudiantes)
                    gotoxy(40, 11); print(f"{green_color}Estudiante actualizado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 12); print(f"{red_color}El estudiante no se encuentra en la base de datos...{reset_color}")
                time.sleep(1)
        else:
            gotoxy(10, 12); print(f"{red_color}No hay estudiantes registrados...{reset_color}")
            time.sleep(1)

    def delete(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Eliminación de Estudiante **********{reset_color}")
        estudiantes = self.json_file.read()
        if estudiantes:
            gotoxy(10, 4); id_estudiante = int(input(f"{yellow_color}Ingrese el ID del estudiante: {reset_color}"))
            for estudiante in estudiantes:
                if estudiante['Id'] == id_estudiante:
                    estudiantes.remove(estudiante)
                    self.json_file.save(estudiantes)
                    gotoxy(35, 6); print(f"{green_color}Estudiante con ID: {id_estudiante} eliminado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 7); print(f"{red_color}El estudiante no se encuentra en la base de datos...{reset_color}")
                time.sleep(2)
        else:
            gotoxy(10, 4); print(f"{red_color}No hay estudiantes en el registro.{reset_color}")
            time.sleep(2)

    def consult(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Consultar Estudiantes **********{reset_color}")
        estudiantes = self.json_file.read()
        if estudiantes:
            gotoxy(35, 4); print(f"{'ID':<5} {'Nombre':<20} {'Activo':<6}")
            gotoxy(35, 5); print("-" * 34)
            for i, estudiante in enumerate(estudiantes):
                gotoxy(35, 6 + i)
                print(f"{estudiante['Id']:<5} {estudiante['Nombre']:<20} {'Sí' if estudiante['Active'] else 'No':<6}")
            gotoxy(10, 6 + len(estudiantes) + 2); input(f"{yellow_color}Presione una tecla para salir...{reset_color}")
            borrarPantalla()
        else:
            gotoxy(10, 4); print(f"{red_color}No hay estudiantes registrados.{reset_color}")
            time.sleep(2)
