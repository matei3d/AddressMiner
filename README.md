# AddressMiner
## Purpose
The goal of this is to provide a small suite of python utilities for interacting with the Ethereum blockchain.

Primarily by giving users the ability to quickly generate Ethereum wallets with the specified public address.

## Usages
### Venv
This suite currently uses venv with the web3.py and eth_account plugins.

To activate: navigate to the project's root and run the venv script at ./venv/Scripts/activate

### wallet_mine.py
```python wallet_mine.py [-h] [-t THREADS] [-n ITERATIONS] target```

Outputs a series of Ethereum private/address keypair.

positional arguments:
  target                wallet address hex value you want from left to right. each digit exponentially more expensive

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        the number of parallel I/O threads to open
  -n ITERATIONS, --iterations ITERATIONS
                        the number of max iterations each thread should go through

### wallet_gen.py
```python wallet_gen.py```

Outputs one random Ethereum private/address keypair.

### simple_transact.py
```python simple_transact.py```