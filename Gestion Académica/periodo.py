from datetime import date
class Periodo: 
    def __init__(self, id, periodo, active):
        self.id = id #Identificador único para el periodo. 
        self.periodo = periodo # Nombre o descripción del periodo (por ejemplo, "Semestre 1"). 
        self.fecha_creacion = date.today() #Fecha de creación del periodo, se asigna la fecha actual. 
        self.active = active # Estado de actividad del periodo (True o False).
        
    def __str__(self):
        return (f'ID: {self.id}, Periodo:{self.periodo}, Fecha de Creación: {self.fecha_creacion}, Activo:{self.active}')
    
    def getJson(self):
        return {
            'Id': self.id,
            'Periodo': self.periodo,
            'Fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
            'Active': self.active
        }
