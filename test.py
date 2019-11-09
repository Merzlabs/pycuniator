from dotenv import load_dotenv, find_dotenv
import os

from pecuniwrap.Pycuniator import Pycuniator

secrets_folder = 'secrets'
secrets_base_path= os.path.abspath(os.path.dirname(__file__)) + '/' + secrets_folder + '/'
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

# To test config error
# PT_WELLKNOWN = None

cuniator = Pycuniator(PT_HOST,PT_PORT, PT_PATH,PT_VERS,PT_TPPREDIRECTURI,PT_IBAN,PT_WELLKNOWN, CERT_PATH, PRIV_KEY_PATH, TPP_CLIENT_ID)

tokens = cuniator.cli_login()
cuniator.setAis(tokens.consent_id,tokens.access_token)

# cuniator.test()
print(cuniator.ais.get_Balance().accounts[0].iban)