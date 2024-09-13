from datetime import date
from estudiante import Estudiante

class Nota:
    def __init__(self, id, periodo, profesor, asignatura, active):
        self.id = id
        self.periodo = periodo
        self.profesor = profesor
        self.asignatura = asignatura
        self.detalleNota = []  # Lista para almacenar los detalles de las notas para cada estudiante
        self.fecha_creacion = date.today()
        self.active = active

    def __str__(self):
        return (f"Nota ID: {self.id}, Periodo: {self.periodo}, Profesor: {self.profesor}, "
                    f"Asignatura: {self.asignatura}, Activo: {self.active}, Fecha de Creación: {self.fecha_creacion}")

    def addNota(self, estudiante, nota1, nota2, recuperacion=None, observacion=None):
        nuevo_detalle = DetalleNota(
            id=len(self.detalleNota) + 1,
            estudiante=estudiante,
            nota1=nota1,
            nota2=nota2,
            recuperacion=recuperacion,
            observacion=observacion
        )
        self.detalleNota.append(nuevo_detalle)

    def to_dict(self):
        return {
            'id': self.id,
            'periodo': self.periodo,
            'profesor': self.profesor,
            'asignatura': self.asignatura,
            'detalleNota': [detalle.__dict__ for detalle in self.detalleNota],
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'active': self.active
        }


class DetalleNota:
    def __init__(self, id, estudiante, nota1, nota2, recuperacion=None, observacion=None):
        self.id = id
        self.estudiante = estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.observacion = observacion
