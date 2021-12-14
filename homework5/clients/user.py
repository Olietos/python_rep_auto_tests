import requests


class ApiUser:
    def __init__(self, url):
        self.url = url
        self.headers = {"Accept": "application/json", "content-type": "application/json"}

    def postUserDict(self, **iInputData):
        iApiMethod = f"/v2/user"
        iUrl = self.url + iApiMethod
        iHeaders = self.headers.copy()

        iReqDict = {
            "id": iInputData['userId'],
            "username": iInputData['username'],
            "firstName": iInputData['firstName'],
            "lastName": iInputData['lastName'],
            "email": iInputData['email'],
            "password": iInputData['password'],
            "phone": iInputData['phone'],
            "userStatus": 0
        }

        iResponse = requests.request("POST", iUrl, headers=iHeaders, json=iReqDict)
        return iResponse

    def putUserDict(self, **iInputData):
        tmpiInputData=iInputData['username']
        iApiMethod = f"/v2/user/{tmpiInputData}"
        iUrl = self.url + iApiMethod
        iHeaders = self.headers.copy()

        iReqDict = {
            "id": iInputData['userId'],
            "username": iInputData['userName'],
            "firstName": iInputData['firstName'],
            "lastName": iInputData['lastName'],
            "email": iInputData['email'],
            "password": iInputData['password'],
            "phone": iInputData['phone'],
            "userStatus": 0
        }

        iResponse = requests.request("PUT", iUrl, headers=iHeaders, json=iReqDict)
        return iResponse

    def postUser(self, userId, userName, firstName, lastName, email, password, phone):
        iApiMethod = f"/v2/user"
        iUrl = self.url + iApiMethod
        iHeaders = self.headers.copy()

        iReqDict = {
            "id": userId,
            "username": userName,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": 0
        }

        iResponse = requests.request("POST", iUrl, headers=iHeaders, json=iReqDict)
        return iResponse

    def putUser(self, userId, userName, firstName, lastName, email, password, phone):
        iApiMethod = f"/v2/user/{userName}"
        iUrl = self.url + iApiMethod
        iHeaders = self.headers.copy()

        iReqDict = {
            "id": userId,
            "username": userName,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": 0
        }

        iResponse = requests.request("PUT", iUrl, headers=iHeaders, json=iReqDict)
        return iResponse

    def getUser(self, userName):
        iApiMethod = f"/v2/user/{userName}"
        iUrl = self.url + iApiMethod
        iHeaders = self.headers.copy()

        iResponse = requests.request("GET", iUrl, headers=iHeaders)
        return iResponse
