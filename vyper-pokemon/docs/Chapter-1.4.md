# Chapter 4: Structs

[Tutorial Link](https://learn.vyperlang.org/#/1/structs)

Welcome to Chapter 4! In this chapter, we'll explore the concept of structs in the Vyper language. Structs provide a powerful way to organize and manage data within your smart contracts.

## Understanding Structs

To begin, we recommend following the comprehensive tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/structs). This tutorial will guide you through the ins and outs of working with structs in Vyper, helping you enhance your contract's data organization and readability.

As you progress through the tutorial, we encourage you to integrate your newfound knowledge into your `Pokemon.vy` contract. For instance, consider the following example where we define a `Pokemon` struct:


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
```

## Compiling and Beyond

Once you've integrated the struct into your contract, let's compile it to ensure everything is in order:

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

This confirmation indicates that your contract has been successfully compiled, and the build artifacts are ready for use.

As you dive into this chapter, you'll uncover the versatility of structs in Vyper and their importance in organizing complex data structures. Apply your understanding to your Pokemon.vy contract and experiment with different struct definitions.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.3.md">Previous: Chapter 3: Math Operations</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.5.md">Next: Chapter 5: Mappings</a>
</div>