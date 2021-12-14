import random
import string


class GenDataApiUser:
    def __init__(self):
        self.id = random.randint(0, 1000000)
        self.userName = 'UserName' + ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        self.firstName = 'FirstName' + ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        self.lastName = 'LastName' + ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        self.email = ''.join(random.choice(string.ascii_uppercase) for i in range(10)) + '@mail.com'
        self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))
        self.phone = ''.join(random.choice(string.digits) for i in range(11))

        self.dataDict = {'id': self.id,
                         'username': self.userName,
                         'firstName': self.firstName,
                         'lastName': self.lastName,
                         'email': self.email,
                         'password': self.password,
                         'phone': self.phone}

    def getDataPostUser(self):
        return self.dataDict

    def getDataPutUser(self):
        self.dataDict['firstName']=self.dataDict['firstName'] + 'PUT'
        return self.dataDict
