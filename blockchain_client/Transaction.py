import binascii
from collections import OrderedDict
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
class Transaction:
    def __init__(self, sender_address, sender_private_key, receiver_address, value):
        self.sender_address = sender_address
        self._sender_private_key = sender_private_key
        self.receiver_address = receiver_address
        self.value = value

    def to_dict(self):
        '''
        return: a dictionary representing transaction
        '''
        return OrderedDict ({
            'sender_address': self.sender_address,
            'receiver_address': self.receiver_address,
            'amount': self.value
        })

    def sign_transaction(self):
        '''
        sign transaction with private key
        '''
        private_key = RSA.import_key(binascii.unhexlify(self._sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        hashed_Trx = SHA256.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(hashed_Trx)).decode('ascii')
