from datetime import date
class Estudiante:
    def __init__(self,id,nombre,active):
        self.id = id
        self.nombre = nombre
        self.active = active
        self.fecha_creacion = date.today()
    
    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.nombre}, Fecha de creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'Id': self.id,
            'Nombre': self.nombre,
            'Active': self.active,
            'Fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d')
        }
