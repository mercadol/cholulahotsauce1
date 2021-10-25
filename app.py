from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from database import usuarios
from config import DevelopmentConfig
from models import db, Empleado
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["SQLALCHEMY_DATABASE_URL"]="sqlite:///database/colula.db"
csrf= CSRFProtect()

@app.errorhandler(404)
def pageNotFound(e):
    print (e)
    return render_template('404.html')
    


@app.route('/api/usuario', methods=['POST'])
def add_usuario():
    Id_Usuario = request.json['Id_Usuario'],
    Correo=request.json['Correo'],
    Nombre=request.json['Nombre'],
    Apellido=request.json['Apellido'],
    Cedula=request.json['Cedula'],
    Genero=request.json['Genero'],
    Fecha_ingreso=request.json['Fecha_ingreso'],
    Direccion=request.json['Direccion'],
    Tipo_contrato=request.json['Tipo_contrato'],
    Id_Rol=request.json['Id_Rol'],
    Id_Cargo=request.json['Id_Cargo']
    
    data = (
        Id_Usuario,
        Correo,
        Nombre,
        Apellido,
        Cedula,
        Genero,
        Fecha_ingreso,
        Direccion,
        Tipo_contrato,
        Id_Rol,
        Id_Cargo
    )
    
    usuario_id = usuarios.insert_usuario(data)
    
    if usuario_id:
        return jsonify({"message": "usuario created"})

@app.route('/api/usuarios')
def getUsuarios():
    return jsonify(usuarios)

@app.route('/')
def index():
    return render_template('login.html')

#default home page
@app.route('/editar')
def editarEmpleado():
    if 'user' in session:
        return render_template('Editar Empleado.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/perfil')
def perfil():
    if 'user' in session:
        return render_template('Perfil Empleado.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/login', methods=['POST'])
def login():
    print ("antes de entrar")
    if request.method=="POST":
        print ("entró")
        usuario=request.form['usuario']
        password=request.form['contrasenia']
        session['user']=usuario
        return redirect(url_for('base'))
    else:
        return "bad request"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/generar')
def generarReporte():
    if 'user' in session:
        return render_template('Generar Reporte.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/busqueda')
def busquedaEmpleado():
    if 'user' in session:
        return render_template('Busqueda_Empleado.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/base')
def base():
    if 'user' in session:
        return render_template('base.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/agregar', methods=['GET', 'POST'])
def agregarEmpleado():
    if 'user' in session:
        if request.method=='POST':

            usuario= Empleado(nombre=request.form['nombre'],
                            correo=request.form['correo'])
            
            db.session.add(usuario)
            db.session.commit()

            return "Empleado Registrado"

        return render_template('Agregar Empleados.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"


#LOGIN PAGE
#@app.route('/login', methods=['POST', 'GET'])
#def login():
    #pass








if __name__== '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=4000)
