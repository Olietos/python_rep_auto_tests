from clients.user import ApiUser
from clients.session import ApiSessions

class ApiContainer:
    def __init__(self, url):
        self.apiUser=ApiUser(url)
        self.session=ApiSessions()