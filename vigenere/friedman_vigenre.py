
def letter_freq(fhand):
    freq = [0 for i in range(26)]
    for line in fhand:
        for char in line:
            if char == "\n":
                continue
            freq[ord(char)-65] = freq[ord(char)-65] + 1
    lfreq = dict()
    for i in range(26):
        lfreq[chr(i+65)] = freq[i]

    return lfreq

def vigenere_key(freq):
    kp = 0.067
    kr = 0.0385
    num = 0
    hist = list(freq.values())
    N = sum(freq.values())

    for n in hist:
        num = num + n*(n-1)
    ko = num/(N*(N-1))
    key = (kp - kr)/(ko - kr)

    return key

fname = input("Enter the name of the file: ")
fhand = open(fname, "r")
freq = letter_freq(fhand)
key = vigenere_key(freq)
print("Estimated key length is:", key)
