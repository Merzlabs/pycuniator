from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class StateMapValues:
    def __init__(self, authorize_url:str, consent_id:str, code_verifier:str):
        #TODO error handling and raising if something does not exist
        self.authorize_url = authorize_url
        self.consent_id = consent_id
        self.code_verifier = code_verifier
