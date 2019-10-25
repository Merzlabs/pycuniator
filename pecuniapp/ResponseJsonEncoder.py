import json
import functools
from flask import make_response

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):  # pylint: disable=E0202
        #cause false positive of lint here
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

    @staticmethod
    def toJson(inObjects):
        return json.dumps(inObjects.reprJSON(), cls=JsonEncoder)


def return_json(f):
    @functools.wraps(f)
    def inner(*a, **k):
        #TODO ability to give in status code to use
        response = make_response(JsonEncoder.toJson(f(*a, **k)))
        response.headers['content-type'] = 'application/json'
        return response
    return inner