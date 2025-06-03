from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_home():
    return "<h1>Área administrativa</h1>"

@admin.route('/login')
def admin_login():
    return "<h1>Login do administrador</h1>"
