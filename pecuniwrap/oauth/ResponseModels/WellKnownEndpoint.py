from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class WellKnownEndpointResponse:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.jwks_uri = inDict["jwks_uri"]
            self.authorization_endpoint = inDict["authorization_endpoint"]
            self.token_endpoint = inDict["token_endpoint"]
        except KeyError as e:
            raise InvalidResponseError(None, inDict,e)

    #TODO stringify and print methods for all these models
