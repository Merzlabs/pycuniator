class InvalidConfigError(Exception):
    def __init__(self, parameters):
        super().__init__('Following parameters were not defined while instantiating Pycuniator: ' + str(parameters))
        self.parameters = parameters