from marshmallow import Schema,fields

# from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class BalanceAmount(Schema):
    currency = fields.Str()
    amount = fields.Float()

class Balance(Schema):
    balanceType = fields.Str()    
    balanceAmount = fields.Nested(BalanceAmount)
    referenceDate = fields.DateTime(format="%Y-%m-%d") 

class HrefLinks(Schema):
    href = fields.Url()

class Links(Schema):
    balances = fields.Nested(HrefLinks)
    transactions = fields.Nested(HrefLinks)

class Account(Schema):
    ownerName = fields.Str()
    resourceId = fields.UUID() #TODO is uuid4
    iban = fields.Str()  #TODO custom iban validator for marshmallow
    currency = fields.Str()
    product = fields.Str()
    balances = fields.Nested(Balance(many=True))
    _links = fields.Nested(Links)

class Accounts(Schema):
    accounts = fields.Nested(Account(many=True))

    #TODO useful error if {'tppMessages': [{'category': 'ERROR', 'code': 'CONSENT_UNKNOWN'}]} basically if tppMessage is there
    # tppMessages = fields.Str()
