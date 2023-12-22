from web3 import Web3
from web3.exceptions import InvalidAddress
from lib.exceptions import ConnectionException, InvalidWalletAddress
from dotenv import load_dotenv

import os

load_dotenv()

class Ethereum:
    """
    Represents an ethereum entry.
    """

    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + os.getenv("PROJECT_ID")))

    def __init__(self, address):
        self.address=address
    
    def get_wallet(self):
        if not self.w3.is_connected():
            raise ConnectionException("Not connected")

        try:
            wallet = {}
            wallet["status"] = "success"
            wallet["address"] = self.address
            
            balance = self.w3.eth.get_balance(self.address)
            wallet["balance"] = self.w3.from_wei(balance, 'ether')

            return wallet
        except InvalidAddress:
            raise InvalidWalletAddress

class Bitcoin:
    """
    Represents a bitcoin entry.
    """

    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + os.getenv("PROJECT_ID")))

    def __init__(self, address):
        self.address=address
    
    def get_wallet(self):
        if not self.w3.is_connected():
            raise ConnectionException("Not connected")

        try:
            wallet = {}
            wallet["status"] = "success"
            wallet["address"] = self.address
            
            balance = self.w3.eth.get_balance(self.address)
            wallet["balance"] = self.w3.from_wei(balance, 'ether')

            return wallet
        except InvalidAddress:
            raise InvalidWalletAddress

# EOF