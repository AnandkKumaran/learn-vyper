import pytest

from brownie import Pokemon, accounts

@pytest.fixture
def pokemon():
    return accounts[0].deploy(Pokemon)

def test_totalPokemonCount(pokemon):    
    assert pokemon.totalPokemonCount() == 0

def test_totalPokemonCountAfterCreatePokemon(pokemon):   
    pokemon.createPokemon("Bulbasaur")
    assert pokemon.totalPokemonCount() == 1