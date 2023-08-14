# Learn Vyper by building a Pokémon Game!

Welcome, learners! This module is designed to help you dive into Vyper contracts through the chapters presented in [Vyper Tutorials](https://learn.vyperlang.org/). 

Please explore the following resources:

1. [Vyper by Example](https://vyper-by-example.org/)
2. [Video Tutorials](https://www.youtube.com/watch?v=-kZpEmNnzyE&list=PLO5VPQH6OWdWOd-IJTfIzlM2a1yv1rSN-)

## Create Your Project Folder

Let's start by setting up your project folder:

```sh
$ mkdir vyper-pokemon
$ cd vyper-pokemon
```

And, Initialize a Brownie project:

```sh
$ brownie init
```

You'll see an output similar to:

```sh
Brownie v1.19.3 - Python development framework for Ethereum

SUCCESS: A new Brownie project has been initialized at /ubuntu/learn-vyper/vyper-pokemon
```
Follow this [link](https://eth-brownie.readthedocs.io/en/stable/structure.html#structure-of-a-project) to get more details about project structure

## Warm up

Let's get comfortable with Brownie!

Please use the following command to get into brownie console  

```sh
$ brownie console
```

You'll see an output similar to:

```sh
Brownie v1.19.3 - Python development framework for Ethereum

VyperByExamplesProject is the active project.

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...
Brownie environment is ready.
>>>
```

Feel free to experiment with the following commands in the Brownie console:


```sh
>>> accounts
[<Account '0x66aB6D9362d4F35596279692F0251Db635165871'>, <Account '0x33A4622B82D4c04a53e170c638B944ce27cffce3'>, <Account '0x0063046686E46Dc6F15918b61AE2B121458534a5'>, <Account '0x21b42413bA931038f35e7A5224FaDb065d297Ba3'>, <Account '0x46C0a5326E643E4f71D3149d50B48216e174Ae84'>, <Account '0x807c47A89F720fe4Ee9b8343c286Fc886f43191b'>, <Account '0x844ec86426F076647A5362706a04570A5965473B'>, <Account '0x23BB2Bb6c340D4C91cAa478EdF6593fC5c4a6d4B'>, <Account '0xA868bC7c1AF08B8831795FAC946025557369F69C'>, <Account '0x1CEE82EEd89Bd5Be5bf2507a92a755dcF1D8e8dc'>]

>>> accounts[0]
<Account '0x66aB6D9362d4F35596279692F0251Db635165871'>

>>> accounts[0].balance()
100000000000000000000

>>> 
```

To exit the Brownie console, use the following command or Ctrl-D (EOF):


```sh
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
Terminating local RPC client...
```

You're now ready to start exploring Vyper and its applications in smart contract development. Let's dive in!


<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="../Prerequisites.md">Previous: Prerequisites</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.1.md">Next: Chapter 1: Contracts</a>
</div>




