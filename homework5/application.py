import os

from config import Config
# from helpers.genDataApiUser import GenDataApiUser
from clients.apiContainer import ApiContainer
from checkers.checkersContainer import CheckersContainer


class Application:
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.configs = Config()
        # self.genDataApiUser = GenDataApiUser()
        self.api = ApiContainer(self.configs.url)
        self.checkerContainer = CheckersContainer()
        self.authToken = self.try_login(self.configs.email, self.configs.password)
        self.authToken = self.configs.authToken if "unsuccessful login" in self.authToken else self.authToken

    def try_login(self, email, password):
        try:
            response = self.api.session.post_login(email, password)
            return response.json()["data"]["key"]["access_token"]
        except:
            return f"unsuccessful login as {email}"
