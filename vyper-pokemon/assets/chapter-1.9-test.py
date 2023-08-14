import pytest

from brownie import Pokemon, accounts

@pytest.fixture
def pokemon():
    return accounts[0].deploy(Pokemon)

def test_greet(pokemon):    
    assert pokemon.totalPokemonCount() == 0