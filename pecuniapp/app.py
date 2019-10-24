from flask import Flask,redirect, request
from dotenv import load_dotenv, find_dotenv
import os

from pecuniwrap.Pycuniator import Pycuniator
from pecuniwrap.request.RequestId import RequestId as Uuid

secrets_folder = 'secrets'
#TODO do this better
secrets_base_path = os.path.abspath(os.path.dirname(__file__)).replace('pecuniapp', '') + '/' + secrets_folder + '/'
print(secrets_base_path)
load_dotenv(secrets_base_path + '/sandbox.env')

PT_HOST = os.getenv('PT_HOST')
PT_PORT = os.getenv('PT_PORT')
PT_PATH = os.getenv('PT_PATH')
PT_VERS = os.getenv('PT_VERS')
PT_TPPREDIRECTURI = os.getenv('PT_TPPREDIRECTURI')
PT_IBAN = os.getenv('PT_IBAN')
PT_WELLKNOWN = os.getenv('PT_WELLKNOWN')

CERT_PATH=secrets_base_path + os.getenv('CERT_PATH')
PRIV_KEY_PATH=secrets_base_path + os.getenv('PRIV_KEY_PATH')
TPP_CLIENT_ID = os.getenv('TPP_CLIENT_ID')

app = Flask(__name__)
# app.config['port'] = PT_TPPREDIRECTURI.split(":")[1].split("/")[0]

cuniator = Pycuniator(PT_HOST,PT_PORT, PT_PATH,PT_VERS,PT_TPPREDIRECTURI,PT_IBAN,PT_WELLKNOWN, CERT_PATH, PRIV_KEY_PATH, TPP_CLIENT_ID)

access_token = None

@app.route('/authorize')
def authorizeUrl():
    state = str(Uuid().id)
    authorize_url = cuniator.get_authorize_url(state)
    return redirect(authorize_url)

@app.route('/redirect')
def redirectToken():
    code = request.args.get('code')
    state = request.args.get('state')

    if code is None or state is None:
        #TODO return 400 failed request
        pass

    token = cuniator.get_token(code, state)
    
    global access_token
    access_token = token
    
    return str(token.access_token)

@app.route('/ais')
def aisTest():
    s = cuniator.get_Balance()
    #TODO give in token and do new ais for every token requests to not have this globally
    return 