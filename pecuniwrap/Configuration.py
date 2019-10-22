from .exceptions.InvalidConfigError import InvalidConfigError

class CuniatorConfiguration():
    def __init__(self, host: str, port: int, path: str, version: str, tppredirecturi: str, iban: str, wellknown: str):
        missingParameters = []
        
        if host is None: missingParameters.append('PT_HOST')
        if port is None: missingParameters.append('PT_PORT') 
        if path is None: missingParameters.append('PT_PATH')
        if version is None: missingParameters.append('PT_VERS')
        if tppredirecturi is None: missingParameters.append('PT_TPPREDIRECTURI')
        if iban is None: missingParameters.append('PT_IBAN')
        if wellknown is None: missingParameters.append('PT_WELLKNOWN')

        if len(missingParameters) > 0:
            raise InvalidConfigError(missingParameters)

        self._host = host
        self._port = port
        self._path = path
        self._version = version
        self._tppredirecturi = tppredirecturi
        self._iban = iban
        self._wellknown = wellknown