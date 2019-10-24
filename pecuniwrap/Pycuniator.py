from pecuniwrap.AccessCredentials import AccessCredentials

from pecuniwrap.exceptions.InvalidConfigError import InvalidConfigError
from pecuniwrap.Configuration import CuniatorConfiguration
from pecuniwrap.request.Requests import Requests
from pecuniwrap.oauth.OAuth import OAuth

from pecuniwrap.ais.AIS import AccountInformationService
from pecuniwrap.ais.models.Accounts import Accounts

class Pycuniator():
    def __init__(self, host: str, port: int, path: str, version: str, tppredirecturi: str, iban: str, wellknown: str, cert_path:str, private_key_path:str, tpp_client_id:str):
        self._config = CuniatorConfiguration(host,port,path,version,tppredirecturi,iban,wellknown, tpp_client_id)
        self._requests = Requests(cert_path,private_key_path)
        self._oauth = OAuth(self._config, self._requests)

    def cli_login(self) -> AccessCredentials:
        credentials: AccessCredentials = self._oauth.cli_login_credentials()
        self._credentials: AccessCredentials = credentials
        self._ais: AccountInformationService = AccountInformationService(self._config, self._requests, self._credentials)
        return credentials

    def get_authorize_url(self, state) -> str:
        return self._oauth.get_login_url(state)

    def get_token(self,code:str, state:str) -> AccessCredentials:
        credentials: AccessCredentials = self._oauth.token_retrieval(code, state)
        self._ais: AccountInformationService = AccountInformationService(self._config, self._requests, credentials)
        return credentials
        
    def get_Balance(self) -> Accounts:
        return self._ais.getAccountsWithBalance()