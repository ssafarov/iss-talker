import json
from urllib import parse, request

from requests import HTTPError

"""API class: open-notify.org api interaction"""


class Api:

    def __init__(self):
        self.url = 'http://api.open-notify.org/'

    """ This function is core API requester, 
    it could accept mode string as parameter: people/location """

    def _api_request(self, mode, arg=""):
        try:
            if mode == 'people':
                end_point = 'astros.json'
            elif mode == 'location':
                end_point = 'iss-now.json'
            elif mode == 'pass':
                end_point = 'iss-pass.json'
            else:
                return {'status': False, 'message': 'Unknown mode'}
            if len(arg) > 0:
                arg = '?' + arg
            url = parse.quote(self.url + end_point + arg, safe='/:?&=')
            api_response = request.urlopen(url)
        except HTTPError as e:
            if e.code < 500:
                data = json.loads(e.read())
            else:
                data = {'reason': e.reason, 'code': e.code, 'message': e.reason}
            return {**{'status': False}, **data}
        else:
            return json.loads(api_response.read())

    """ This function will return people dictionary structure or error message from API response """

    def get_people_onboard(self):
        response = self._api_request('people')
        status = ('message' in response) and response['message'] == 'success'
        return {**{'status': status}, **response}

    """ This function will return location dictionary structure or error message from API response """

    def get_location(self):
        response = self._api_request('location')
        status = ('message' in response) and response['message'] == 'success'
        return {**{'status': status}, **response}

    """ This function will return location dictionary structure or error message from API response """

    def get_pass_details(self, lat, long):
        response = self._api_request('pass', 'lat=' + lat + '&lon=' + long)
        status = ('message' in response) and response['message'] == 'success'
        return {**{'status': status}, **response}
