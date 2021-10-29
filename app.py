from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from config import DevelopmentConfig
from models import Dependencia, Rol, db, Empleado, Contrato
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database/cholula.db"
csrf= CSRFProtect()



@app.errorhandler(404)
def pageNotFound(e):
    print (e)
    return render_template('404.html')


@app.route('/')
def index():
    return render_template('login.html')

#default home page
@app.route('/busqueda/<int:id>')
@app.route('/editar/<int:id>')
def editarEmpleado(id):
    if 'user' in session:
        user = Empleado.query.filter_by(Id_Usuario=id).first()
        return render_template('Editar Empleado.html',user=user)
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
        return render_template('Busqueda_Empleado.html', empleados = Empleado.query.all())
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/base')
def base():
    if 'user' in session:
        return render_template('base.html')
    else:
        return "No tiene permisos. Debe iniciar sesion"

@app.route('/contratos', methods=['GET', 'POST'])
def gestionarContratos():
    if request.method=='POST':
        contrato = Contrato( Nombre_Contrato= request.json['Nombre_Contrato'])
        db.session.add(contrato)
        print (db.session.commit())
        return jsonify({"mesage":"contrato registrado"})
    else:
        contratos = Contrato.query.all()
        return contratos

@app.route('/agregar', methods=['GET', 'POST'])
def agregarEmpleado():
    if 'user' in session:
        if request.method=='POST':

            usuario= Empleado(
                nombre=request.form['nombre'],
                apellidos=request.form['apellidos'],
                cedula=request.form['cedula'],
                password=request.form['password'],
                Genero=request.form['genero'],
                direccion=request.form['direccion'],
                telefono=request.form['telefono'],
                celular=request.form['celular'],
                correo=request.form['correo'],
                correoInstitucional=request.form['correo_Institucional'],
                idContrato=request.form['idContrato'],
                fechaInicioContrato=request.form['correo'],
                fechaFinContrato=request.form['correo'],
                salario=request.form['salario'],
                idDependencia=request.form['idDependencia'],
                idRol=request.form['idRol'])
            
            db.session.add(usuario)
            db.session.commit()

            return "Empleado Registrado"
        contratos = Contrato.query.all()
        roles= Rol.query.all()
        dependencias=Dependencia.query.all()
        return render_template('Agregar Empleados.html', contratos=contratos, roles=roles,dependencias=dependencias)
    else:
        return "No tiene permisos. Debe iniciar sesion"



if __name__== '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=4000)
