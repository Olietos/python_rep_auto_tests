from config import Config
# from helpers.genDataApiUser import GenDataApiUser
from clients.apiContainer import ApiContainer
from checkers.checkersContainer import CheckersContainer

class Application:
    def __init__(self):
        self.configs = Config()
        # self.genDataApiUser = GenDataApiUser()
        self.api = ApiContainer(self.configs.url)
        self.checkerContainer = CheckersContainer()
