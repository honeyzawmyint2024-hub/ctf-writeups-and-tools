# Puzzle 3 - Iterated SHA256 with Salts
# Find 6-char string starting with 't' and ending with 'e'

import hashlib
from itertools import product

alpha = 'abcdefghijklmnopqrstuvwxyz'
salt1 = "secret_salt_for_re_challenge"
salt2 = "additional_entropy_2024"

for combo in product(alpha, repeat=4):
    text = 't' + ''.join(combo) + 'e'

    # Hash 1000 times with salt1
    arr = text.encode()
    for _ in range(1000):
        arr = hashlib.sha256(arr + salt1.encode()).digest()

    # Final hash with salt2
    final = hashlib.sha256(arr + salt2.encode()).hexdigest()

    # Check specific positions of the final hash
    if (final[:8]    == 'e7521280' and
        final[24:32] == 'e45810fe' and
        final[-8:]   == '99d3ba76'):
        print(f"Puzzle 3 answer: {text}")
        break


