#!/usr/bin/python3

import numpy as np

def letter_freq(line):
    freq = [0 for i in range(26)]
    for char in line:
        if char == "\n":
            continue
        freq[ord(char)-65] = freq[ord(char)-65] + 1
    lfreq = dict()
    for i in range(26):
        lfreq[chr(i+65)] = freq[i]

    return lfreq

def chisquared(line, efreq):
    freq = letter_freq(line)
    chi = 0
    for i in range(26):
        c = freq[chr(i+65)]
        e = len(line)*efreq[i]
        chi = chi + ((c-e)*(c-e))/e
    return chi

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

def initialize():
    engfreq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    engfreq = np.array(engfreq)
    """efreq = dict()
    for i in range(26):
        efreq[chr(i+65)] = engfreq[i]"""
    return engfreq

def keyfind(cipher, n, efreq):
    key = ""
    chivalues = [0  for i in range(26)]
    for i in range(n):
        parts = ""
        for j in np.arange(i, len(cipher), n):
            parts = parts + cipher[j]
        for i in range(26):
            decipher = decrypt(parts, chr(i+65))
            chi = chisquared(decipher, efreq)
            chivalues[i] = chi
        chivalues = np.array(chivalues)
        ind = int(np.where(chivalues == min(chivalues))[0])
        key = key + chr(ind+65)
    return key

fname = input("Enter the name of the file: ")
n = int(input("Enter the length: "))
fhand = open(fname, "r")
cipher = ""
for line in fhand:
    cipher = cipher + line

efreq = initialize()
key = keyfind(cipher, n, efreq)
print("Estimated key is:", key)
