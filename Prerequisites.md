# Prerequisites

Before you embark on your journey to master Vyper and smart contract development, make sure you have the following tools and software installed on your system:




3. **Brownie Framework (Optional, but Recommended)**: While not mandatory, the Brownie framework offers an excellent environment for smart contract development, testing, and deployment. To install Brownie, you can use:




## Python

Vyper is closely related to Python, so having Python installed is essential. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

Having Python 3.9 installed on your system is recommended for setting up eth-brownie. Python 3.10 and 3.11 may present some dependency challenges, making Python 3.9 a more preferable choice.

```sh
sudo apt install python3.9 -y
```


Please make sure to install the necessary dependencies:

```sh
sudo apt install python3.9-distutils python3.9-dev python3.9-venv
```


## Vyper

The Vyper compiler is required to translate your Vyper smart contracts into bytecode that can be executed on the Ethereum Virtual Machine (EVM). You can install Vyper using pip:

```sh
pip install vyper
```

OR

```sh
python3.9 -m pip install vyper
```

To ensure a smooth setup process, please follow the instructions provided in the official Vyper installation guide. [docs.vyperlang.org](https://docs.vyperlang.org/en/stable/installing-vyper.html#id1)

## Brownie Framework

The Brownie framework presents an exceptional environment tailored for smart contract development, testing, and deployment. To integrate Brownie into your setup, follow these steps:

1. **Install pipx:**

Start by installing pipx, a tool that provides a way to install and run Python applications in isolated environments. Open your terminal and execute the following commands:

```sh
python3.9 -m pip install pipx
python3.9 -m pipx ensurepath
```

If everything is in order, you should see output similar to this:

```sh
ubuntu@ubuntu:~$ python3.9 -m pipx ensurepath
/home/ubuntu/.local/bin is already in PATH.

⚠️  All pipx binary directories have been added to PATH. If you are sure you want to proceed, try again with the '--force' flag.

Otherwise pipx is ready to go! ✨ 🌟 ✨

```

2. **Install Brownie:**

Now, install Brownie using pipx with the following command:

```sh
pipx install eth-brownie
```

Upon successful installation, you'll receive an output similar to:


```sh
ubuntu@ubuntu:~$ pipx install eth-brownie
  installed package eth-brownie 1.19.3, installed using Python 3.9.17
  These apps are now globally available
    - brownie
done! ✨ 🌟 ✨

```

For comprehensive instructions and more details, refer to the official Brownie installation [documentation](https://eth-brownie.readthedocs.io/en/stable/install.html).

To enable the Brownie console, you'll need to have ganache-cli installed. If it's not already installed, you can use the following command:

```sh
sudo npm install -g ganache-cli
```

## Finished

Congratulations! You've completed the prerequisites and are now ready to embark on your exciting journey through the Vyper Learning Path.

Please follow the [Next button](#) to start the course.

<div style="display: flex; justify-content: space-between;">
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: left;" href="README.md">Previous: Introduction</a>
    <a style="text-decoration: none; padding: 5px 10px; border: 1px solid #ccc; border-radius: 5px; float: right;" href="/vyper-by-examples/README.md">Next: Vyper by examples</a>
</div>