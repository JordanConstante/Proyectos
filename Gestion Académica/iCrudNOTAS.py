from iCrud import ICrud
from datetime import date
from utilities import borrarPantalla,gotoxy, red_color,reset_color,blue_color, yellow_color,cyan_color
from clsJson import JsonFile
from nota import Nota,DetalleNota
import time
import os

path, file = os.path.split(__file__)

class CrudNota(ICrud):
    json_file = JsonFile(f"{path}/archivos/Notas.json")   

    def create(self):
        # Cargar los datos necesarios
        profesores = JsonFile(f"{path}/archivos/Profesores.json").read()
        asignaturas = JsonFile(f"{path}/archivos/Asignaturas.json").read()
        periodos = JsonFile(f"{path}/archivos/Periodos.json").read()
        estudiantes = JsonFile(f"{path}/archivos/Estudiantes.json").read()

        # Seleccionar profesor
        borrarPantalla()
        gotoxy(27,2),print(red_color + "********** Registrar notas **********" + reset_color)
        print("-"*100)
        print("Profesor que asigna nota:")
        for i, prof in enumerate(profesores):
            print(f"{i + 1}. {prof['Nombre']}")
        while True:
            try:
                opcion_profesor = int(input("Opción: ")) - 1
                if opcion_profesor < 0 or opcion_profesor >= len(profesores):
                    raise ValueError("Opción inválida")
                profesor_seleccionado = profesores[opcion_profesor]
                break
            except ValueError as e:
                print(e)

        # Seleccionar asignatura
        borrarPantalla()
        gotoxy(27,2),print(red_color + "********** Registrar notas **********" + reset_color)
        print("-"*100)
        print("Seleccione la Asignatura:")
        for i, asign in enumerate(asignaturas):
            print(f"{i + 1}. {asign['Descripcion']}")
        while True:
            try:
                opcion_asignatura = int(input("Opción: ")) - 1
                if opcion_asignatura < 0 or opcion_asignatura >= len(asignaturas):
                    raise ValueError("Opción inválida")
                asignatura_seleccionada = asignaturas[opcion_asignatura]
                break
            except ValueError as e:
                print(e)

        # Seleccionar periodo
        borrarPantalla()
        gotoxy(27,2),print(red_color + "********** Registrar notas **********" + reset_color)
        print("-"*100)
        print("Seleccione el Periodo:")
        for i, per in enumerate(periodos):
            print(f"{i + 1}. {per['Periodo']}")
        while True:
            try:
                opcion_periodo = int(input("Opción: ")) - 1
                if opcion_periodo < 0 or opcion_periodo >= len(periodos):
                    raise ValueError("Opción inválida")
                periodo_seleccionado = periodos[opcion_periodo]
                break
            except ValueError as e:
                print(e)

        # Crear una nueva instancia de Nota
        nueva_nota = Nota(id=len(self.json_file.read()) + 1, 
                        periodo=periodo_seleccionado['Periodo'], 
                        profesor=profesor_seleccionado['Nombre'],
                        asignatura=asignatura_seleccionada['Descripcion'],
                        active=True)

        # Agregar notas para los estudiantes seleccionados
        while True:
            borrarPantalla()
            gotoxy(27,2),print(red_color + "********** Registrar notas **********" + reset_color)
            print("-"*100)
            print("Seleccione el Estudiante para agregar la nota:")
            for i, est in enumerate(estudiantes):
                print(f"{i + 1}. {est['Nombre']}")
            try:
                opcion_estudiante = int(input("Opción: ")) - 1
                if opcion_estudiante < 0 or opcion_estudiante >= len(estudiantes):
                    raise ValueError("Opción inválida")
                estudiante_seleccionado = estudiantes[opcion_estudiante]
            except ValueError as e:
                print(e)
                continue
            borrarPantalla()
            
            gotoxy(27,2),print(red_color + "********** Registrar notas **********" + reset_color)
            print("-"*100)
            gotoxy(1, 4), print(f"{yellow_color}Fecha:{blue_color}{time.strftime('%d-%m-%Y')}")
            gotoxy(45, 4), print(f"{yellow_color}Id:{blue_color}{nueva_nota.id} ")
            gotoxy(1, 5), print(f"{yellow_color}Docente:{blue_color}{nueva_nota.profesor} ")
            gotoxy(1, 6), print(f"{yellow_color}Asignatura: {blue_color}{nueva_nota.asignatura} ")
            gotoxy(45, 6), print(f"{yellow_color}Periodo:{blue_color}{nueva_nota.periodo}")
            print("-"*100)
            # Ingresar notas para el estudiante
            

            gotoxy(27, 8)
            print(f"{yellow_color}Detalle de Notas")
            print("-"*100)
            gotoxy(1, 10), print(f"{yellow_color}Estudiante")
            gotoxy(15, 10), print(f"{yellow_color}Nota 1er Parcial")
            gotoxy(35, 10), print(f"{yellow_color}Nota 2do Parcial")
            gotoxy(55, 10), print(f"{yellow_color}Recuperación")
            gotoxy(72, 10), print(f"{yellow_color}Observación")

            gotoxy(1,11);print(f"{blue_color}{estudiante_seleccionado["Nombre"]}")
            gotoxy(21,11);nota1 = float(input())
            gotoxy(42,11);nota2 = float(input())
            gotoxy(60,11);recuperacion = input()
            if recuperacion is "":
                gotoxy(60,11);print("N/A")
            gotoxy(75,11);observacion = input()
            if observacion is "":
                gotoxy(75,11);print("N/A")
            recuperacion = float(recuperacion) if recuperacion else None

            # Agregar la nota para el estudiante
            nueva_nota.addNota(estudiante_seleccionado, nota1, nota2, recuperacion, observacion)

            # Preguntar si desea agregar otra nota
            continuar = input("¿Desea agregar otra nota? (s/n): ").lower()
            if continuar != 's':
                break

        # Guardar la nueva nota en el archivo JSON
        notas = self.json_file.read()
        notas.append(nueva_nota.to_dict())  # Convertir la nota a diccionario
        self.json_file.save(notas)
        print("Nota creada con éxito.")
        time.sleep(2)
        
    def update(self):
        borrarPantalla()
        notas = self.json_file.read()

        if not notas:
            print("No hay notas registradas para actualizar.")
            time.sleep(2)
            return

        # Mostrar todas las notas y seleccionar cuál actualizar
        print("Seleccione la Nota a actualizar:")
        for i, nota in enumerate(notas):
            print(f"{i + 1}. Nota ID {nota['id']} - {nota['asignatura']}")

        while True:
            try:
                opcion = int(input("Opción: ")) - 1
                if opcion < 0 or opcion >= len(notas):
                    raise ValueError("Opción inválida")
                nota_seleccionada = notas[opcion]
                break
            except ValueError as e:
                print(e)

        # Asegurarse de que la clave 'detalleNota' existe
        detalles_nota = nota_seleccionada.get('detalleNota', [])
        if not detalles_nota:
            print("No hay detalles de notas para esta entrada.")
            time.sleep(2)
            return

        # Mostrar detalles de la nota seleccionada
        print(f"Detalles de la Nota ID {nota_seleccionada['id']} - {nota_seleccionada['asignatura']}:")
        for i, detalle in enumerate(detalles_nota):
            print(f"{i + 1}. Estudiante: {detalle['estudiante']['Nombre']}, Nota1: {detalle['nota1']}, Nota2: {detalle['nota2']}")

        # Seleccionar el detalle de la nota a actualizar
        while True:
            try:
                opcion_detalle = int(input("Seleccione el detalle de la nota a actualizar: ")) - 1
                if opcion_detalle < 0 or opcion_detalle >= len(detalles_nota):
                    raise ValueError("Opción inválida")
                detalle_seleccionado = detalles_nota[opcion_detalle]
                break
            except ValueError as e:
                print(e)

        # Actualizar las notas del estudiante
        try:
            detalle_seleccionado['nota1'] = float(input(f"Nota1 actual ({detalle_seleccionado['nota1']}), nueva Nota1: "))
            detalle_seleccionado['nota2'] = float(input(f"Nota2 actual ({detalle_seleccionado['nota2']}), nueva Nota2: "))
            recuperacion = input(f"Recuperación actual ({detalle_seleccionado.get('recuperacion', 'N/A')}), nueva Recuperación (opcional): ")
            if recuperacion:
                detalle_seleccionado['recuperacion'] = float(recuperacion)
            observacion = input(f"Observación actual ({detalle_seleccionado['observacion']}), nueva Observación (opcional): ")
            if observacion:
                detalle_seleccionado['observacion'] = observacion
        except ValueError as e:
            print("Error en la entrada. Asegúrese de ingresar un número válido para las notas.")
            return

        # Guardar los cambios en el archivo JSON
        self.json_file.save(notas)
        print("Nota actualizada con éxito.")
        time.sleep(2)
        
    def delete(self):
        borrarPantalla()
        notas = self.json_file.read()
        if not notas:
            print("No hay notas registradas para eliminar.")
            time.sleep(2)
            return

        print("Seleccione la Nota a eliminar:")
        for i, nota in enumerate(notas):
            print(f"{i + 1}. Nota ID {nota['id']} - Profesor: {nota['profesor']} - Asignatura: {nota['asignatura']}")
        opcion = int(input("Opción: ")) - 1

        if opcion < 0 or opcion >= len(notas):
            print("Opción inválida.")
            return

        # Confirmar eliminación
        nota_seleccionada = notas[opcion]
        confirmacion = input(f"¿Está seguro de que desea eliminar la Nota ID {nota_seleccionada['id']}? (s/n): ").lower()

        if confirmacion == 's':
            notas.pop(opcion)
            self.json_file.save(notas)
            print("Nota eliminada con éxito.")
        else:
            print("Eliminación cancelada.")

        time.sleep(2)
        
    def consult(self):
        borrarPantalla()
        notas = self.json_file.read()
        if not notas:
            print("No hay notas registradas.")
        else:
            print("NOTAS REGISTRADAS:")
            print("=" * 50)
            for nota in notas:
                print(f"ID Nota: {nota['id']}")
                print(f"Profesor: {nota['profesor']}")
                print(f"Asignatura: {nota['asignatura']}")
                print(f"Periodo: {nota['periodo']}")
                print(f"Estado: {'Activa' if nota['active'] else 'Inactiva'}")
                print("-" * 50)
                for detalle in nota['detalleNota']:
                    print(f"Estudiante: {detalle['estudiante']['Nombre']}")
                    print(f"Nota 1: {detalle['nota1']}")
                    print(f"Nota 2: {detalle['nota2']}")
                    print(f"Recuperación: {detalle.get('recuperacion', 'N/A')}")
                    print(f"Observación: {detalle.get('observacion', 'N/A')}")
                    print("-" * 50)
                print("=" * 50)
        input("\nPresione Enter para continuar...")