import pytest

from brownie import HelloWorld, accounts

@pytest.fixture
def helloWorld():
    return accounts[0].deploy(HelloWorld)

def test_greet(helloWorld):    
    assert helloWorld.greet() == "Hello World"