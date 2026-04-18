#Trang điều khiển

from flask import Flask
from routes.main import main_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(main_bp) # Đăng ký blueprint cho cho trang main
app.register_blueprint(auth_bp) # Đăng ký blueprint cho trang auth






if __name__ == '__main__':
    app.run(debug=True)