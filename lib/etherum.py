from web3 import Web3
from web3.exceptions import InvalidAddress
from lib.exceptions import ConnectionException, InvalidWalletAddress
from dotenv import load_dotenv

import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + os.getenv("PROJECT_ID")))

def get_wallet(address):
    if not w3.is_connected():
        raise ConnectionException("Not connected")

    try:
        wallet = {}
        wallet["status"] = "success"
        wallet["address"] = address
        
        balance = w3.eth.get_balance(address)
        wallet["balance"] = w3.from_wei(balance, 'ether')

        return wallet
    except InvalidAddress:
        raise InvalidWalletAddress


# EOF