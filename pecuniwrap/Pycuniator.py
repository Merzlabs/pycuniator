from .exceptions.InvalidConfigError import InvalidConfigError
from .Configuration import CuniatorConfiguration

class Pycuniator():
    def __init__(self, host: str, port: int, path: str, version: str, tppredirecturi: str, iban: str, wellknown: str):
        self._config = CuniatorConfiguration(host,port,path,version,tppredirecturi,iban,wellknown)

    def _login(self):
        pass