import hashlib

class IronCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike Sends 3.2 IC to Bob"
t4 = "Danile Sends 0.3 IC to Anna"
t5 = "Mike Sends 1 IC to Charle"
t6 = "Mike Sends 5.4 IC to Danile"

initial_block = IronCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = IronCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = IronCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)