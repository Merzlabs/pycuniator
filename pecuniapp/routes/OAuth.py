from flask import Blueprint, redirect,request,jsonify

from pecuniwrap.Pycuniator import Pycuniator
from pecuniwrap.request.RequestId import RequestId as Uuid

from pecuniapp.Config import PecuniAppConfig
c = PecuniAppConfig()

oauth_flow = Blueprint('oauth_flow', __name__)

login_cuniator = Pycuniator(c.PT_HOST,c.PT_PORT, c.PT_PATH,c.PT_VERS,c.PT_TPPREDIRECTURI,c.PT_IBAN,c.PT_WELLKNOWN, c.CERT_PATH, c.PRIV_KEY_PATH, c.TPP_CLIENT_ID)

@oauth_flow.route('/authorize')
def authorizeInit():
    state = str(Uuid().id)
    authorize_url = login_cuniator.get_authorize_url(state)
    return redirect(authorize_url)

@oauth_flow.route('/redirect')
def redirectToken():
    code = request.args.get('code')
    state = request.args.get('state')

    if code is None or state is None:
        #TODO return 400 failed request
        pass

    token = login_cuniator.get_token(code, state)
    return jsonify({"token": token.access_token, "consent_id": token.consent_id})

