# Chapter 8: External / Internal Functions

[[Tutorial Link]](https://learn.vyperlang.org/#/1/external_internal_functions)

Welcome to Chapter 8! In this chapter, we'll delve into the concepts of external and internal functions in the Vyper language. Understanding how these functions work and when to use them is crucial for building effective and secure smart contracts.

## Exploring External and Internal Functions

To begin, follow the in-depth tutorial provided by learn.vyperlang.org. This tutorial will guide you through the intricacies of external and internal functions, showcasing their respective roles in smart contract development.

As you progress through the tutorial, we encourage you to integrate the concepts of external and internal functions into your existing Pokemon.vy contract. Here's an example where we define an internal function _createPokemon within our contract:

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

@internal
def _createPokemon(_name: String[32], _dna: uint256, _HP: uint256):
    self.pokemonList[0] = Pokemon({
        name: _name,
        dna: _dna,
        HP: _HP,
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

## Deployment and Invocation

Once you've integrated external and internal functions into your contract, let's proceed with deployment and function invocation.

Deploy your contract to the Ganache network using the Brownie console:

```sh
>>> Pokemon.deploy({"from":accounts[0]})
Transaction sent: 0xb1fa4e7982de70cb1b313cba52178d6ebfdeb43e142b5e97549a30e1139ec1a3
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Pokemon.constructor confirmed   Block: 1   Gas used: 97920 (0.82%)
  Pokemon deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

<Pokemon Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>
```

Now, let's attempt to invoke the _createPokemon internal function. However, note that internal functions cannot be directly invoked externally:

```sh
>>> Pokemon[0]._createPokemon("Bulbasaur",123456789,100)
  File "<console>", line 1, in <module>
  File "brownie/network/contract.py", line 783, in __getattribute__
    raise AttributeError(f"Contract '{self._name}' object has no attribute '{name}'")
AttributeError: Contract 'Pokemon' object has no attribute '_createPokemon'
```

## Understanding Internal Functions

Internal functions, such as _createPokemon, are designed to be accessed and used only within the contract itself. They cannot be invoked externally or by other contracts. This encapsulation helps enhance security and control over contract behavior.

As you continue your exploration of external and internal functions, remember that understanding when and how to use each type is essential for building robust and efficient smart contracts.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.7.md">Previous: Chapter 7: Working With Structs and Mappings</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.9.md">Next: Chapter 9: Public Variables</a>
</div>



