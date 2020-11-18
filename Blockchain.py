from uuid import uuid4
from Crypto.Hash import SHA256
from hashlib import sha256
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
        pass

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
    def hash(block):
        """
        :param block: <dict> block
        :return: <str> the SHA-256 hash of block
        """
        block_str=json.dump(block,sort_keys=True).encode()
        return sha256(block_str).hexdigest()

    def proof_of_work(self):
        pass

    def valid_chain(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def resolve_conflicts(self):
        pass
