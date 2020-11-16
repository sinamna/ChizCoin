from uuid import uuid4


class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        self.node_id = str(uuid4()).replace('-', ' ')

    def register_node(self, node_url):
        pass

    def verify_transaction_signature(self, sender_address, signature, transaction):
        pass

    def submit_transaction(self, sender_address, receiver_address, value, signature):
        pass

    def create_block(self, nonce, previous_hash):
        pass

    def hash(self, block):
        pass

    def proof_of_work(self):
        pass

    def valid_chain(self):
        pass

    def resolve_conflicts(self):
        pass
