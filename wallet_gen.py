from eth_account import Account

extra_entropy = '1337'

def generateAddress():
    act = Account.create(extra_entropy)
    private_key = act.privateKey.hex()
    return {'walletAddress': act.address, 'privateKey': private_key,}

if __name__ == '__main__':
    print(generateAddress())