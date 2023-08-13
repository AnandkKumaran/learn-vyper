
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

## Key Take aways

... (will add soon)


Continue your exploration of Vyper and smart contract development as we progress through this exciting learning path!

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="/vyper-by-examples/README.md">Previous: Vyper by examples: Introduction</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-by-examples/docs/">Next: Data Types Values</a>
</div>