import json

from src.utils.request_engine import RequestEngine


class GitApi():
    request_engine = RequestEngine()

    def get_all_users(self, url):
        # url="https://api.github.com/users?page=1&per_page=100&since=0"
        # params= {"page":1,"per_page":100,"since":0}
        return self.request_engine.request_sender(url_link=url, params=None, request_type="GET")
