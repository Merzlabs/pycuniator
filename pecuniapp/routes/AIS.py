from flask import Blueprint, redirect,request,jsonify,make_response
import json

from pecuniwrap.ais.AIS import AccountInformationService
from pecuniwrap.Pycuniator import Pycuniator

from pecuniapp.Config import PecuniAppConfig
c = PecuniAppConfig()

ais_bp = Blueprint('ais_bp', __name__)


#TODO flask_smorest and return of accountsSchema openapi and so on
@ais_bp.route('/balance')
def aisTest():
    consent_id = request.headers.get('consent_id')
    token = request.headers.get('authorization')

    cuniator = Pycuniator(c.PT_HOST,c.PT_PORT, c.PT_PATH,c.PT_VERS,c.PT_TPPREDIRECTURI,c.PT_IBAN,c.PT_WELLKNOWN, c.CERT_PATH, c.PRIV_KEY_PATH, c.TPP_CLIENT_ID)
    cuniator.setAis(consent_id,token)
    
    result = cuniator.ais.getAccountsWithBalance()

    # uses return json funcwrapper to serialize returned object
    return result

