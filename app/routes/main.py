# Trang main

from flask import Flask, render_template, request, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "<h1>You are at the main page</h1>"