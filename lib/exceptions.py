class ConnectionException(Exception):
    """
    Raised when there is any connection error with blockchain.
    """
    
    pass

class InvalidWalletAddress(Exception):
    """
    Raised when the wallet address supplied is not valid.
    """
    
    pass