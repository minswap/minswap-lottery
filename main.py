import random

SEED = "4bca53c717e88696e0d432600784d10339f6d8a1522f06867fd096641750a606"

with open("pools.txt") as f:
    pools = f.read().splitlines()

random.seed(SEED)
random.shuffle(pools)

print(pools)
