
# Chapter 1: Hello World!

Welcome to the First Chapter, dear learners! In this chapter, we're taking our first steps in Vyper by crafting a simple smart contract. We'll be delving into the world of Vyper programming by exploring the classic "Hello World" program.

Let's start by examining the core components of our initial endeavor:

## Tutorials

1. [Hello World](https://vyper-by-example.org/hello-world/) 
2. [Video](https://youtu.be/-kZpEmNnzyE)

## The Code

Begin by creating a file named **HelloWorld.vy** in the **contracts** folder, then paste the following code:

```python
# @version ^0.3.0

# Create a string variable that can store maximum 100 characters
greet: public(String[100])

@external
def __init__():
    self.greet = "Hello World"
```

## Exploring the Code

... (will add soon)


## Running the Code


### Compile

Start by compiling the contract:


```sh
$ brownie compile contracts/HelloWorld.vy
```

You should see output similar to:


```sh
Brownie v1.19.3 - Python development framework for Ethereum

Project has been compiled. Build artifacts saved at /learn-vyper/vyper-by-examples/build/contracts
```

### Deployment and Interaction

To deploy and interact with the HelloWorld contract, open the Brownie console:

```sh
$ brownie console
```

Deploy the HelloWorld Contract:


```sh
>>> HelloWorld.deploy({"from": accounts[0]})
Transaction sent: 0x45d5d5993e0e3cfe61b16bc257e7d3dbc7f891fa5e6326f998376143cd04197c
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  HelloWorld.constructor confirmed   Block: 1   Gas used: 133278 (1.11%)
  HelloWorld deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

<HelloWorld Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>
```

Invoke the greet() function:

```sh
>>> HelloWorld[0].greet()
'Hello World'
```

## Uint Testing

When it comes to software development, unit testing plays a crucial role in ensuring the reliability and correctness of your code. In the context of smart contract development, unit testing is equally essential to verify the behavior of your smart contracts and catch potential issues early in the development process.

Unit testing not only helps validate the functionality of your code but also aids in achieving a high level of code coverage. Code coverage measures how much of your code is executed during tests, indicating the thoroughness of your testing strategy. Additionally, monitoring gas usage is vital for optimizing smart contract deployments. Gas reports provide insights into the gas consumption of your contract, helping you identify gas-intensive operations and optimize your code for better performance.

For a more comprehensive understanding of unit tests in Brownie, refer to the [official documentation](https://eth-brownie.readthedocs.io/en/stable/tests-pytest-intro.html#writing-unit-tests).

Let's dive into writing unit tests for the `HelloWorld` contract:

1. Create a file named `HelloWorld_test.py` in the `tests` folder.

2. Copy and paste the following script into `HelloWorld_test.py`:

```python
import pytest

from brownie import HelloWorld, accounts

@pytest.fixture
def helloWorld():
    return accounts[0].deploy(HelloWorld)

def test_greet(helloWorld):    
    assert helloWorld.greet() == "Hello World"
```

Run unit tests:

```sh
$ brownie test tests/HelloWorld_test.py 
```

You should see output similar to:

```sh
Brownie v1.19.3 - Python development framework for Ethereum

================================================================================ test session starts =================================================================================
platform linux -- Python 3.9.17, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /ubuntu/learn-vyper/vyper-by-examples
plugins: eth-brownie-1.19.3, xdist-1.34.0, hypothesis-6.27.3, web3-5.31.3, forked-1.4.0
collected 1 item                                                                                                                                                                     

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/HelloWorld_test.py .                                                                                                                                                     [100%]

================================================================================= 1 passed in 6.51s ==================================================================================
Terminating local RPC client...
```

To generate a gas report:

```sh
brownie test tests/HelloWorld_test.py --gas
```

You should see output similar to:


```sh
Brownie v1.19.3 - Python development framework for Ethereum

================================================================================ test session starts =================================================================================
platform linux -- Python 3.9.17, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /ubuntu/learn-vyper/vyper-by-examples
plugins: eth-brownie-1.19.3, xdist-1.34.0, hypothesis-6.27.3, web3-5.31.3, forked-1.4.0
collected 1 item                                                                                                                                                                     

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

tests/HelloWorld_test.py .                                                                                                                                                     [100%]
==================================================================================== Gas Profile =====================================================================================


HelloWorld <Contract>
   └─ constructor -  avg: 133278  avg (confirmed): 133278  low: 133278  high: 133278

================================================================================= 1 passed in 6.90s ==================================================================================
Terminating local RPC client...
```
Unit testing and gas optimization are integral to creating robust and cost-effective smart contracts. As you proceed in your Vyper learning journey, remember to incorporate these practices into your development process.


## Key Take aways

... (will add soon)


Continue your exploration of Vyper and smart contract development as we progress through this exciting learning path!

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-by-examples/README.md">Previous: Vyper by examples: Introduction</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-by-examples/docs/">Next: Data Types Values</a>
</div>