""""
cryptography.py
Author: kezar
Credit: kotz

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
no = input("Enter e to encrypt, d to decrypt, or q to quit: ")
again = True
numlist = []
while again == True:
    if no == ("q"):
        print ("Goodbye!")
        again = False
    elif no not in ("e", "d", "q"):
        no = input("Did not understand command, try again: ")
    elif no == "e":
        fist = input("Message: ")
        for c in fist:
            numlist.append(associations.find(c) +1)
            print (numlist)
        input("Key: ") 
        again = False
    elif no == "d":
        input("Message: ")
        input ("Key: ")
        again = False