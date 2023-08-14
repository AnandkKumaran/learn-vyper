# Chapter 2: State Variables, Integers & Constants

Welcome to Chapter 2! In this chapter, we'll delve into state variables, integers, and constants in the Vyper language. These concepts are essential building blocks for creating robust and efficient smart contracts.

[Tutorial Link](https://learn.vyperlang.org/#/1/state_vars_and_ints)

## State Variables, Integers & Constants

To get started, we recommend following the detailed tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/state_vars_and_ints). This tutorial will help you grasp the concepts of state variables, integers, and constants in Vyper.

Once you've gone through the tutorial, apply your code by updating the `Pokemon.vy` contract in the `contracts` folder of your project. Incorporate the code snippets you've learned into your contract to reinforce your understanding.

For example, define a constant `DNA_DIGITS` in your contract:

```python
# @version >=0.2.4 <0.3.0

DNA_DIGITS: constant(uint256) = 16
```

## Compiling Your Contract

After updating your Pokemon.vy contract, it's time to compile it and ensure your changes are error-free. 

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

This output indicates that your contract has been successfully compiled, and the build artifacts have been saved for future use.

As you progress through this chapter, you'll become more comfortable with state variables, integers, and constants in Vyper. Feel free to experiment with your Pokemon.vy contract and apply the concepts you've learned from the tutorial.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.1.md">Previous: Chapter 1: Getting Started with Vyper Contracts</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.3.md">Next: Chapter 3: Math Operations</a>
</div>