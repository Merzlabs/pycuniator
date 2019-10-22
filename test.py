from dotenv import load_dotenv, find_dotenv
from os import getenv

from pecuniwrap.Pycuniator import Pycuniator

# Loading env vars
load_dotenv('secrets/sandbox.env')

PT_HOST = getenv('PT_HOST')
PT_PORT = getenv('PT_PORT')
PT_PATH = getenv('PT_PATH')
PT_VERS = getenv('PT_VERS')
PT_TPPREDIRECTURI = getenv('PT_TPPREDIRECTURI')
PT_IBAN = getenv('PT_IBAN')
PT_WELLKNOWN = getenv('PT_WELLKNOWN')

# To test config error
# PT_WELLKNOWN = None

cuniator = Pycuniator(PT_HOST,PT_PORT, PT_PATH,PT_VERS,PT_TPPREDIRECTURI,PT_IBAN,PT_WELLKNOWN)