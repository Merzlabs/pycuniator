from marshmallow import Schema,fields 

class TokenEnpointResponse(Schema):
    class Meta:
        strict = True
    access_token = fields.Str()
    token_type = fields.Str()
    refresh_token = fields.Str()
    expires_in = fields.Int()
