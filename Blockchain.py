from uuid import uuid4
from Crypto.Hash import SHA256
from hashlib import sha256
from urllib.parse import urlparse
import json
import time

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
        pass

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

    def proof_of_work(self,last_nonce):
        """
        proof of work algorithm:
        finds the nonce that expression '{last_nonce}{nonce}' ends in 4 zeroes
        :param last_nonce: <int> the nonce of last block
        :return: <int> newly found nonce
        """
        nonce=0
        while self.validate_nonce(last_nonce,nonce) is False:
            nonce +=1

        return nonce
    @staticmethod
    def validate_nonce(last_nonce,nonce):
        """
        checks if hash(last_nonce,nonce) contains 4 ending zeroes ?

        :param last_nonce: <int> previous nonce
        :param nonce:  <int> current testing nonce
        :return:  <bool> true if condition is true

        """
        expr=f'{last_nonce}{nonce}'.encode()
        expr_hash=sha256(expr).hexdigest()
        return expr_hash[:-4]=="0000"

    def valid_chain(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def resolve_conflicts(self):
        pass
