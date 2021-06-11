# AddressMiner
## Purpose
The goal of this is to provide a small suite of python utilities for interacting with the Ethereum blockchain.

Primarily by giving users the ability to quickly generate Ethereum wallets with the specified public address.

## Usages
### Venv
This suite currently uses venv with the web3.py and eth_account plugins.

To activate: navigate to the project's root and run the venv script at ```./venv/Scripts/activate```

### wallet_mine.py
```python wallet_mine.py [-h] [-t THREADS (default 1)] [-n ITERATIONS (default 10)] target```

Outputs a series of Ethereum private/address keypair.

Results can be piped or routed to a file, 

eg: ```python wallet_mine.py -n 100 "0xABC" > ./Data/ABCwallets.txt```
will generate wallets starting with "0xABC" that you can read in the ABCwallets.txt file.

--help: 
```
positional arguments:
  target                wallet address hex value you want from left to right. each digit exponentially more expensive

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        the number of parallel I/O threads to open
  -n ITERATIONS, --iterations ITERATIONS
                        the number of max iterations each thread should go through
```

### wallet_gen.py
```python wallet_gen.py```

Outputs one random Ethereum private/address keypair.

### simple_transact.py
```python simple_transact.py```

Simple transact currently has everything done from variables in the script. Will be adding arguments soon.

For the time being, please fill in the following fields.

With an RPC key taken from your own private node or from your infura account:
```rpc_url = "https://ropsten.infura.io/v3/<your_infura_API_Key>"```

With a private key / public address pair of a valid Ethereum wallet:
```
private_key_from = "0xPRIVATE_key_Example"
public_key_from = "0xPUBLIC_key_example
```

#### The best is yet to come.