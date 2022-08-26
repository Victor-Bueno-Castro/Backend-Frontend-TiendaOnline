from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.productos import Productos
from utils.db import db

productos = Blueprint('productos', __name__)

@productos.route('/')
def home():
    productos = Productos.query.all()
    return render_template('index.html', productos=productos)

@productos.route('/productos', methods=['POST'])
def add_producto():
    nombreProducto = request.form['nombreProducto']
    sku = request.form['sku']
    tags = request.form['tags']
    costo = request.form['costo']
    estatus = request.form['estatus']
    tallas = request.form['tallas']
    nuevo_producto = Productos(nombreProducto, sku, tags, costo, estatus, tallas)
    db.session.add(nuevo_producto)
    db.session.commit()
    flash('Producto creado satisfactoriamente!')
    return redirect(url_for('productos.home'))

@productos.route('/update/<id>', methods=['POST', 'GET'])
def actualizar_producto(id):
    producto = Productos.query.get(id)
    if request.method == 'POST':
        producto.nombreProducto = request.form['nombreProducto']
        producto.sku = request.form['sku']
        producto.tags = request.form['tags']
        producto.costo = request.form['costo']
        producto.estatus = request.form['estatus']
        producto.tallas = request.form['tallas']
        db.session.commit()
        flash('Producto actualizado satisfactoriamente!')
        return redirect(url_for('productos.home'))
    return render_template('update.html', producto=producto)

@productos.route('/delete/<id>')
def eliminar_producto(id):
    producto = Productos.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado satisfactoriamente!')
    return redirect(url_for('productos.home'))
