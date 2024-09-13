from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla, gotoxy, red_color, reset_color, green_color, yellow_color
from clsJson import JsonFile
from asignatura import Asignatura
import time
import os

path, file = os.path.split(__file__)

class CrudAsignatura(ICrud):
    json_file = JsonFile(f"{path}/archivos/Asignaturas.json")
    
    def create(self):
        borrarPantalla()
        gotoxy(25, 2); print(f"{green_color}********** Crear Asignatura Académica **********{reset_color}")
        asignaturas = self.json_file.read()
        id_asignatura = max([asignatura["Id"] for asignatura in asignaturas], default=0) + 1
        gotoxy(10, 4); asignatura_descripcion = input(f"{yellow_color}Ingrese la asignatura (Ejemplo: Programación):...{reset_color}")
        gotoxy(10, 5); nivel_asignatura = input(f"{yellow_color}Ingrese el nivel al que pertenece la asignatura (Ejemplo: 1er Nivel)...{reset_color}")
        gotoxy(10, 6); active = input(f"{yellow_color}La asignatura está activa? (si/no):{reset_color}").lower()
        active = True if active == 'si' else False
        asignatura_nueva = Asignatura(id_asignatura, asignatura_descripcion, nivel_asignatura, active)
        asignaturas.append(asignatura_nueva.getJson())
        self.json_file.save(asignaturas)
        
        gotoxy(33, 8); print(f"{green_color}Asignatura Creada exitosamente!{reset_color}")
        time.sleep(2)
        
    def update(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{green_color}********** Actualización de Asignatura**********{reset_color}")
        asignaturas = self.json_file.read()
        if asignaturas:
            gotoxy(10, 4); id_asignatura = int(input(f"{yellow_color}Ingrese el ID de la asignatura: {reset_color}"))
            for asignatura in asignaturas:
                if asignatura['Id'] == id_asignatura:
                    gotoxy(10, 6); print(f"{green_color}Asignatura Actual:{reset_color} {asignatura['Descripcion']}   {green_color}Fecha Creado:{reset_color}{asignatura['Fecha_creacion']}   {green_color}Nivel:{reset_color}{asignatura['Nivel']}   {green_color}Activo:{reset_color}{asignatura['Active']}")
                    gotoxy(10, 7); asignatura['Descripcion'] = input(f"{yellow_color}Ingrese la asignatura nueva:{reset_color}")
                    asignatura['Fecha_creacion'] = date.today().strftime('%Y-%m-%d')
                    gotoxy(10, 8); asignatura['Nivel'] = input(f"{yellow_color}Ingrese el nivel de la asignatura:{reset_color}")
                    gotoxy(10, 9); active = input(f"{yellow_color}La asignatura está activa? (si/no):{reset_color}").lower()
                    active = True if active == 'si' else False
                    asignatura['Active'] = active
                    self.json_file.save(asignaturas)
                    gotoxy(10, 11); print(f"{green_color}Asignatura actualizada!{reset_color}")
                    time.sleep(2)
                else:
                    gotoxy(10, 6); print(f"{red_color}La asignatura no se encuentra en la base de datos...{reset_color}")
                    time.sleep(1)
        else:
            gotoxy(30, 4); print(f"{red_color}No hay asignaturas registradas...{reset_color}")
            
    def delete(self):
        borrarPantalla()
        gotoxy(15, 2); print(f"{green_color}********** Eliminación de asignatura **********{reset_color}")
        asignaturas = self.json_file.read()
        if asignaturas:
            gotoxy(10, 4); id_asignatura = int(input(f"{yellow_color}Ingrese el ID de la asignatura: {reset_color}"))
            for asignatura in asignaturas:
                if asignatura['Id'] == id_asignatura:
                    asignaturas.remove(asignatura)
                    self.json_file.save(asignaturas)
                    gotoxy(27, 6); print(f"{green_color}Asignatura con ID:{reset_color}{id_asignatura} {green_color}eliminada!{reset_color}")
                    time.sleep(2)
                    break
        else:
            gotoxy(10, 4); print(f"{red_color}No hay asignaturas en el registro.{reset_color}")
            
    def consult(self):
        borrarPantalla()
        gotoxy(15, 2); print(f"{green_color}Consultar Asignaturas{reset_color}")
        asignaturas = self.json_file.read()
        if asignaturas:
            gotoxy(35, 4); print(f"{yellow_color}Asignaturas:{reset_color}")
            row = 6
            for asignatura in asignaturas:
                gotoxy(10, row); print(f"Id:{asignatura['Id']} ||| Asignatura:{asignatura['Descripcion']} ||| Fecha de Creación:{asignatura['Fecha_creacion']} ||| Nivel:{asignatura['Nivel']} ||| Activo:{asignatura['Active']}")
                row += 1
            gotoxy(10, row + 2); input(f"{yellow_color}Presione una tecla para salir...{reset_color}")
            borrarPantalla()
        else:
            gotoxy(10, 4); print(f"{red_color}No hay asignaturas{reset_color}")
