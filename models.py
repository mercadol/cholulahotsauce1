from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
#from sqlalchemy import Column, Integer, String, Float

class Empleado(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellidos = db.Column(db.String)
    cedula = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(66))
    Genero = db.Column(db.String(10))
    fecha_nacimiento = db.Column(db.DateTime)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.Integer)
    celular = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    correoInstitucional = db.Column(db.String(50))
    idContrato = db.Column(db.Integer, nullable=False)
    fechaInicioContrato = db.Column(db.DateTime)
    fechaFinContrato = db.Column(db.DateTime)
    idRol = db.Column(db.Integer, nullable=False) #llave foranea
    idDependencia = db.Column(db.Integer, nullable=False) #llave foranea
    salario = db.Column(db.Integer)

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __repr__(self):
        return f'Empleado({self.nombre}, {self.correo})'
        
    def __str__(self):
        return self.nombre


