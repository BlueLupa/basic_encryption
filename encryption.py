from random import randint
import os
def encrypt(plaintext: str, key: str, decrypt: bool) -> str:
    encrypted = ""
    for i,c in enumerate(plaintext):
        base = 32
        range = 95
        key_char = key[i%len(key)]
        shift = ord(key_char)-base
        if decrypt:
            shift=-shift
        encrypted += chr(((ord(c)-base) + shift)%range+base)
    return encrypted
def gen_key(bytes: int) -> str:
    key = ""
    for i in range(bytes):
        char = chr(randint(32,126))
        key+=char
    return key
os.system('clear')
message = input("Enter the message: ")
key = input("Enter the key (type 'r' for random): ")
if key=='r':
    key = gen_key(128)
encrypted = encrypt(message, key, False)
decrypted = encrypt(encrypted, key, True)
print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Key: {key}")