from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla, gotoxy, red_color, reset_color, green_color, yellow_color
from clsJson import JsonFile
from nivel import Nivel
import time
import os

path, file = os.path.split(__file__)

class CrudNiveles(ICrud):
    json_file = JsonFile(f"{path}/archivos/Niveles.json")
    
    def create(self):
        borrarPantalla()
        gotoxy(15, 2); print(f"{green_color}********** Crear Nivel Académico **********{reset_color}")
        niveles = self.json_file.read()
        id_nivel = max([nivel["Id"] for nivel in niveles], default=0) + 1
        gotoxy(10, 4); nivel_descripcion = input(f"{yellow_color}Ingrese el nivel académico (Ejemplo: Secundaria): {reset_color}")
        
        nivel_nuevo = Nivel(id_nivel, nivel_descripcion)
        niveles.append(nivel_nuevo.getJson())
        self.json_file.save(niveles)
        
        gotoxy(20, 6); print(f"{green_color}Nivel Académico Creado exitosamente!{reset_color}")
        time.sleep(2)
        
    def update(self):
        borrarPantalla()
        gotoxy(15, 2); print(f"{green_color}********** Actualización de Niveles Académicos **********{reset_color}")
        niveles = self.json_file.read()
        
        if niveles:
            gotoxy(11, 4); id_nivel = int(input(f"{yellow_color}Ingrese el ID del nivel académico: {reset_color}"))
            for nivel in niveles:
                if nivel['Id'] == id_nivel:
                    gotoxy(10, 6); print(f"Nivel Actual: {nivel['Nivel']}   Fecha Creado: {nivel['Fecha_creacion']}   Activo: {nivel['Active']}")
                    gotoxy(12, 8); nivel['Nivel'] = input(f"{yellow_color}Ingrese el Nivel nuevo: {reset_color}")
                    nivel['Fecha_creacion'] = date.today().strftime('%Y-%m-%d')
                    self.json_file.save(niveles)
                    gotoxy(30, 10); print(f"{green_color}Nivel Académico actualizado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 6); print(f"{red_color}El nivel académico no se encuentra en la base de datos...{reset_color}")
        else:
            gotoxy(10, 4); print(f"{red_color}No hay niveles académicos registrados...{reset_color}")
            time.sleep(2)
        
    def delete(self):
        borrarPantalla()
        gotoxy(15, 2); print(f"{green_color}********** Eliminación de Niveles Académicos **********{reset_color}")
        niveles = self.json_file.read()
        
        if niveles:
            gotoxy(10, 4); id_nivel = int(input(f"{yellow_color}Ingrese el ID del nivel académico: {reset_color}"))
            for nivel in niveles:
                if nivel['Id'] == id_nivel:
                    niveles.remove(nivel)
                    self.json_file.save(niveles)
                    gotoxy(30, 6); print(f"{green_color}Nivel con ID: {id_nivel} eliminado!{reset_color}")
                    time.sleep(2)
                    break
        else:
            gotoxy(10, 4); print(f"{red_color}No hay Niveles Académicos en el registro.{reset_color}")
            time.sleep(2)
    
    def consult(self):
        borrarPantalla()
        gotoxy(25, 2); print(f"{green_color}********** Consultar Niveles Académicos **********{reset_color}")
        niveles = self.json_file.read()
        
        if niveles:
            gotoxy(35, 4); print(f"{yellow_color}Niveles Académicos Registrados:{reset_color}")
            row = 6
            for nivel in niveles:
                gotoxy(10, row); print(f"Id: {nivel['Id']} || Nivel: {nivel['Nivel']} || Fecha de Creación: {nivel['Fecha_creacion']} || Activo: {nivel['Active']}")
                row += 1
            gotoxy(10, row + 2); input(f"{yellow_color}Presione una tecla para salir...{reset_color}")
            borrarPantalla()
        else:
            gotoxy(10, 4); print(f"{red_color}No hay Niveles académicos registrados.{reset_color}")
            time.sleep(2)
