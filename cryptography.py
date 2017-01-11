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
dummes = []
dumkey = []
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
        iam = input("Key: ") 
        for i in iam:
            numkey.append(associations.find(i))
        numkey = numkey*10
        kez = []
        for x in range(len(nummes)):
            y = (nummes[x] + numkey[x])
            if y > 84:
                y = y - 85
            kez.append(y)
        another = ""
        for z in kez:
            another = another + associations[z]
        print (another)
        again = False
    elif no == "d":
        nwdid = input("Message: ")
        for f in nwdid:
            dummes.append(associations.find(f))
        idw = input ("Key: ")
        for k in idw:
            dumkey.append(associations.find(k))
        dumkey = dumkey*10
        forget = []
        for p in range(len(dummes)):
            n = dummes[p] - dumkey[p]
            if n < 0:
                n = n+85
            forget.append(n)
        result = ""
        for g in forget:
            result = result + associations[g]
        print (result)
        again = False

        
        
