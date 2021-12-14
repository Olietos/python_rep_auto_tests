def test_positive(baseFixture, dataUserFixture):
    sessionToken = baseFixture.configs.authToken
    iInputPostUser = dataUserFixture.getDataPostUser()
    baseFixture.api.apiUser.postUserDict(**iInputPostUser)
    iInputPutUser = dataUserFixture.getDataPutUser()
    response = baseFixture.api.apiUser.putUserDict(**iInputPutUser)
    responseGet = baseFixture.api.apiUser.getUser(iInputPutUser['username'])

    assert \
        response.status_code == 200 and \
        baseFixture.checkerContainer.validateSchema('schemaPutUserResp', response.json(), baseFixture.ROOT_DIR) and \
        baseFixture.checkerContainer.checkerApiUser.checkPutUser(response, responseGet, iInputPutUser)
