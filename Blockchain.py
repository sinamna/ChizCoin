from uuid import uuid4
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from hashlib import sha256
from urllib.parse import urlparse
import json
import time
import binascii

class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        self.node_id = str(uuid4()).replace('-', ' ')

        #creating genesis block

    def register_node(self, node_url):
        """
        adds new node to list of nodes
        """
        parse_url=urlparse(node_url)
        if parse_url.netloc :
            self.nodes.add(parse_url.netloc)
        elif parse_url.path:
            self.nodes.add(parse_url.path)
        else:
            raise ValueError('invalid URL')

    def verify_transaction_signature(self, sender_address, signature, transaction):
        """
        checks the signature of transaction is signed by the public key
        :param sender_address: the public key
        """
        public_key=RSA.import_key(binascii.unhexlify(sender_address))
        verifier=PKCS1_v1_5.new(public_key)
        hashed_trx=SHA256.new(str(transaction).encode('utf8'))
        return verifier.verify(hashed_trx,binascii.unhexlify(signature))

    def submit_transaction(self, sender_address, receiver_address, value, signature):
        pass

    def create_block(self, nonce, previous_hash=None):
        """

        :param nonce: <int> the nonce found by the Proof of Word algorithm
        :param previous_hash: <str> the hash of the previous block (none for genesis block)
        :return: <dict> the newly created block
        """
        pass

    @staticmethod
    def hash_block(block):
        """
        :param block: <dict> block
        :return: <str> the SHA-256 hash of block
        """
        block_str=json.dump(block,sort_keys=True).encode()
        return sha256(block_str).hexdigest()

    def proof_of_work(self,last_nonce,difficulty=4):
        """
        proof of work algorithm:
        finds the nonce that expression '{last_nonce}{nonce}' ends in 4 zeroes
        :param last_nonce: <int> the nonce of last block
        :param difficulty" <int> the numb of ending zeroes
        :return: <int> newly found nonce
        """
        nonce=0
        while self.validate_nonce(last_nonce,nonce,difficulty) is False:
            nonce +=1

        return nonce
    @staticmethod
    def validate_nonce(last_nonce,nonce,difficutly):
        """
        checks if hash(last_nonce,nonce) contains ending zeroes as many as difficulty ?

        :param last_nonce: <int> previous nonce
        :param nonce:  <int> current testing nonce
        :return:  <bool> true if condition is true

        """
        expr=f'{last_nonce}{nonce}'.encode()
        expr_hash=sha256(expr).hexdigest()
        return expr_hash[:-4]=="0"*difficutly

    def valid_chain(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def resolve_conflicts(self):
        pass
