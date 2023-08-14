# Chapter 3: Math Operations

[Tutorial Link](https://learn.vyperlang.org/#/1/math_operations)

Welcome to Chapter 3! In this chapter, we'll dive into the fascinating world of math operations in the Vyper language. Understanding how to perform various mathematical computations is essential for creating powerful and versatile smart contracts.

## Math Operations in Vyper

To get started, we encourage you to follow the in-depth tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/math_operations). This tutorial will guide you through essential math operations in Vyper, helping you build a strong foundation in numerical computations.

As you work through the tutorial, we invite you to enhance your learning experience by incorporating the concepts into your existing `Pokemon.vy` contract. Let's consider an example where you define `DNA_DIGITS` and `DNA_MODULUS` constants in your contract:

```python
# @version >=0.2.4 <0.3.0

DNA_DIGITS: constant(uint256) = 16
DNA_MODULUS: constant(uint256) = 10 ** DNA_DIGITS
```
## Compiling and Beyond

Once you've incorporated the math operations into your contract, it's time to compile your updated Pokemon.vy contract. Here's how you can do it:

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

This output confirms that your contract has been successfully compiled, and the build artifacts are ready for use.

As you immerse yourself in this chapter, you'll unlock the potential of math operations in Vyper and understand their significance in creating sophisticated smart contracts. Apply your knowledge to your Pokemon.vy contract and experiment with different mathematical computations.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.2.md">Previous: Chapter 2: State Variables, Integers & Constants</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.4.md">Next: Chapter 4: Structs</a>
</div>