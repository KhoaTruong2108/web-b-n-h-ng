# Trang main

from flask import Flask, render_template, request, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST', 'DELETE'])
def home():
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return f'{request.form.get("name")} hiện tại đang {request.form.get("age")} tuổi và học tại {request.form.get("school")}', 500
    else:
        return 'we don\'t support this method', 401

