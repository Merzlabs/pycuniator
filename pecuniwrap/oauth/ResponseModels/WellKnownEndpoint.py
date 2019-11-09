from marshmallow import Schema,fields 

class WellKnownEndpointResponse(Schema):
    class Meta:
        strict = True
    jwks_uri = fields.Url()
    authorization_endpoint = fields.Url()
    token_endpoint = fields.Url()
