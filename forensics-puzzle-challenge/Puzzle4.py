# Puzzle 4 - Arithmetic Constraints
# Find 6-char lowercase string satisfying multiple arithmetic checks

from itertools import combinations_with_replacement, permutations

alpha = 'abcdefghijklmnopqrstuvwxyz'

for combo in combinations_with_replacement(alpha, 6):
    # Quick filter: sum must equal 667
    if sum(ord(c) for c in combo) != 667:
        continue

    for perm in set(permutations(combo)):
        arr = [ord(c) for c in perm]

        # Check 1: sum == 667
        if sum(arr) != 667:
            continue

        # Check 2: Running product % 65536 == 48256
        p = 1
        for x in arr:
            p = p * x % 65536
        if p != 48256:
            continue

        # Check 3: Weighted sum XOR 0xDEADBEEF == 3736075110
        num3 = 0
        for k in range(6):
            num4 = 1
            for l in range(k):
                num4 = num4 * 137 % 65535
            num3 += arr[k] * num4 % 65535
        num3 ^= 0xDEADBEEF
        if num3 != 3736075110:
            continue

        # Check 4: Pair relation == 3416554022
        num5 = 0
        for m in range(0, 6, 2):
            num5 += (arr[m] << 8 | arr[m+1]) * 2654435769 % (2**32)
        num5 &= 0xFFFFFFFF
        if num5 != 3416554022:
            continue

        # Check 5: Sum of squares % 65535 == 8736
        num6 = sum(x*x for x in arr) % 65535
        if num6 != 8736:
            continue

        # Check 6: Final polynomial % 16777215 == 8641177
        num8 = arr[0] << 16 | arr[1] << 8 | arr[2]
        num9 = arr[3] << 16 | arr[4] << 8 | arr[5]
        if (num8 * 31 + num9 * 37) % 16777215 == 8641177:
            print(f"Puzzle 4 answer: {''.join(chr(x) for x in arr)}")
            break


