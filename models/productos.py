#   Creación de clasesimport imghdr
import datetime as dt
from utils.db import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(100), nullable=False, unique=True)
    #imagen = db.Column(db.String(300), nullable=True)
    tags = db.Column(db.String(100), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    estatus = db.Column(db.String(50), nullable=False)
    tallas = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)

#   Método constructor para instanciar los campos
    def __init__(self, nombreProducto, sku, tags, costo, 
                estatus, tallas): 
        self.nombreProducto = nombreProducto
        self.sku = sku
        self.tags = tags
        self.costo = costo
        self.estatus = estatus
        self.tallas = tallas