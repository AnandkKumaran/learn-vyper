# Chapter 6: Function Declarations

[Tutorial Link](https://learn.vyperlang.org/#/1/function_declarations?id=chapter-6-function-declarations)

Welcome to Chapter 6! In this chapter, we'll dive into the realm of function declarations in the Vyper language. Functions are the building blocks of smart contracts, allowing you to define and execute specific actions within your code.

## Unveiling Function Declarations

To get started, we recommend following the comprehensive tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/function_declarations?id=chapter-6-function-declarations). This tutorial will guide you through the intricacies of function declarations in Vyper, helping you grasp the fundamental concepts of defining and implementing functions.

As you progress through the tutorial, we encourage you to apply your knowledge to your existing `Pokemon.vy` contract. For instance, consider the following example where we introduce a function declaration `createPokemon`:
 

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
    pass # fill in the function body
```

## Compiling and Beyond

With the function declaration in place, it's time to compile your contract:


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

This confirmation assures you that your contract has been successfully compiled, and the build artifacts are ready for further use.

As you delve into this chapter, you'll unravel the significance of function declarations and how they contribute to the functionality of your smart contract. Experiment with defining and implementing functions in your Pokemon.vy contract to reinforce your understanding.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.5.md">Previous: Chapter 5: Mappings</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.7.md">Next: Chapter 7: Working With Structs and Mappings</a>
</div>