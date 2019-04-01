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

    return freq

def findkey(cipher, n):
    key = ""
    for i in range(n):
        parts = ""
        for j in range(i, len(cipher), n):
            parts = parts + cipher[j]
        freq = letter_freq(parts)
        ind = int(np.where(freq == np.max(freq))[0])
        if ind < 4:
            freq[ind] = -1
            ind = int(np.where(freq == np.max(freq))[0])
        letter = chr(ind+61)
        key = key + letter
    return key

fname = input("Enter the name of the file: ")
n = int(input("Enter the length: "))
fhand = open(fname, "r")
cipher = ""
for line in fhand:
    cipher = cipher + line

key = findkey(cipher, n)
print("The Estimated key is", key)
