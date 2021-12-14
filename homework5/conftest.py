import pytest

from application import Application
from helpers.dataFabric import dataFabric

fixture = Application()


@pytest.fixture(scope="session")
def baseFixture():
    return fixture

@pytest.fixture(scope="module")
def dataUserFixture():
    data = dataFabric().getDataApiUser()
    return data