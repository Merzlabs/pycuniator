from base64 import urlsafe_b64encode
from os import urandom
from re import sub as re_sub
from hashlib import sha256 as hash_sha256
import urllib.parse

from pecuniwrap.Configuration import CuniatorConfiguration
from pecuniwrap.AccessCredentials import AccessCredentials
from pecuniwrap.exceptions.OAuthFlowError import OAuthFlowError

from pecuniwrap.request.Requests import Requests
from pecuniwrap.oauth.PKCE import PKCE
from pecuniwrap.oauth.StateMapValues import StateMapValues

from pecuniwrap.oauth.ResponseModels.WellKnownEndpoint import WellKnownEndpointResponse
from pecuniwrap.oauth.ResponseModels.AccountInfoConsent import AccountInfoConsent
from pecuniwrap.oauth.ResponseModels.TokenEnpoint import TokenEnpointResponse


class OAuth:
    def __init__(self, config: CuniatorConfiguration, requests: Requests):
        self._config = config
        self._requests = requests

        #TODO implement this with database to be stateless function
        self.stateMap = {}

    # 1 use well known endpoint to get specific oauth endpoints for banks
    def _well_known_endpoint_info(self) -> WellKnownEndpointResponse:
        r = self._requests.get(self._config.wellknown)
        info = WellKnownEndpointResponse(r.json())
        return info

    # 2. requests consent to input into authorize redirect url which prompt user
    # which permissions should be requested
    def _account_info_consent(self) -> AccountInfoConsent:
        consent_url = self._config.full_url + 'consents'
        headers = {
            #TODO review these headers
            'TPP-Redirect-Preferred': 'true',
            'TPP-Redirect-URI': self._config.tppredirecturi
        }
        #TODO more configurable consent not just postman copy
        iban = self._config.iban
        body = {
            "access": {
                "balances": [{
                        "iban": iban
                    }
                ],
                "transactions": [{
                        "iban": iban
                    }
                ]
            },
            "recurringIndicator": True,
            "validUntil": '2019-11-01', #TODO make logic for this
            "frequencyPerDay": 4,
            "combinedServiceIndicator": False
        }
        r = self._requests.post(consent_url, headers, body)
        print(r.text)
        consent = AccountInfoConsent(r.json())
        return consent

    # 3. Construct authorize url which user should open to enter credentials
    def _authorize_url(self, authorization_endpoint: str, consentId: str, code_challenge:str, state:str):
        authorize_url = 'responseType=code'
        authorize_url += '&client_id='+ self._config.tpp_client_id
        authorize_url += '&scope=AIS:' + urllib.parse.quote(' ' + consentId)
        authorize_url += '&state=' + urllib.parse.quote(state)
        authorize_url += '&code_challenge_method=S256'
        authorize_url += '&code_challenge=' + code_challenge
        authorize_url += '&redirect_uri=' + urllib.parse.quote(self._config.tppredirecturi)
        # returned errors of this method with unexpected error when e.g. scope is wrong are super not helpful so be aware and check all url param thoroughly
        # to debug what is wrong inspect form of webpage and look at hidden fields whats missing

        return_authorize_url = authorization_endpoint + '?' + authorize_url
        return return_authorize_url
    
    # 4. Use code got from redirect to get a token to use
    def _token_from_code(self, token_endpoint:str, code:str, code_challenge:str) -> TokenEnpointResponse:
        headers = {
            #TODO content type form encoded like in postman? or leave empty
        }
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self._config.tpp_client_id, #TODO set this in env an get here from config
            "code_verifier": code_challenge
        }
        r = self._requests.post(token_endpoint, headers, body)
        print(r.text)
        return TokenEnpointResponse(r.json())

    #TODO method with SOCKET waiting for reponse redirect rule call

    #TODO return types
    def get_login_url(self, state:str="cliEmpty"):
        well_known_info = self._well_known_endpoint_info()
        pkce = PKCE()

        consent_id = self._account_info_consent().consentId
        authorize_url = self._authorize_url(well_known_info.authorization_endpoint, consent_id, pkce.code_challenge, state)

        self.stateMap[state] = StateMapValues(authorize_url,consent_id,pkce.code_verifier)
        print(self.stateMap)
        return authorize_url

    def token_retrieval(self,code:str, state:str='cliEmpty')-> AccessCredentials:
        print(self.stateMap)
        try:
            stateValues = self.stateMap[state]
        except KeyError:
            raise OAuthFlowError()

        consent_id = stateValues.consent_id
        code_verifier = stateValues.code_verifier

        token_endpoint = self._well_known_endpoint_info().token_endpoint
        tokenModel = self._token_from_code(token_endpoint, code, code_verifier)
        print("Consent ID: " + consent_id)
        print("Access Token: " + tokenModel.access_token)
        accessCredentials = AccessCredentials(consent_id, tokenModel.access_token)
        return accessCredentials

    # whole login flow to get valid token
    def cli_login_credentials(self) -> AccessCredentials:
        authorize_url = self.get_login_url()
        print('Open in browser: ' + authorize_url)

        # TODO cli only method here parallel version
        print('Input code received:')
        code = input()
        return self.token_retrieval(code)


    # @app.route('/')
    # def hello_world(self):
    #     self.cont = True
    #     del app
    #     return 'Hello, World!'