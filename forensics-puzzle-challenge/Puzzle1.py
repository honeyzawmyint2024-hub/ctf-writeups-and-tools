# Puzzle 1 - Polynomial Hash Constraints
# Find 6-char lowercase string satisfying all conditions

alpha = 'abcdefghijklmnopqrstuvwxyz'
target_sum = 626  # derived from: sum*7919 % 10000 == 7294

for a in alpha:
    for b in alpha:
        for c in alpha:
            for d in alpha:
                for e in alpha:
                    # Use sum constraint to determine 6th char
                    rem = target_sum - ord(a)-ord(b)-ord(c)-ord(d)-ord(e)
                    if rem < 97 or rem > 122:
                        continue
                    f = chr(rem)
                    s = a+b+c+d+e+f

                    # Check 1: Polynomial hash
                    num = 0
                    for ch in s:
                        num = (num * 31 + ord(ch)) % 1000000
                    if num != 995996:
                        continue

                    # Check 2: Weighted sum
                    num3 = sum((i+1)*ord(ch) for i,ch in enumerate(s)) % 10000
                    if num3 != 2167:
                        continue

                    # Check 3: Pair product
                    prod = (ord(s[0])*ord(s[1]) + ord(s[2])*ord(s[3]) + ord(s[4])*ord(s[5])) % 10000
                    if prod == 2541:
                        print(f"Puzzle 1 answer: {s}")
                        break


