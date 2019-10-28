from pecuniwrap.exceptions.InvalidResponseError import InvalidResponseError

class Accounts:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.accounts = []
            for account in inDict["accounts"]:
                self.accounts.append(Account(account))
        except KeyError as e:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)

        if (self.accounts is None):
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)  
    def reprJSON(self):
        return dict(accounts=self.accounts) 

class Account:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.resourceId = inDict["resourceId"]            
            self.iban = inDict["iban"]            
            self.currency = inDict["currency"]            
            self.product = inDict["product"]

            self.balances = []
            for balance in inDict["balances"]:
                self.balances.append(Balance(balance))

            #TODO _links attribute e.g.
            # "_links": {
            #     "balances": {
            #         "href": "https://xs2a-sandbox.f-i-apim.de:8444/fixs2a-env/xs2a-api/12345678/v1/accounts/3217d050-f5b5-4318-a799-413bce784ef6/balances"
            #     },
            #     "transactions": {
            #         "href": "https://xs2a-sandbox.f-i-apim.de:8444/fixs2a-env/xs2a-api/12345678/v1/accounts/3217d050-f5b5-4318-a799-413bce784ef6/transactions"
            #     }
            # }

        except KeyError as e:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)

        if (self.resourceId is None or self.iban is None or self.currency is None
                or self.product is None or self.balances is None or self.iban is None):
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)
    def reprJSON(self):
        return dict(resourceId=self.resourceId, iban=self.iban,currency=self.currency,product=self.product, balances=self.balances) 

class Balance:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.balanceType = inDict["balanceType"]            
            self.balanceAmount = BalanceAmount(inDict["balanceAmount"])           
            self.referenceDate = inDict["referenceDate"]            
        except KeyError as e:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)

        if (self.balanceType is None or self.balanceAmount is None or self.referenceDate is None):
            #TODO inputs
            raise InvalidResponseError(None, inDict, e) 
    def reprJSON(self):
        return dict(balanceType=self.balanceType, balanceAmount=self.balanceAmount, referenceDate=self.referenceDate) 

class BalanceAmount:
    def __init__(self, inDict: dict):
        #TODO error handling and raising if something does not exist
        try:
            self.currency = inDict["currency"]            
            self.amount = inDict["amount"]            
        except KeyError as e:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)

        if (self.currency is None) or self.amount is None:
            #TODO inputs
            raise InvalidResponseError(None, inDict, e)
    def reprJSON(self):
        return dict(currency=self.currency, amount=self.amount) 