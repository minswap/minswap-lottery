import random

SEED = "4bca53c717e88696e0d432600784d10339f6d8a1522f06867fd096641750a606"

with open("pools.txt") as f:
    pools = f.read().splitlines()

random.seed(SEED)
# Number of pools needs to be <= 2080 in order to fit within Python's Mersenne Twister implemetation's period
random.shuffle(pools)

print(pools)
