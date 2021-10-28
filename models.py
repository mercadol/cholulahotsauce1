from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
#from sqlalchemy import Column, Integer, String, Float

class Empleado(db.Model):
    __tablename__ = 'Usuario'
    Id_Usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String)
    apellidos = db.Column(db.String)
    cedula = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(66))
    Genero = db.Column(db.String(10))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.Integer)
    celular = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    Correo_Institucional = db.Column(db.String(50))
    ID_Contrato = db.Column(db.Integer, nullable=False)
    Fecha_Inicio_Contrato = db.Column(db.DateTime)
    Fecha_Fin_Contrato = db.Column(db.DateTime)
    ID_Rol = db.Column(db.Integer, nullable=False) #llave foranea
    ID_Dependencia = db.Column(db.Integer, nullable=False) #llave foranea
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
    ID_Contrato = db.Column('ID_Contrato', db.Integer, primary_key=True)
    Nombre_Contrato = db.Column('Nombre_Contrato',db.String)

    def __init__(self, Nombre_Contrato):
        self.Nombre_Contrato=Nombre_Contrato
    
    def __repr__(self):
        return f'Empleado({self.Nombre_Contrato})'
        
    def __str__(self):
        return self.ID_Contrato

class Rol(db.Model):
    __tablename__ = 'Rol'
    id = db.Column('ID_Contrato', db.Integer, primary_key=True)
    nombre = db.Column('Nombre_Rol',db.String(20))
    descripcion = db.Column('Descripcion_Rol',db.String(100))

    def __init__(self, Nombre_Contrato):
        self.Nombre_Contrato=Nombre_Contrato
    
    def __repr__(self):
        return f'Empleado({self.Nombre_Contrato})'
        
    def __str__(self):
        return self.ID_Contrato




