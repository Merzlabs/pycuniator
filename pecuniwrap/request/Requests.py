import requests
from json import dumps as json_dumps

from pecuniwrap.request.RequestId import RequestId

class Requests():
    def __init__(self, cert_path: str, priv_key_path:str):
        self._cert = (cert_path, priv_key_path)
        self._base_headers = {"x-request-id": str(RequestId().id)}

    #TODO other put and delete and so on

    def get(self,url, in_headers:dict={}, in_parameters:dict={}):
        headers = self._base_headers.copy()
        headers.update(in_headers)
        
        params = {}
        params.update(in_parameters)

        r = requests.get(url, params=params, headers=headers, cert=self._cert, verify=True)
        #TODO error handling for status codes
        return r

    def post(self,url:str, in_headers: dict, body:dict):
        #jsonify body dict for request
        body = json_dumps(body)

        headers = self._base_headers.copy()
        headers["Content-Type"] = "application/json"
        
        headers.update(in_headers)
        
        r = requests.post(url, data=body, headers=headers, cert=self._cert, verify=True)
        #TODO error handling for different status code
        return r