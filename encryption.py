from random import randint
import os
import re
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
        char = chr(randint(33,126))
        key+=char
    return key
os.system('clear')
message = input("Enter the message: ")
print("Would you like to:")
print("1. Encrypt")
print("2. Decrypt")
option = re.sub(r'[^0-9]',"",input(""))
print()
match option:
    case "1":
        key = input("Enter the key (type 'r' for random): ")
        print()
        if key=='r':
            key = gen_key(128)
        encrypted = encrypt(message, key, False)
        print(f"Original: {message}")
        print()
        print(f"Encrypted: {encrypted}")
        print()
        print(f"Key: {key}")
    case "2":
        key = input("Enter the key: ")
        print()
        decrypted = encrypt(message, key, True)
        print(f"Original: {message}")
        print()
        print(f"Decrypted: {decrypted}")
        print()
        print(f"Key: {key}")
    case _:
        print(f"'{option}' is not a valid option")