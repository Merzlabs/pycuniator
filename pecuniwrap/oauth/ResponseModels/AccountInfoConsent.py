from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class AccountInfoConsent:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.consentStatus = inDict["consentStatus"]
            self.consentId = inDict["consentId"]
            self.psuMessage = inDict["psuMessage"]
            self.links = {
                'scaOAuth': {
                    'href': inDict["_links"]["scaOAuth"]["href"]
                },
                'self': {
                    'href': inDict["_links"]["self"]["href"]
                },
                'status': {
                    'href': inDict["_links"]["status"]["href"]
                }
            }
        except KeyError as e:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)

        if (self.consentStatus is None or self.consentId is None 
                    or self.psuMessage is None or self.links is None):
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)            

    #TODO stringify and print methods for all these models