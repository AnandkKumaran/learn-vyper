# Chapter 5: Mappings

[Tutorial Link](https://learn.vyperlang.org/#/1/mappings)

Welcome to Chapter 5! In this chapter, we'll delve into the powerful concept of mappings in the Vyper language. Mappings provide an efficient way to associate and store key-value pairs within your smart contracts.

## Unraveling Mappings

Begin your exploration by following the comprehensive tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/mappings). This tutorial will guide you through the intricacies of working with mappings in Vyper, enhancing your contract's capabilities to store and retrieve data.

As you progress through the tutorial, we encourage you to integrate your newfound knowledge into your existing `Pokemon.vy` contract. For instance, consider the following example where we introduce a `pokemonList` mapping:


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
```
## Compiling and Beyond

With the mapping concept integrated into your contract, let's proceed to compile it:


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

As you immerse yourself in this chapter, you'll uncover the versatility and efficiency of mappings in Vyper. These data structures open up new possibilities for data storage and retrieval within your smart contracts. Apply your insights to your Pokemon.vy contract and experiment with various mapping interactions.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.4.md">Previous: Chapter 4: Structs</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.6.md">Next: Chapter 6: Function Declarations</a>
</div>