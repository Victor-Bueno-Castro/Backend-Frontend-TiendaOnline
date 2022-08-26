from flask import Flask #   Importación de la librería flask
from routes.productos import productos  #   Importación de la ruta productos
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   #   Instancia del módulo flask
app.secret_key = 'mi_clave_secreta'

#   Configuración de la BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/productosdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)   #   Instancia de la BD


app.register_blueprint(productos)