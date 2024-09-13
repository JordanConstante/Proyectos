from utilities import borrarPantalla,gotoxy, red_color,reset_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from components import Menu
from iCrudPERIODOS import CrudPeriodo
from iCrudNIVELES import CrudNiveles
from iCrudASIGNATURA import CrudAsignatura
from iCrudPROFESOR import CrudProfesor
from iCrudESTUDIANTE import CrudEstudiante
from iCrudNOTAS import CrudNota
import time
#Menu Proceso Principal
opc = " "
while opc != '7':
    borrarPantalla()
    menu_principal = Menu("Menú de Gestión Académica", ["Gestión de Periodos Académicos", "Gestión de Niveles Académicos", "Gestión de Asignaturas", "Gestión de Profesores", "Gestión de Estudiantes", "Gestión de Notas","Salir"], color=purple_color, colornum=blue_color)

    opc = menu_principal.menu()

    if opc == '1':
        opc1 = ""
        while opc1 != "5":
            borrarPantalla()
            menu_periodo = Menu("Menú Periodos Académicos", ["Ingresar Periodo", "Actualizar Periodo", "Eliminar Periodo", "Consultar Periodo", "Salir"],color=purple_color, colornum=green_color)
            opc1 = menu_periodo.menu()
            crud_periodo = CrudPeriodo()
            if opc1 == '1':
                crud_periodo.create()
            elif opc1 == '2':
                crud_periodo.update()
            elif opc1 == '3':
                crud_periodo.delete()
            elif opc1 == '4':
                crud_periodo.consult()

    elif opc == '2':
        opc2 = ""
        while opc2 != '5':
            borrarPantalla()
            menu_Niveles = Menu("Menú Niveles Académicos", ["Ingresar Nivel", "Actualizar Nivel", "Eliminar Nivel", "Consultar Nivel", "Salir"],color=purple_color, colornum=red_color)
            opc2 = menu_Niveles.menu()
            crud_niveles = CrudNiveles()
            if opc2 == '1':
                crud_niveles.create()
            elif opc2 == '2':
                crud_niveles.update()
            elif opc2 == '3':
                crud_niveles.delete()
            elif opc2 == '4':
                crud_niveles.consult()

            
    elif opc == '3':
        opc3 = ""
        while opc3 != '5':
            borrarPantalla()
            menu_asignatura = Menu("Menú de Asignatura", ["Ingresar Asignatura", "Actualizar Asignatura", "Eliminar Asignatura", "Consultar Asignaturas", "Salir"],color=purple_color, colornum=yellow_color)
            opc3 = menu_asignatura.menu()
            crud_asignatura = CrudAsignatura()
            if opc3 == '1':
                crud_asignatura.create()
            elif opc3 == '2':
                crud_asignatura.update()
            elif opc3 == '3':
                crud_asignatura.delete()
            elif opc3 == '4':
                crud_asignatura.consult()


    elif opc == '4':
        opc4 = ""
        while opc4 != "5":
            borrarPantalla()
            menu_profesor = Menu("Menú de Profesor", ["Ingresar Profesor", "Actualizar Profesor", "Eliminar Profesor", "Consultar Profesor", "Salir"],color=purple_color, colornum=cyan_color)
            crud_profesor = CrudProfesor()
            opc4 = menu_profesor.menu()
            if opc4 == '1':
                crud_profesor.create()
            elif opc4 == '2':
                crud_profesor.update()
            elif opc4 == '3':
                crud_profesor.delete()
            elif opc4 == '4':
                crud_profesor.consult()


    elif opc == "5":
        opc5 = ""
        while opc5 != "5":
            borrarPantalla()
            menu_estudiante = Menu("Menú de Estudiante", ["Ingresar Estudiante", "Actualizar Estudiante", "Eliminar Estudiante", "Consultar Estudiante", "Salir"],color=purple_color, colornum=blue_color)
            crud_estudiante = CrudEstudiante()
            opc5 = menu_estudiante.menu()
            if opc5 == '1':
                crud_estudiante.create()
            elif opc5 == '2':
                crud_estudiante.update()
            elif opc5 == '3':
                crud_estudiante.delete()
            elif opc5 == '4':
                crud_estudiante.consult()

    
    elif opc == "6":
        opc6 = ""
        while opc6 != "5":
            borrarPantalla()
            menu_notas = Menu("Menú de Notas", ["Ingresar Nota", "Actualizar Nota", "Eliminar Nota", "Consultar Notas", "Salir"],color=purple_color, colornum=red_color)
            crud_nota=CrudNota()
            opc6 = menu_notas.menu()
            if opc6 == '1':
                crud_nota.create()
            elif opc6 == '2':
                crud_nota.update()
            elif opc6 == '3':
                crud_nota.delete()
            elif opc6 == '4':
                crud_nota.consult()

    print("Regresando al menu Principal...")
    time.sleep(1)            
borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()