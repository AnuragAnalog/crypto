#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def word_dis(cipher, wsize):
    for i in range(len(wsize)):
        for j in range(len(cipher)):
            cword = cipher[j:j+wsize[i]]
            for k in range(j, len(cipher)-wsize[i]):
                if cword == cipher[k:k+wsize[i]]:
                    print(cword)

n = int(input("Enter the size: "))
fhand = open("cipher2018.txt.txt", "r")
cipher = ""
for line in fhand:
    cipher = cipher + line

wsize = [i for i in range(3, n)]
word_dis(cipher, wsize)

"""plt.title("Average I.C's for different key period", fontsize=15)
plt.xlabel("Period")
plt.ylabel("Average of I.C's")
plt.show(plt.stem(range(2, n), icavg[2:]))"""
