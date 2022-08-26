from app import app #   Importanción del archivo app
from utils.db import db #   Importación de la base de datos

#   Creación de la base de datos y tabla
with app.app_context():
    db.create_all()

if __name__ == '__main__':  #   Condicional para levantar el servidor en Flask
    app.run(debug=True) #   Guarda los cambios en automático

