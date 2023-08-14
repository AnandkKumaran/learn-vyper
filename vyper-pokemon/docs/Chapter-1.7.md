# Chapter 7: Working With Structs and Mappings

[Tutorial Link](https://learn.vyperlang.org/#/1/working_with_structs)

Welcome to Chapter 7! In this chapter, we will dive deeper into working with structs and mappings in the Vyper language. By understanding how these powerful data structures interact, you'll gain the ability to create more sophisticated and dynamic smart contracts.

## Exploring Structs and Mappings Interaction

To begin, follow the detailed tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/working_with_structs). This tutorial will guide you through the process of working with structs and mappings together, demonstrating their synergistic capabilities in your smart contract design.

As you progress through the tutorial, we encourage you to apply your newfound knowledge to your existing `Pokemon.vy` contract. Here's an example where we combine the `Pokemon` struct with a mapping to create a `createPokemon` function:


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

pokemonList: HashMap[uint256, Pokemon]

@external
def createPokemon(name: String[32], dna: uint256, HP: uint256):
    self.pokemonList[0] = Pokemon({
        name: name,
        dna: dna,
        HP: HP,
        matches: 0,
        wins: 0
    })
```

## Compiling

Once you've integrated the struct-mapping interaction into your contract, let's compile, deploy, and invoke the functions: 

```sh
$ brownie compile
```

The compilation process will generate output similar to the following:

```sh
Brownie v1.19.3 - Python development framework for Ethereum

Compiling contracts...
  Vyper version: 0.2.16
Generating build data...
 - Pokemon

Project has been compiled. Build artifacts saved at /ubuntu/learn-vyper/vyper-pokemon/build/contracts
```

## Deploying and Invoking

Lets Deploy your contract to the Ganache network using the Brownie console:

```sh
>>> Pokemon.deploy({"from":accounts[0]})
Transaction sent: 0xb1fa4e7982de70cb1b313cba52178d6ebfdeb43e142b5e97549a30e1139ec1a3
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Pokemon.constructor confirmed   Block: 1   Gas used: 97920 (0.82%)
  Pokemon deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

<Pokemon Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>
>>>
```

Once deployed, you can invoke the createPokemon function:

```sh
>>> Pokemon[0].createPokemon("Bulbasaur",123456789,100)
Transaction sent: 0xe9f2e3982d6032b09751b16f9e770628d8704930664c1a44b69248e710a82154
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 2
  Pokemon.createPokemon confirmed   Block: 3   Gas used: 39887 (0.33%)

<Transaction '0xe9f2e3982d6032b09751b16f9e770628d8704930664c1a44b69248e710a82154'>
>>>
```

This hands-on experience will solidify your understanding of how structs and mappings interact within your Vyper smart contract. Feel free to experiment and explore different variations of these interactions to enhance your contract's functionality.

Follow this [documentation](https://eth-brownie.readthedocs.io/en/stable/core-contracts.html#working-with-contracts) to get more details about Contract interactions

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.6.md">Previous: Chapter 6: Function Declarations</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.8.md">Next: Chapter 8: External / Internal Functions</a>
</div>