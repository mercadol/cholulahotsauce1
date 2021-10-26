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

    def __init__(
            self,
            nombre,
            correo,
            apellidos,
            cedula,
            password,
            Genero,
            direccion,
            telefono,
            celular,
            correoInstitucional,
            idContrato,
            fechaInicioContrato,
            fechaFinContrato,
            idRol,
            idDependencia,
            salario
        ):
        self.nombre = nombre
        self.correo = correo
        self.apellidos = apellidos
        self.cedula = cedula
        self.password = password
        self.Genero = Genero
        self.direccion = direccion
        self.telefono = telefono
        self.celular = celular
        self.correo = correo
        self.correoInstitucional = correoInstitucional
        self.idContrato = idContrato
        self.fechaInicioContrato = fechaInicioContrato
        self.fechaFinContrato = fechaFinContrato
        self.idRol = idRol
        self.idDependencia = idDependencia
        self.salario = salario

    def __repr__(self):
        return f'Empleado({self.nombre}, {self.correo})'
        
    def __str__(self):
        return self.id


class Contrato(db.Model):
    __tablename__ = 'Contrato'
    id = db.Column(db.Integer, primary_key=True)
    nombreContrato = db.Column(db.String)

    def __init__(self, nombreContrato):
        self.nombreContrato=nombreContrato
    
    def __repr__(self):
        return f'Empleado({self.nombreContrato})'
        
    def __str__(self):
        return self.id

class Dependencia(db.Model):
    __tablename__ = 'Dependencia'
    id = db.Column(db.Integer, primary_key=True)
    nombreDependencia = db.Column(db.String)

    def __init__(self, id, nombreDependencia):
        self.id = id
        self.nombreDependencia=nombreDependencia
    
    def __repr__(self):
        return f'Empleado({self.nombreDependencia})'
    def __str__(self):
        return self.id


