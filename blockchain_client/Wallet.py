import binascii
from Crypto.PublicKey import RSA
from Crypto import Random
class Wallet:
    """
    wallet is actually a public and private key pair
    """
    def __init__(self):
        random_seed=Random.new().read
        self._private_key=RSA.generate(2048,random_seed)
        self._public_key=self._private_key.publickey()
    @property
    def address(self):
        '''
        :return:  the public key as the address of wallet
        '''
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
        
    def to_dict(self):
        '''
        :return: dictionary representing the wallet
        '''
        return {
            'private_key':binascii.hexlify(self._private_key.export_key(format='DER')).decode('ascii'),
            'public_key':binascii.hexlify(self._public_key.export_key(format='DER')).decode('ascii')
        }

