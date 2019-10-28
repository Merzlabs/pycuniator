from flask import Flask,redirect, request,jsonify, render_template  
from dotenv import load_dotenv, find_dotenv
import os

from pecuniwrap.Pycuniator import Pycuniator

from pecuniapp.Config import PecuniAppConfig
c = PecuniAppConfig()


app = Flask(__name__)
# app.config['port'] = PT_TPPREDIRECTURI.split(":")[1].split("/")[0]

from pecuniapp.routes.OAuth import oauth_flow
from pecuniapp.routes.AIS import ais_bp

app.register_blueprint(oauth_flow,  url_prefix='/oauth')
app.register_blueprint(ais_bp,  url_prefix='/ais')

@app.route('/')
def indexTemp():
    return render_template('index.html')
