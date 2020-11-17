import binascii
from Crypto.PublicKey import RSA
from Crypto import Random
class Wallet:
    """
    wallet is actually a public and private key pair
    """
    def __init__(self):
        random_seed=Random.new().read
        self._private_key=RSA.generate(1024,random_seed)
        self._public_key=self._private_key.publickey()
    @property
    def address(self):
        '''

        :return:  the public key as the address of wallet
        '''
        return binascii.unhexlify(self._public_key.export_key(format="DER")).decode('ascii')
