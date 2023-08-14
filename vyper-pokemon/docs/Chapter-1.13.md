# Chapter 13: Events

[Tutorial Link](https://learn.vyperlang.org/#/1/events)

Welcome to Chapter 13! In this chapter, we'll explore the concept of events in Vyper. Events are a crucial feature in Ethereum smart contracts that allow contracts to communicate and log information in a decentralized and transparent manner.

## Logging Events in Vyper

To begin, let's update the `Pokemon.vy` contract with your code, which includes logging an event `NewPokemonCreated` whenever a new Pokemon is created:

To test the contract do some adjustments in the pasted code. Please make sure that createPokemon() is an external function, then only we can test it using test scripts.

```python
@external
def createPokemon(_name: String[32]) -> Pokemon:

    randomDNA: uint256 = self._generateRandomDNA(_name)

    randomHP: uint256 = randomDNA % HP_LIMIT

    newPokemon: Pokemon = Pokemon({
        name: _name,
        dna: randomDNA,
        HP: randomHP,
        matches: 0,
        wins: 0
    })

    self.pokemonList[self.totalPokemonCount] = newPokemon
    self.totalPokemonCount += 1

    log NewPokemonCreated(_name, randomDNA, randomHP)

    return newPokemon
```

## Unit Tests

Update the unit tests as follows:

```python
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
```
## Gas Report

Now, Let's analyze the gas usage of our contract by running the unit tests with a gas report:

```sh
$ brownie test --gas
```
The output will provide detailed information about the gas usage of different contract functions:

```sh
Brownie v1.19.3 - Python development framework for Ethereum

============================================================================ test session starts =============================================================================
platform linux -- Python 3.9.17, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /media/anand/78e9a4f0-d141-4399-abe0-07b9a9f0098c/anand/Workplace/learn-vyper/vyper-pokemon
plugins: eth-brownie-1.19.3, xdist-1.34.0, hypothesis-6.27.3, web3-5.31.3, forked-1.4.0
collected 3 items                                                                                                                                                                    

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/Pokemon_test.py ...                                                                                                                                                      [100%]

================================================================================ Gas Profile =================================================================================

Pokemon <Contract>
   ├─ constructor   -  avg: 269060  avg (confirmed): 269060  low: 269060  high: 269060
   └─ createPokemon -  avg: 132127  avg (confirmed): 132127  low: 132127  high: 132127

============================================================================ 3 passed in 7.30s ============================================================================
Terminating local RPC client...
```

Analyzing the gas report can provide valuable insights into optimizing gas consumption for more complex use cases.

By incorporating events and understanding gas implications, you're now equipped to build more sophisticated and interactive smart contracts with Vyper.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.8.md">Previous: Chapter 9: Public Variables</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.12.md">Next: Chapter 11: Function Modifiers</a>
</div>