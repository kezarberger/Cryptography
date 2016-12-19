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
nummes = []
numkey = []
combine = []
while again == True:
    if no == ("q"):
        print ("Goodbye!")
        again = False
    elif no not in ("e", "d", "q"):
        no = input("Did not understand command, try again: ")
    elif no == "e":
        fist = input("Message: ")
        for c in fist:
            nummes.append(associations.find(c))
        print (nummes)
        iam = input("Key: ") 
        for i in iam:
            numkey.append(associations.find(i))
        numkey = numkey*10
        print (numkey)
        kez = []
        for x in range(len(nummes)):
            kez.append(nummes[x] + numkey[x])
        print (kez)
        again = False
    elif no == "d":
        input("Message: ")
        input ("Key: ")
        again = False