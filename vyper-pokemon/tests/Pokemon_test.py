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

def test_EventNewPokemonCreated(pokemon):   
    name = "Bulbasaur"
    transaction = pokemon.createPokemon(name)
    transaction.wait(1)
    assert transaction.events["NewPokemonCreated"]["name"] == name
    assert transaction.events["NewPokemonCreated"]["dna"] > 0
    assert transaction.events["NewPokemonCreated"]["HP"] > 0