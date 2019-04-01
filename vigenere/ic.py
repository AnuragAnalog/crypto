#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

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

def ic(freq):
    num = 0
    hist = list(freq.values())
    N = sum(freq.values())

    for n in hist:
        num = num + n*(n-1)
    ko = num/(N*(N-1))

    return ko

def partition(cipher, k):
    parts = ["" for i in range(k)]
    for i in np.arange(0, len(cipher), k):
        for j in range(k):
            parts[j] = parts[j] + cipher[i+j]
            if cipher[i+j] == cipher[-1]:
                break
    ics = 0
    for i in range(k):
        freq = letter_freq(parts[i])
        ics = ics + ic(freq)
    return ics/k

fname = input("Enter the file name: ")
n = int(input("Enter the value of n: "))
fhand = open(fname, "r")
cipher = ""
for line in fhand:
    cipher = cipher + line

icavg = [0 for i in range(n)]
for i in range(2, n):
    icavg[i] = partition(cipher, i)

plt.title("Average I.C's for different key period", fontsize=15)
plt.xlabel("Period")
plt.ylabel("Average of I.C's")
plt.show(plt.stem(range(2, n), icavg[2:]))
