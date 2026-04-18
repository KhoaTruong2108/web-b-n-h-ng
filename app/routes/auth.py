# Trang auth


from flask import Flask, render_template, request, Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth')
def home():
    return "<h1>You are at the auth page</h1>"