from datetime import date
class Profesor:
    def __init__(self,id, nombre,active):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = date.today()
        self.active = active

    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.nombre}, active: {self.active}, Fecha de creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'Id': self.id,
            'Nombre': self.nombre,
            'Active': self.active,
            'Fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d')
        }
