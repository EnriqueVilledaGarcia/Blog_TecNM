import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Importar los modelos para que SQLAlchemy los reconozca
from app.models import Post
from app.models import Category

#Importar y registrar los blueprints
from app.routes.post import posts_bp
from app.routes.categories import categories_bp

#Crear tablas si no existen.
with app.app_context():
    db.create_all()


app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(categories_bp, url_prefix='/categories')


@app.route('/')
def index():
    return render_template('index.html')
