import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Crear tablas si no existen.
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello, World!'

