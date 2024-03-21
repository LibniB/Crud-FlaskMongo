from flask import Flask, session
import pymongo
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/imagenes'

miConexion = pymongo.MongoClient('mongodb+srv://libnibetancourth:12345678Lb@cluster0.xng9auw.mongodb.net/')
baseDatos = miConexion['GestionProductos']
productos = baseDatos['productos']
categorias = baseDatos['categorias']
usuarios = baseDatos['usuarios']

#clave secreta manejo de sesiones
app.secret_key= os.urandom(10)

from controlador.productoController import *
from controlador.categoriaController import *
from controlador.usuarioController import *


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
