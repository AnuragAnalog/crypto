#!/usr/bin/python3

import numpy as np

def encrypt(plaintext, key):
    keylen = len(key)
    key_as_int = np.array([ord(i) for i in key])
    plaintext_int = np.array([ord(i) for i in plaintext])
    ciphertext = ""
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % keylen]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def decrypt(ciphertext, key):
    keylen = len(key)
    key_as_int = np.array([ord(i) for i in key])
    ciphertext_int = np.array([ord(i) for i in ciphertext])
    plaintext = ""
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % keylen]) % 26
        plaintext += chr(value + 65)
    return plaintext

def input_m():
    fin = input("Enter the name of the input-file: ")
    key = input("Enter the key: ")
    message = ""
    fhand = open(fin, "r")
    for line in fhand:
        message = message + line
    return message, key

def output_m(message):
    fout = input("Enter the name of the ouput-file: ")
    fhand = open(fout, "w")
    fhand.write(message)
    fhand.write("\n")

print("What do you want to do?")
print("1) Encryption.")
print("2) Decryption.")
opt = int(input("Your choice> "))

if opt == 1:
    plain, key = input_m()
    cipher = encrypt(plain, key)
    output_m(cipher)
elif opt == 2:
    cipher, key = input_m()
    plain = decrypt(cipher, key)
    output_m(plain)
else:
    print("### INVALID OPTION ###")

