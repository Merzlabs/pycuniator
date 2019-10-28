
from dotenv import load_dotenv
import os

class PecuniAppConfig:
    def __init__(self):
        secrets_folder = 'secrets'
        #TODO do this better
        secrets_base_path = os.path.abspath(os.path.dirname(__file__)).replace('pecuniapp', '') + '/' + secrets_folder + '/'
        # print(secrets_base_path)
        load_dotenv(secrets_base_path + '/sandbox.env')

        self.PT_HOST = os.getenv('PT_HOST')
        self.PT_PORT = os.getenv('PT_PORT')
        self.PT_PATH = os.getenv('PT_PATH')
        self.PT_VERS = os.getenv('PT_VERS')
        self.PT_TPPREDIRECTURI = os.getenv('PT_TPPREDIRECTURI')
        self.PT_IBAN = os.getenv('PT_IBAN')
        self.PT_WELLKNOWN = os.getenv('PT_WELLKNOWN')

        self.CERT_PATH=secrets_base_path + os.getenv('CERT_PATH')
        self.PRIV_KEY_PATH=secrets_base_path + os.getenv('PRIV_KEY_PATH')
        self.TPP_CLIENT_ID = os.getenv('TPP_CLIENT_ID')
