import json


class CheckerApiUser:
    def __init__(self):
        pass

    def checkPostUser(self, response, responseGet=None, initData=None):

        checkFlag = True

        if responseGet is not None and initData is not None:
            if 'username' in responseGet.json() and responseGet.json()['username'] == initData['username']:
                checkFlag = True
            else:
                checkFlag = False
                return checkFlag

        if response.json()['code'] == 200 and response.json()['type'] == 'unknown':
            checkFlag = checkFlag and True
        else:
            checkFlag = False
            return checkFlag

        return checkFlag

    def checkPutUser(self, response, responseGet=None, initData=None):
        checkFlag = True

        if responseGet is not None and initData is not None:
            if 'username' in responseGet.json() and \
                    responseGet.json()['username'] == initData['username'] and \
                    responseGet.json()['firstName'] == initData['firstName']:
                checkFlag = True
            else:
                checkFlag = False
                return checkFlag

        if response.json()['code'] == 200 and response.json()['type'] == 'unknown':
            checkFlag = checkFlag and True
        else:
            checkFlag = False
            return checkFlag

        return checkFlag

    def checkGetUser(self, responseGet, initData):
        checkFlag = True

        if 'username' in responseGet.json() and responseGet.json()['username'] == initData['username'] and responseGet.json()['firstName'] == initData['firstName']:
            checkFlag = True
        else:
            checkFlag = False
            return checkFlag

        return checkFlag
