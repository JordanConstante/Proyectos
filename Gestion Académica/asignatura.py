from datetime import date
class Asignatura:
    def __init__(self, id, descripcion, nivel, active):
        self.id = id
        self.descripcion = descripcion  
        self.nivel = nivel  
        self.fecha_creacion = date.today()  
        self.active = active  
    
    def __str__(self):
        return (f'Id: {self.id}, Descripcion: {self.descripcion}, Nivel: {self.nivel}, Active: {self.active}, Fecha de Creacion: {self.fecha_creacion}')
    
    def getJson(self):
        return {
            'Id': self.id,
            'Descripcion': self.descripcion,
            'Nivel': self.nivel,
            'Active': self.active,
            'Fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d')
        }