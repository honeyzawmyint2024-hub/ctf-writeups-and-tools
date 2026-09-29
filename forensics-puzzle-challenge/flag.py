import hashlib

with open(r'extracted_soundtrack.mp3', 'rb') as f:
    mp3_data = f.read()

print(f"MP3 loaded: {len(mp3_data)} bytes")

# Step 2: Compute key2 
key2 = hashlib.sha256(mp3_data).digest()
print(f"key2: {key2.hex()}")

#  Step 3: Build key1 
bonus1 = "sacred"
bonus2 = "forest"
bonus3 = "temple"
bonus4 = "spirit"
key1 = f"{bonus1}_{bonus2}_{bonus3}_{bonus4}".encode()
print(f"key1: {key1.decode()}")

#  Step 4: Encrypted flag from decompiled source 
ENCRYPTED_FLAG = bytes([
    110, 159, 249,  74,  19, 236,  99, 192,
     35,  43, 131, 226,  36, 229,   0, 231,
    110,  93, 167,  26, 107, 185,  39, 217,
     22,  98,  97,   1,  90, 142,  68,  91,
      3, 161, 157,  33, 115, 152, 112, 161,
     17,  46, 131, 181
])

# Step 5: Decrypt 
flag = bytearray(
    ENCRYPTED_FLAG[i] ^ key1[i % len(key1)] ^ key2[i % len(key2)]
    for i in range(len(ENCRYPTED_FLAG))
)

print(f"\nFlag: {flag.decode('utf-8')}")