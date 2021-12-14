from clients.user import ApiUser

class ApiContainer:
    def __init__(self, url):
        self.apiUser=ApiUser(url)