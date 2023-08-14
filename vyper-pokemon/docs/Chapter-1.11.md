# Chapter 11: Keccak256 and Typecasting

[Tutorial Link](https://learn.vyperlang.org/#/1/keccak256-and-typecasting)

Welcome to Chapter 11! In this chapter, we will delve into the concepts of Keccak256 and typecasting in the Vyper language. Understanding how to use Keccak256 and how to perform typecasting is essential for various aspects of smart contract development.

## Learning Keccak256 and Typecasting

To begin, follow the comprehensive tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org/#/1/keccak256-and-typecasting). This tutorial will guide you through the process of using Keccak256 for cryptographic hashing and performing typecasting operations in your Vyper smart contracts.

As you progress through the tutorial, you'll gain insights into the practical applications of Keccak256 and typecasting, enhancing your ability to build secure and efficient smart contracts.

After studying the tutorial, apply the concepts learned to your existing `Pokemon.vy` contract by copying and pasting the provided code snippets.

## Running Unit Tests

To ensure that your code is functioning correctly, you can run unit tests using the Brownie testing framework. Use the previously used file named `Pokemon_test.py` in the `tests` folder to check the code is error free

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
collected 1 item                                                                                                                                                                     

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/Pokemon_test.py .                                                                                                                                                        [100%]

============================================================================= 1 passed in 6.18s ==============================================================================
Terminating local RPC client...
```

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-pokemon/docs/Chapter-1.10.md">Previous: Chapter 10: More on Functions</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.12.md">Next: Chapter 12: Putting It Together</a>
</div>