import pytest


def test_positive(baseFixture, dataUserFixture):
    sessionToken = baseFixture.configs.authToken
    # iInputPostUser= baseFixture.genDataApiUser.getDataPostUser()
    iInputPostUser = dataUserFixture.getDataPostUser()
    # print(iInputPostUser)
    response = baseFixture.api.apiUser.postUserDict(**iInputPostUser)
    responseGet = baseFixture.api.apiUser.getUser(iInputPostUser['username'])

    assert \
        response.status_code == 200 and \
        baseFixture.checkerContainer.validateSchema('schemaPstUserResp', response.json()) and \
        baseFixture.checkerContainer.checkerApiUser.checkPostUser(response, responseGet, iInputPostUser)

