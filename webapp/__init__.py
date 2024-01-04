from flask import Flask
from flask_mysql_connector import MySQL
from .db import create_tables, mysql
from webapp.config import Config
from dotenv import load_dotenv
import cloudinary
from cloudinary import config as cloudinary_config

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config.from_object(Config)

    cloudinary.config(
        cloud_name=app.config['CLOUD_NAME'],
        api_key=app.config['CLOUD_API_KEY'],
        api_secret=app.config['CLOUD_API_SECRET'],
        folder_name=app.config['CLOUD_FOLDER']
    )

    create_tables(app=app, mysql=mysql)
    
    from .routes.base_bp import base_bp
    # from .routes.college_bp import college
    # from .routes.course_bp import course
    # from .routes.student_bp import student

    app.register_blueprint(base_bp, url_prefix='/')
    # app.register_blueprint(college, url_prefix='/college')
    # app.register_blueprint(course, url_prefix='/course')
    # app.register_blueprint(student, url_prefix='/student')
   
    return app
