# Chapter 9: Public Variables

[Tutorial Link](https://learn.vyperlang.org/#/1/public_vars)

Welcome to Chapter 9! In this chapter, we will explore the concept of public variables in the Vyper language. Public variables offer a way to expose certain data to the outside world, allowing external contracts and users to access and interact with them. 

## Understanding Public Variables

To get started, follow the comprehensive tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/public_vars). This tutorial will guide you through the fundamentals of public variables and demonstrate how they can be implemented in your smart contracts.

As you progress through the tutorial, we encourage you to integrate the concept of public variables into your existing `Pokemon.vy` contract. Here's an example where we add a public variable `totalPokemonCount` to track the total number of Pokemon created:
 

```python
# @version >=0.2.4 <0.3.0

DNA_DIGITS: constant(uint256) = 16
DNA_MODULUS: constant(uint256) = 10 ** DNA_DIGITS

struct Pokemon:
    name: String[32]
    dna: uint256
    HP: uint256
    matches: uint256
    wins: uint256

totalPokemonCount: public(uint256)
pokemonList: HashMap[uint256, Pokemon]

@internal
def _createPokemon(_name: String[32], _dna: uint256, _HP: uint256):
    self.pokemonList[self.totalPokemonCount] = Pokemon({
        name: _name,
        dna: _dna,
        HP: _HP,
        matches: 0,
        wins: 0
    })
    self.totalPokemonCount += 1
```

## Unit Testing
Unit tests are essential to ensure the correctness of your smart contract. To create a unit test for the totalPokemonCount public variable, follow these steps:

1. Create a file called `Pokemon_test.py` in the `tests` folder.
2. Copy and paste the following code into `Pokemon_test.py`:

```python
import pytest

from brownie import Pokemon, accounts

@pytest.fixture
def pokemon():
    return accounts[0].deploy(Pokemon)

def test_greet(pokemon):    
    assert pokemon.totalPokemonCount() == 0
```

Follow this [documentation](https://eth-brownie.readthedocs.io/en/stable/tests-pytest-intro.html#writing-unit-tests) to learn more about unit testing in brownie.

Run the unit test:

```sh
$ brownie test
```

You should see an output similar to the following:


```sh
Brownie v1.19.3 - Python development framework for Ethereum

============================================================================ test session starts =============================================================================
platform linux -- Python 3.9.17, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /ubuntu/learn-vyper/vyper-pokemon
plugins: eth-brownie-1.19.3, xdist-1.34.0, hypothesis-6.27.3, web3-5.31.3, forked-1.4.0
collected 1 item                                                                                                                                                                     

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/Pokemon_test.py .                                                                                                                                                        [100%]

============================================================================= 1 passed in 6.31s ==============================================================================
Terminating local RPC client...
```

## Summary

Public variables play a crucial role in making specific data accessible to external entities. By following this chapter, you have gained insights into the implementation and testing of public variables in your Vyper smart contracts. Continue exploring and experimenting with public variables to enhance the functionality and usability of your contracts.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.8.md">Previous: Chapter 8: External / Internal Functions</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.10.md">Next: Chapter 10: More on Functions</a>
</div>