from pecuniwrap.Configuration import CuniatorConfiguration
from pecuniwrap.request.Requests import Requests
from pecuniwrap.ais.models.Accounts import Accounts

from pecuniwrap.AccessCredentials import AccessCredentials

class AccountInformationService:

    def __init__(self, config: CuniatorConfiguration, requests: Requests, accessCredentials: AccessCredentials):
        self._config = config
        self._requests = requests
        self._accessCredentials = accessCredentials

    def getAccountsWithBalance(self) -> Accounts:
        # accounts?withBalance=true
        headers = {
            "Consent-ID": self._accessCredentials.consent_id,
            "Authorization": self._accessCredentials.access_token, 
        }
        parameters = {
            "withBalance": "true"
        }
        url = self._config.full_url + 'accounts'

        r = self._requests.get(url,headers,parameters)
        print(r.url)
        print(r.json())
        schema = Accounts()
        accountInfo = schema.load(r.json())
        return schema.dump(accountInfo)

# TODO get transactions method and route in web