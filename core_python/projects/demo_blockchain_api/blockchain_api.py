import datetime
import hashlib
import json

from flask import Flask, jsonify


# In java, I made Blockchain as an ArrayList, here blockchain is an object containing everything...
# Something is not right...


class Blockchain:

    def __init__(self):
        self.chain = []

        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash,
        }
        print("Created Block:", block)
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(
                    new_proof**2 - previous_proof**2
                ).encode()  # Proof**2, where is the payload
            ).hexdigest()
            if hash_operation[:5] == "00000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()  # Sorted keys
        print("Encoded Block", json.loads(encoded_block))
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:5] != "00000":
                return False
            previous_block = block
            block_index += 1
        return True


app = Flask(__name__)
blockchain = Blockchain()

# blockchain.chain.append({"proof":"First Block"})


@app.route("/mine_block", methods=["GET"])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        "message": "1 block mined",
        "index": block["index"],
        "timeStamp": block["timestamp"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200  # json.dumps()


@app.route("/get_chain", methods=["GET"])
def display_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(response), 200


@app.route("/valid_chain", methods=["GET"])
def valid_chain():
    valid = blockchain.is_chain_valid(blockchain.chain)
    if valid:
        return jsonify({"message": "The block chain is valid"}), 200
    else:
        return jsonify({"message": "The block chain is corrupt"}), 200


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
