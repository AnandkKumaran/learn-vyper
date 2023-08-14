# Chapter 12: Putting It Together

[Tutorial Link](https://learn.vyperlang.org/#/1/putting_it_together)

Welcome to Chapter 12! In this final chapter, we will bring together the concepts we've learned throughout this tutorial series to create a complete and functional smart contract using the Vyper language. We will combine various elements such as structs, mappings, functions, Keccak256, and more to create a practical example of a Pokemon-related smart contract.

## Creating a Complete Smart Contract

To begin, follow the step-by-step tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/putting_it_together). This tutorial will guide you through creating a complete smart contract that leverages the concepts we've covered so far.

In this example, we will focus on a `Pokemon` contract that allows users to create Pokemon creatures with randomly generated DNA and hit points (HP). We'll use external and internal functions, Keccak256 for generating randomness, and typecasting to achieve our goals.

As you follow the tutorial, make sure to copy and paste the provided code snippets into your existing `Pokemon.vy` contract. Additionally, there's an adjustment in the `createPokemon()` function to make it external for testing purposes:


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

    return newPokemon
```
## Unit Tests

Update the unit test as follows

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
```

Run the unit tests using the following command:

```sh
$ brownie test
```
The output will provide information about the test execution and whether the tests passed successfully.

```sh
Brownie v1.19.3 - Python development framework for Ethereum

Compiling contracts...
  Vyper version: 0.2.16
Generating build data...
 - Pokemon

============================================================================ test session starts =============================================================================
platform linux -- Python 3.9.17, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /media/anand/78e9a4f0-d141-4399-abe0-07b9a9f0098c/anand/Workplace/learn-vyper/vyper-pokemon
plugins: eth-brownie-1.19.3, xdist-1.34.0, hypothesis-6.27.3, web3-5.31.3, forked-1.4.0
collected 2 items                                                                                                                                                                    

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/Pokemon_test.py ..                                                                                                                                                       [100%]

============================================================================= 2 passed in 6.91s ==============================================================================
Terminating local RPC client...
```

By completing this tutorial, you will have gained a solid understanding of Vyper and smart contract development concepts. You can use this knowledge as a foundation for creating more advanced and sophisticated smart contracts in the future.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.11.md">Previous: Chapter 11: Keccak256 and Typecasting</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.13.md">Next: Chapter 13: Events</a>
</div>