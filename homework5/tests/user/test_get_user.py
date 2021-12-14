def test_positive(baseFixture, dataUserFixture):
    sessionToken = baseFixture.configs.authToken
    iInputPostUser = dataUserFixture.getDataPostUser()
    baseFixture.api.apiUser.postUserDict(**iInputPostUser)
    responseGet = baseFixture.api.apiUser.getUser(iInputPostUser['username'])

    assert \
        responseGet.status_code == 200 and \
        baseFixture.checkerContainer.validateSchema('schemaGetUserResp', responseGet.json()) and \
        baseFixture.checkerContainer.checkerApiUser.checkGetUser(responseGet, iInputPostUser)

