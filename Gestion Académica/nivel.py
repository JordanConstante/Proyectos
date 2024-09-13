from datetime import date
class Nivel:
    def __init__(self, id,nivel):
        self.id = id
        self.nivel = nivel
        self.fecha_creacion = date.today()
        self.active =True
    
    def __str__(self):
        return (f'ID: {self.id}, Nivel:{self.nivel}, Fecha de Creación: {self.fecha_creacion}, Activo:{self.active}')
    
    def getJson(self):
        return {
            'Id': self.id,
            'Nivel': self.nivel,
            'Fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
            'Active': self.active
        }