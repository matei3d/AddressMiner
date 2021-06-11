'''
Generates a list of wallets according to a specified target string for the first few characters.
'''

from tinydb import TinyDB
from wallet_gen import generateAddress
import timeit
import threading
import argparse

def run(iterations, threadNum, target):
    #db= TinyDB(f'./Data/addresses{threadNum}.json')

    for i in range(iterations):
        eth = generateAddress()
        address = eth['walletAddress']

        if address[:(len(target))] == target:
            print(f"{{{eth['walletAddress']},{eth['privateKey']}}}", flush=True)

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("target", type=str, nargs='?', default="0x",
help="wallet address hex value you want from left to right. each digit exponentially more expensive")
parser.add_argument("-t", "--threads", type=int,
help="the number of parallel I/O threads to open")
parser.add_argument("-n", "--iterations", type=int,
help="the number of max iterations each thread should go through")
args = parser.parse_args()

# Calculate instancing numbers
num_threads = 1
if args.threads is not None:
    num_threads = args.threads
#print(num_threads)

#iterations = 22**(len(args.target)-2) + 22 #22 cause the hex chars are case sensitive (a != A)
iterations = 10     # 10 loops per thread by default
if args.iterations is not None:
    iterations = args.iterations
#print(iterations)

# Initialize Program
print ('WalletAddress,PrivateKey')
for i in range(num_threads):
    t = threading.Thread(target=run, args=(iterations, i, args.target))
    t.daemon = True
    t.run()