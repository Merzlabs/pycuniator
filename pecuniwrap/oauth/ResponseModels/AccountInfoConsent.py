from marshmallow import Schema,fields 

# TODO raise personalized error and catch if model is invalid
# from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class HrefLink(Schema):
    href = fields.Url()

class linkSchema(Schema):
    scaOAuth = fields.Nested(HrefLink)
    self = fields.Nested(HrefLink)
    status = fields.Nested(HrefLink)

class AccountInfoConsent(Schema):
    class Meta:
        strict = True
    consentStatus = fields.Str()
    consentId = fields.Str() #looks like a3245e87-6c83-48a9-9b85-dd18f216ec74 could be uuid
    psuMessage = fields.Str()
    _links = fields.Nested(linkSchema)