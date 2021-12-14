import json
import jsonschema
import os
from checkers.checkerApiUser import CheckerApiUser


class CheckersContainer:
    def __init__(self):
        self.checkerApiUser = CheckerApiUser()

    def getSchema(self, schemaFileName):
        with open(f'../schemas/{schemaFileName}.json', 'r') as file:
        # with open(f'{os.getcwd()}/schemas/{schemaFileName}.json', 'r') as file:
            schema = json.load(file)
        return schema

    def validateSchema(self, schemaFileName, jsonData):
        jsonSchema=self.getSchema(schemaFileName)

        try:
            jsonschema.validate(instance=jsonData, schema=jsonSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        else:
            # print('schema OK')
            return True

# для внутренних проверок
if __name__ == '__main__':
    chec = CheckersContainer()
    print(chec.getSchema('schemaPostUserResp'))
    jsonData = {
        "code": 200,
        "type": "200",
        "message": "9223372036854775807"
    }
    chec.validateSchema('schemaPostUserResp', jsonData)


