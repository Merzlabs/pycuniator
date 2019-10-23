from pecuniwrap.exceptions.InvalidConfigError import InvalidConfigError

class CuniatorConfiguration():
    def __init__(self, host: str, port: int, path: str, version: str, tppredirecturi: str, iban: str, wellknown: str, tpp_client_id:str):
        missingParameters = []
        
        if host is None: missingParameters.append('PT_HOST')
        if port is None: missingParameters.append('PT_PORT') 
        if path is None: missingParameters.append('PT_PATH')
        if version is None: missingParameters.append('PT_VERS')
        if tppredirecturi is None: missingParameters.append('PT_TPPREDIRECTURI')
        if iban is None: missingParameters.append('PT_IBAN')
        if wellknown is None: missingParameters.append('PT_WELLKNOWN')
        if tpp_client_id is None: missingParameters.append('TPP_CLIENT_ID')

        if len(missingParameters) > 0:
            raise InvalidConfigError(missingParameters)

        self.host = host
        self.port = port
        self.path = path
        self.version = version
        self.tppredirecturi = tppredirecturi
        self.iban = iban
        self.wellknown = wellknown
        self.tpp_client_id = tpp_client_id

        self.full_url = 'https://' + self.host + ':' + self.port
        self.full_url += '/' + self.path
        self.full_url += '/' + self.version + '/'