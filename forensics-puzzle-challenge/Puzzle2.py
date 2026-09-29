# Puzzle 2 - SHA256 Hash Checks
# Find 6-char lowercase string whose SHA256 matches conditions

import hashlib
import struct
from itertools import combinations, permutations

alpha = 'abcdefghijklmnopqrstuvwxyz'

for combo in combinations(alpha, 6):
    for perm in permutations(combo):
        text = ''.join(perm)
        h = hashlib.sha256(text.encode()).digest()

        # Check 1: First 4 bytes (big-endian)
        first = struct.unpack('>I', h[0:4])[0]
        if first != 1637493967:
            continue

        # Check 2: Last 4 bytes (big-endian)
        last = struct.unpack('>I', h[-4:])[0]
        if last != 2639439759:
            continue

        # Check 3: Sum of middle bytes % 65536
        mid = sum(h[4:-4]) % 65536
        if mid == 3403:
            print(f"Puzzle 2 answer: {text}")
            break


