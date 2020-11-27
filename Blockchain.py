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

MINNING_SENDER = "BLOCKCHAIN"
MINNING_REWARD = 50


class Blockchain:

    def __init__(self):
        self.transactions = []  # kinda the mempool
        self.chain = []
        self.nodes = set()
        self.node_id = str(uuid4()).replace('-', ' ')

        # creating genesis block

    def register_node(self, node_url):
        """
        adds new node to list of nodes
        """
        parse_url = urlparse(node_url)
        if parse_url.netloc:
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
        public_key = RSA.import_key(binascii.unhexlify(sender_address))
        verifier = PKCS1_v1_5.new(public_key)
        hashed_trx = SHA256.new(str(transaction).encode('utf8'))
        return verifier.verify(hashed_trx, binascii.unhexlify(signature))

    def submit_transaction(self, sender_address, receiver_address, value, signature):
        """
        Add a transaction to the transaction array if it be valid
        :param sender_address: the address (public_key) of sender
        """
        transaction = OrderedDict({
            'sender_address': sender_address,
            'receiver_address': receiver_address,
            'value': value
        })
        # mining reward
        if sender_address == MINNING_SENDER:  # MINNING_SENDER is the blockchain it self
            self.transactions.append(transaction)
            return len(self.chain) + 1
        # sending to another wallet
        transaction_validity = self.verify_transaction_signature(sender_address, signature, transaction)
        if transaction_validity == True:
            self.transactions.append(transaction)
            return len(self.chain) + 1
        else:
            return False

    def create_block(self, nonce, previous_hash=None):
        """

        :param nonce: <int> the nonce found by the Proof of Word algorithm
        :param previous_hash: <str> the hash of the previous block (none for genesis block)
        :return: <dict> the newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash_block(self.chain[-1]),
        }
        # clearing the current list of transaction
        self.transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(block):
        """
        :param block: <dict> block
        :return: <str> the SHA-256 hash of block
        """
        block_str = json.dump(block, sort_keys=True).encode()
        return sha256(block_str).hexdigest()

    def proof_of_work(self, difficulty=4):
        """
        proof of work algorithm:
        finds the nonce that expression '{last_nonce}{nonce}' ends in 4 zeroes
        :param last_nonce: <int> the nonce of last block
        :param difficulty" <int> the number of ending zeroes
        :return: <int> newly found nonce
        """
        last_block = self.last_block
        last_nonce = last_block["nonce"]
        nonce = 0
        while self.validate_nonce(last_nonce, nonce, difficulty) is False:
            nonce += 1

        return nonce

    @staticmethod
    def validate_nonce(last_nonce, nonce, difficutly):
        """
        checks if hash(last_nonce,nonce) contains ending zeroes as many as difficulty ?

        :param last_nonce: <int> previous nonce
        :param nonce:  <int> current testing nonce
        :return:  <bool> true if condition is true

        """
        expr = f'{last_nonce}{nonce}'.encode()
        expr_hash = sha256(expr).hexdigest()
        return expr_hash[:-4] == ("0" * difficutly)

    def valid_chain(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def resolve_conflicts(self):
        pass


# blockchain fucking api :)
app = Flask(__name__)
CORS(app)
blockchain = Blockchain()


# the index page
@app.route('/')
def index():
    # should render index.html from templates
    pass


# configure page
@app.route('/configure')
def configure():
    # should render configure.html from templates
    pass


# new transaction
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # post contains a from
    form = request.form
    required_fields = ['sender_address', 'receiver_address', 'amount', 'signature']
    # checks that all values be present in form
    if not all(field in form for field in required_fields):
        return 'Missing value', 400

    sender_address = form['sender_address']
    receiver_address = form['receiver_address']
    amount = form['amount']
    signature = form['signature']
    transaction_result = blockchain.submit_transaction(sender_address, receiver_address, amount, signature)

    if transaction_result == False:
        response = {
            'message': 'Invalid Transaction!',
        }
        # 406 is 'not acceptable' response :")
        return jsonify(response), 406
    else:
        response = {
            'message': 'Transaction will be added to block' + str(transaction_result)
        }
        return jsonify(response), 201


# get transactions
@app.route('transactions/get', methods=['GET'])
def get_transactions():
    # getting the transactions from mempool
    transactions = blockchain.transactions
    response = {
        'message': 'current transactions in the mempool',
        'transactions': transactions
    }
    return jsonify(response), 200


# get chain
@app.route('/chain', methods=['GET'])
def get_full_chain():
    chain = blockchain.chain
    response = {
        'chain': chain,
        'length': len(chain)
    }
    return jsonify(response), 200


# mine
@app.route('/mine', methods=['GET'])
def mine():
    # we get the nonce of the last block in blockchain
    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()  # we can set the difficulty manualy too

    # reserving a reward for ourself
    blockchain.submit_transaction(sender_address=MINNING_SENDER, receiver_address=blockchain.node_id,
                                  value=MINNING_REWARD, signature="")

    previous_hash=blockchain.hash_block(last_block)
    new_block=blockchain.create_block(nonce,previous_hash)

    response={
        'message':'new block added to blockchain',
        'block_number':new_block['block_number'],
        'transactions':new_block['transactions'],
        'nonce':new_block['nonce'],
        'previous_hash':new_block['previous_hash']
    }
    return jsonify(response),200


# registering node

# resolving conflicts

# getting nodes

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='listening port')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)
