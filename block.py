import hashlib


class Block:
    __hashAlgorithm = "sha3_512"

    @staticmethod
    def hashAlgorithm() -> str:
        return Block.__hashAlgorithm

    def __init__(self, data, previous_hash) -> None:
        self.hash = hashlib.new(Block.__hashAlgorithm)
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0

    def __str__(self) -> str:
        return "{}{}{}".format(self.previous_hash.hexdigest(), self.data, self.nonce)

    def mine(self, difficulty: int):
        self.hash.update(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > 2 ** (
            self.hash.digest_size * 8 - difficulty
        ):
            self.nonce += 1
            self.hash = hashlib.new(Block.__hashAlgorithm)
            self.hash.update(str(self).encode("utf-8"))
