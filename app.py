from flask import Flask, request, jsonify

from lib.crypto import Ethereum, Bitcoin
from lib.exceptions import ConnectionException, InvalidWalletAddress
from lib.error import error_out

app = Flask(__name__)

@app.get("/health")
def health():
    status = {"status":"alive"}
    return jsonify(status)

@app.get("/wallet/eth/<address>")
def get_eth_wallet_details(address):
        try:
            ethereum = Ethereum(address)
            return jsonify(ethereum.get_wallet())
        except ConnectionException:
             return error_out("Error connecting to blockchain", 500)
        except InvalidWalletAddress:
             return error_out("Invalid wallet address", 400)
        except Exception:
             return error_out("Unexpected error", 500)

@app.get("/wallet/bitcoin/<address>")
def get_bitcoin_wallet_details(address):
        try:
            bitcoin = Bitcoin(address)
            return jsonify(bitcoin.get_wallet())
        except ConnectionException:
             return error_out("Error connecting to blockchain", 500)
        except InvalidWalletAddress:
             return error_out("Invalid wallet address", 400)
        except Exception:
             return error_out("Unexpected error", 500)

if __name__ == "__main__":
    app.run(debug=True)

# EOF