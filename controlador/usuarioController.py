from app import app, usuarios
from flask import render_template, request, redirect, session, url_for
import pymongo
import yagmail
import threading

@app.route('/')
def vistaIniciarSesion():  
    return render_template('frmIniciarSesion.html')

@app.route('/iniciarSesion', methods=['POST'])
def iniciarSesion():  
    mensaje = None
    estado = False
    try:
        usuario = request.form['txtUser']
        password = request.form['txtPassword']
        datosConsulta = {"usuario": usuario, "password": password}
        print(datosConsulta)
        user = usuarios.find_one(datosConsulta)
        if (user):
            session['user']=usuario
            email = yagmail.SMTP("libnibernate@gmail.com", open(".password").read(), encoding='UTF-8')
            asunto = 'Reporte de ingreso al sistema de usuario'
            mensaje = f"Se informa que el usuario <b>'{user["nombres"]} {user["apellidos"]}'</b> ha ingresado al sistema"  # Corrección en la interpolación de cadenas
           
            
            thread = threading.Thread(target=enviarCorreo, args=(email, ["libnibernate@gmail.com" , user [ 'correo' ]], asunto, mensaje ))
            thread. start()
            estado = True

            return redirect("/listarProductos")  
        else:
            mensaje = 'Credenciales no válidas'
            
            
    except pymongo.errors.PyMongoError as error:  
        mensaje = error
        
    return render_template('frmIniciarSesion.html', estado=estado, mensaje=mensaje)

#funcion que envia el correo
def enviarCorreo(email=None, destinatario=None, asunto=None, mensaje=None):
    email. send (to=destinatario, subject=asunto, contents=mensaje)


@app.route('/registro', methods=['POST'])
def registro():
    try:
        # Obtener los datos del formulario
        usuario = request.form['txtUser']
        password = request.form['txtPassword']
        nombres = request.form['txtNombres']
        apellidos = request.form['txtApellidos']
        correo = request.form['txtCorreo']

        # Verificar si el usuario ya existe en la base de datos
        if usuarios.find_one({"usuario": usuario}):
            return "El usuario ya está registrado"

        # Crear un nuevo documento de usuario
        nuevo_usuario = {
            "usuario": usuario,
            "password": password,
            "nombres": nombres,
            "apellidos": apellidos,
            "correo": correo
        }

        # Insertar el nuevo usuario en la base de datos
        usuarios.insert_one(nuevo_usuario)

        # Redirigir al usuario a la página de inicio de sesión después del registro exitoso
        return redirect(url_for('vistaIniciarSesion'))

    except Exception as e:
        return f"Error al registrar el usuario: {e}"

# Ruta para la página de registro
@app.route('/registro', methods=['GET'])
def vistaRegistro():
    return render_template('frmRegistrarse.html')


@app.route('/cerrarSesion')
def cerrarSesion():
    session.pop('user', None)
    return redirect(url_for('inicio'))