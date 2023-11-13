import hashlib

from block import Block


class Chain:
    def __init__(self, difficulty: int) -> None:
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []
        self.__create_genesis_block()

    def proof_of_work(self, block: Block) -> bool:
        h = hashlib.new(Block.hashAlgorithm())
        h.update(str(block).encode("utf-8"))
        val = h.hexdigest()
        return (
            block.hash.hexdigest() == val
            and int(val, 16) < 2 ** (h.digest_size * 8 - self.difficulty)
            and block.previous_hash == self.blocks[-1].hash
        )

    def __create_genesis_block(self):
        h = hashlib.new(Block.hashAlgorithm())
        h.update("".encode("UTF-8"))
        origin = Block("GENESIS", h)
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def add_to_chain(self, block: Block) -> None:
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self, data):
        self.pool.append(data)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)

            print("\n==============================")
            print("Hash:\n", block.hash.hexdigest())
            print("Previous Hash:\n", block.previous_hash.hexdigest())
            print("Nonce:\t\t", block.nonce)
            print("Data:\t\t", block.data)
            print("\n==============================")