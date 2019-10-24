class OAuthFlowError(Exception):
    def __init__(self):
        #TODO catch this in token endpoint and return message as json response
        super().__init__('No values found for this request. Please start the oauth flow correctly')