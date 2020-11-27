from collections import OrderedDict
from uuid import uuid4
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from hashlib import sha256
from urllib.parse import urlparse
import json
import time
import binascii
from time import time
from flask import Flask, request, jsonify
from flask_cors import CORS

MINNING_SENDER="BLOCKCHAIN"
MINNING_REWARD=50

class Blockchain:

    def __init__(self):
        self.transactions = [] # kinda the mempool
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
        """
        Add a transaction to the transaction array if it be valid
        :param sender_address: the address (public_key) of sender
        """
        transaction =OrderedDict({
            'sender_address':sender_address,
            'receiver_address':receiver_address,
            'value':value
        })
        #mining reward
        if sender_address== MINNING_SENDER: # MINNING_SENDER is the blockchain it self
            self.transactions.append(transaction)
            return len(self.chain)+1
        #sending to another wallet
        transaction_validity=self.verify_transaction_signature(sender_address,signature,transaction)
        if transaction_validity==True:
            self.transactions.append(transaction)
            return len(self.chain)+1
        else:
            return False


    def create_block(self, nonce, previous_hash=None):
        """

        :param nonce: <int> the nonce found by the Proof of Word algorithm
        :param previous_hash: <str> the hash of the previous block (none for genesis block)
        :return: <dict> the newly created block
        """
        block={
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transactions':self.transactions,
            'nonce':nonce,
            'previous_hash':previous_hash or self.hash_block(self.chain[-1]),
        }
        #clearing the current list of transaction
        self.transactions=[]
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(block):
        """
        :param block: <dict> block
        :return: <str> the SHA-256 hash of block
        """
        block_str=json.dump(block,sort_keys=True).encode()
        return sha256(block_str).hexdigest()

    def proof_of_work(self,difficulty=4):
        """
        proof of work algorithm:
        finds the nonce that expression '{last_nonce}{nonce}' ends in 4 zeroes
        :param last_nonce: <int> the nonce of last block
        :param difficulty" <int> the number of ending zeroes
        :return: <int> newly found nonce
        """
        last_block=self.last_block
        last_nonce=last_block["nonce"]
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
        return expr_hash[:-4]==("0"*difficutly)

    def valid_chain(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def resolve_conflicts(self):
        pass



# blockchain fucking api :)
app=Flask(__name__)
CORS(app)

# the index page

# configure page

# new transaction

# get transactions

#get chain

# mine

#registering node

# resolving conflicts

#getting nodes