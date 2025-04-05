from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Post
from app.models import Category

posts_bp = Blueprint ('posts',__name__)

