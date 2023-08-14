# Chapter 1: Getting Started with Vyper Contracts

In this chapter, we'll dive into the world of smart contracts with Vyper and learn the basics of writing, compiling, and testing Vyper code. We'll follow the tutorial provided by [learn.vyperlang.org](https://learn.vyperlang.org) to grasp the fundamentals of the Vyper language.

At the moment, the learn.vyperlang.org platform does not have an integrated compiler or testing tool. However, you can use this guide along with our project to seamlessly compile and test the code you learn from the tutorial.

[Tutorial Link](https://learn.vyperlang.org/#/1/contract_structure)

Follow these steps to get started:

## Step 1: Create Your First Contract

Begin by creating a new file named **Pokemon.vy** in the **contracts** folder. Copy and paste the code you've learned from the tutorial into this file.

For example, your **Pokemon.vy** contract might look like:

```python
# @version >=0.2.4 <0.3.0
```

## Step 2: Compile Your Contract

Once you have your contract code ready, it's time to compile it. Open your terminal and navigate to the root folder of your project.

Run the following command to compile your Vyper contract:

```sh
$ brownie compile
```

You'll receive feedback from the compiler about your contract's compilation status.

## Step 3: Understand the Output

The compilation process will generate output similar to the following:


```sh
Brownie v1.19.3 - Python development framework for Ethereum

Compiling contracts...
  Vyper version: 0.2.16
CompilerError: vyper returned the following errors:

start (8,32) precedes previous end (9,0)
```

If you encounter any errors during the compilation process, the output will provide information about the issues. Review your code and the provided error messages to identify and rectify any mistakes.

As you progress through this module, you'll gain proficiency in writing Vyper contracts, compiling them, and understanding any encountered errors. Our project is here to support you on your journey, ensuring a smooth learning experience.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="../README.md">Previous: Vyper Poemon Introduction</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-pokemon/docs/Chapter-1.2.md">Next: Chapter 2: State Variables, Integers & Constants</a>
</div>