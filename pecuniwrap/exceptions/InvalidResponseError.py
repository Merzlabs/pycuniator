class InvalidResponseError(Exception):
    def __init__(self, endpoint:str, reponse: dict, message: str):
        #TODO maybe give in expected to compare
        #TODO useful error message
        super().__init__('Response returned by X2SA API did not conform to data model: ' + str(endpoint) + str(message))