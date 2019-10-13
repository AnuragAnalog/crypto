"""
    Rot13 is a special case of ceaser cipher in which both the encryption
and decryption algorithms are same.
"""

def rot13(fhand):
    message = ""
    for line in fhand:
        for i in range(len(line)):
            if ord(line[i]) in range(65, 92):
                c = (ord(line[i])+13-65)%26
                lim = 65
            elif ord(line[i]) in range(97, 124):
                c = (ord(line[i])+13-97)%26
                lim = 97
            message = message + chr(c+lim)
    return message

fname = input("Enter the name of text-file: ")
fhand = open(fname, "r")

message = rot13(fhand)
print(message)
