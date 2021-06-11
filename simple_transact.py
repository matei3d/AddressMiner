from web3 import Web3
import math

# Initialize Connection to Blockchain
rpc_url = "https://ropsten.infura.io/v3/07bcd7ea355f472ab79d13d551c18a05"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Keys
private_key_from = "PRIVATE_KEY_EXAMPLE"
public_key_from = "PUBLIC_KEY_EXAMPLE"
public_key_to = "0xBA5ED8d01BBD17CF895dd077C66a352308b036c0"

# Build Account and Relevant Values
account = public_key_from
balance = web3.eth.getBalance(account)
nonce = web3.eth.getTransactionCount(account)

# How much we sending
# send_value = math.trunc(balance/2)
gas_estimate = web3.eth.estimateGas({'to': public_key_to, 'from': account, 'value': balance})
send_value = balance - gas_estimate * web3.eth.gasPrice - 1

# Print Information
print("Connected: " + str(web3.isConnected()))
print("Block #: " + str(web3.eth.blockNumber))
print("Gas Price: " + str(web3.eth.gasPrice))
print("Gas Estimate: " + str(gas_estimate))
print("Gas COST: " + str(gas_estimate * web3.eth.gasPrice))
print("Account Balance: " + str(balance))

# Get Smart Contract ABI

# Build and Sign Transaction
txn = {
    'nonce': nonce,
    'to': public_key_to,
    'value': send_value,
    'gasPrice': web3.eth.gasPrice,
    'gas': gas_estimate,
    'data': {
        # Interactions with the erc20 smart contract
    }
}

print(txn)

signed_txn = web3.eth.account.signTransaction(txn, private_key_from)

# Send Signed Transaction
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(web3.toHex(tx_hash))