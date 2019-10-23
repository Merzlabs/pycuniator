from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class TokenEnpointResponse:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.access_token = inDict["access_token"]
            self.token_type = inDict["token_type"]
            self.refresh_token = inDict["refresh_token"]
            self.expires_in = inDict["expires_in"]
        except KeyError as e:
            raise InvalidResponseError(None, inDict,e)

    #TODO stringify and print methods for all these models
