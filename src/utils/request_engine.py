import os

from requests.adapters import HTTPAdapter
import requests
from requests.auth import HTTPBasicAuth

username = "sanemeroglu"


# password= #gettoken
class RequestEngine(object):
    def request_sender(self, url_link, request_type, params=None, headers=None, body_params=None):
        response = ""
        adapter = HTTPAdapter(max_retries=5)
        session = requests.Session()
        session.mount(url_link, adapter)
        try:
            if request_type == "GET":
                response = session.get(url=url_link, params=params, headers=headers,
                                       auth=HTTPBasicAuth(username, password))
            else:
                response = session.post(url=url_link, data=body_params, headers=headers, params=params,
                                        auth=HTTPBasicAuth(username, password))
        except ConnectionError as e:
            print(e)
            # os.exit(1)
        return response
