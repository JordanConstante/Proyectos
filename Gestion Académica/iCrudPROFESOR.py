from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla, gotoxy, red_color, reset_color, green_color, yellow_color
from clsJson import JsonFile
from profesor import Profesor
import time
import os

path, file = os.path.split(__file__)

class CrudProfesor(ICrud):
    json_file = JsonFile(f"{path}/archivos/Profesores.json")

    def create(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{green_color}********** Crear nuevo profesor **********{reset_color}")
        profesores = self.json_file.read()
        id_profesor = max([profesor["Id"] for profesor in profesores], default=0) + 1
        gotoxy(10, 4); nombre = input(f"{yellow_color}Ingrese el nombre del profesor: {reset_color}")
        gotoxy(10, 5); active = input(f"{yellow_color}El profesor está activo? (si/no): {reset_color}").lower()
        active = True if active == 'si' else False
        profesor_nuevo = Profesor(id_profesor, nombre, active)
        profesores.append(profesor_nuevo.getJson())
        self.json_file.save(profesores)
        
        gotoxy(34, 7); print(f"{green_color}Profesor Creado exitosamente!{reset_color}")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Actualización de Profesor **********{reset_color}")
        profesores = self.json_file.read()
        if profesores:
            gotoxy(10, 4); id_profesor = int(input(f"{yellow_color}Ingrese el ID del profesor: {reset_color}"))
            for profesor in profesores:
                if profesor['Id'] == id_profesor:
                    # Mostrar la información actual del profesor
                    gotoxy(10, 6); print(f"{green_color}Profesor: {profesor['Id']}   Nombre: {profesor['Nombre']}   Activo: {profesor['Active']}{reset_color}")
                    
                    # Solicitar los nuevos datos
                    gotoxy(10, 8); profesor['Nombre'] = input(f"{yellow_color}Ingrese el nombre del profesor: {reset_color}")
                    gotoxy(10, 9); active = input(f"{yellow_color}El profesor está activo? (si/no): {reset_color}").lower()
                    active = True if active == 'si' else False
                    profesor['Active'] = active
                    
                    # Guardar el profesor actualizado
                    self.json_file.save(profesores)
                    gotoxy(34, 11); print(f"{green_color}Profesor actualizado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 12); print(f"{red_color}El profesor no se encuentra en la base de datos...{reset_color}")
                time.sleep(1)
        else:
            gotoxy(10, 12); print(f"{red_color}No hay profesores registrados...{reset_color}")
            time.sleep(1)

    def delete(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Eliminación de Profesor **********{reset_color}")
        profesores = self.json_file.read()
        if profesores:
            gotoxy(10, 4); id_profesor = int(input(f"{yellow_color}Ingrese el ID del profesor: {reset_color}"))
            for profesor in profesores:
                if profesor['Id'] == id_profesor:
                    profesores.remove(profesor)
                    self.json_file.save(profesores)
                    gotoxy(10, 6); print(f"{green_color}Profesor con ID: {id_profesor} eliminado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 7); print(f"{red_color}El profesor no se encuentra en la base de datos...{reset_color}")
                time.sleep(1)
        else:
            gotoxy(10, 4); print(f"{red_color}No hay profesores en el registro.{reset_color}")
            time.sleep(1)

    def consult(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Consultar Profesores **********{reset_color}")
        profesores = self.json_file.read()
        if profesores:
            gotoxy(35, 4); print(f"{'ID':<5} {'Nombre':<20} {'Activo':<6}")
            gotoxy(35, 5); print("-" * 34)
            for i, profesor in enumerate(profesores):
                gotoxy(35, 6 + i)
                print(f"{profesor['Id']:<5} {profesor['Nombre']:<20} {'Sí' if profesor['Active'] else 'No':<6}")
            gotoxy(10, 6 + len(profesores) + 2); input(f"{yellow_color}Presione una tecla para salir...{reset_color}")
            borrarPantalla()
        else:
            gotoxy(10, 4); print(f"{red_color}No hay profesores registrados.{reset_color}")
            time.sleep(2)
