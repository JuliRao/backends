# coding: utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@0.0.0.0:1050/wsm?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PIC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/pic/")

db = SQLAlchemy(app)
