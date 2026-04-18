# Trang auth


from flask import Flask, flash, render_template, request, Blueprint, redirect, url_for
import sqlite3
auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/auth')
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/signup')
def register():
    return render_template('signup.html')
@auth_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if (len(password) < 6):
            flash('Mật khẩu phải có ít nhất 6 ký tự.')
            return redirect(url_for('auth.signup'))
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        flash('Đăng ký thành công! Vui lòng đăng nhập.')
        return redirect(url_for('main.home'))