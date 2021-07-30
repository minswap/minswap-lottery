import random

SEED = "f311cd852027b18d83ff33cc888d5a4ed2cdfd8c6f1a61ce314d5e56dc6c9db9"

with open("pools.txt") as f:
    pools = f.read().splitlines()

random.seed(SEED)
# Number of pools needs to be <= 2080 in order to fit within Python's Mersenne Twister implemetation's period
random.shuffle(pools)

for p in pools:
    print(p)
