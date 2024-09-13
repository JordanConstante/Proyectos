from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla, gotoxy, red_color, reset_color, green_color, yellow_color
from clsJson import JsonFile
from periodo import Periodo
import time
import os

path, file = os.path.split(__file__)

class CrudPeriodo(ICrud):
    json_file = JsonFile(f"{path}/archivos/Periodos.json")

    def create(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{green_color}********** Crear nuevo periodo Académico **********{reset_color}")
        periodos = self.json_file.read()
        id_periodo = max([periodo["Id"] for periodo in periodos], default=0) + 1
        gotoxy(10, 4); periodo_descripcion = input(f"{yellow_color}Ingrese el nombre del periodo (Ejemplo: Semestre 1): {reset_color}")
        gotoxy(10, 5); active = input(f"{yellow_color}El periodo está activo? (si/no): {reset_color}").lower()
        active = True if active == 'si' else False
        periodo_nuevo = Periodo(id_periodo, periodo_descripcion, active)
        periodos.append(periodo_nuevo.getJson())
        self.json_file.save(periodos)

        gotoxy(46, 7); print(f"{green_color}Periodo Creado exitosamente!{reset_color}")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(35, 2); print(f"{yellow_color}********** Actualización de Periodo Académico **********{reset_color}")
        periodos = self.json_file.read()
        if periodos:
            gotoxy(10, 4); id_periodo = int(input(f"{yellow_color}Ingrese el ID del periodo académico: {reset_color}"))
            for periodo in periodos:
                if periodo['Id'] == id_periodo:
                    # Mostrar la información del periodo actual
                    gotoxy(10, 6); print(f"{green_color}Periodo Actual: {periodo['Periodo']}   Fecha Creado: {periodo['Fecha_creacion']}   Activo: {periodo['Active']}{reset_color}")
                    
                    # Solicitar los nuevos datos
                    gotoxy(10, 8); periodo['Periodo'] = input(f"{yellow_color}Ingrese el periodo nuevo: {reset_color}")
                    periodo['Fecha_creacion'] = date.today().strftime('%Y-%m-%d')
                    gotoxy(10, 9); active = input(f"{yellow_color}El periodo está activo? (si/no): {reset_color}").lower()
                    active = True if active == 'si' else False
                    periodo['Active'] = active
                    
                    # Guardar el periodo actualizado
                    self.json_file.save(periodos)
                    gotoxy(34, 11); print(f"{green_color}Periodo actualizado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 12); print(f"{red_color}El periodo no se encuentra en la base de datos...{reset_color}")
                time.sleep(1)
        else:
            gotoxy(10, 12); print(f"{red_color}No hay periodos registrados..{reset_color}")
            time.sleep(1)

    def delete(self):
        borrarPantalla()
        gotoxy(30, 2); print(f"{yellow_color}********** Eliminación de Periodo Académico **********{reset_color}")
        periodos = self.json_file.read()
        if periodos:
            gotoxy(10, 4); id_periodo = int(input(f"{yellow_color}Ingrese el ID del periodo académico: {reset_color}"))
            for periodo in periodos:
                if periodo['Id'] == id_periodo:
                    periodos.remove(periodo)
                    self.json_file.save(periodos)
                    gotoxy(45, 6); print(f"{green_color}Periodo con ID: {id_periodo} eliminado!{reset_color}")
                    time.sleep(2)
                    break
            else:
                gotoxy(10, 7); print(f"{red_color}El periodo no se encuentra en la base de datos...{reset_color}")
                time.sleep(1)
        else:
            gotoxy(10, 4); print(f"{red_color}No hay periodos en el registro.{reset_color}")
            time.sleep(1)

    def consult(self):
        borrarPantalla()
        gotoxy(30, 2); print(f"{yellow_color}********** Consultar Periodos Académicos **********{reset_color}")
        periodos = self.json_file.read()
        if periodos:
            gotoxy(30, 4); print(f"{'ID':<5} {'Periodo':<20} {'Fecha de Creación':<15} {'Activo':<6}")
            gotoxy(30, 5); print("-" * 46)
            for i, periodo in enumerate(periodos):
                gotoxy(30, 6 + i)
                print(f"{periodo['Id']:<5} {periodo['Periodo']:<20} {periodo['Fecha_creacion']:<15} {'Sí' if periodo['Active'] else 'No':<6}")
            gotoxy(10, 6 + len(periodos) + 2); input("Presione una tecla para salir...")
            borrarPantalla()
        else:
            gotoxy(10, 4); print(f"{red_color}No hay periodos académicos{reset_color}")
            time.sleep(2)
