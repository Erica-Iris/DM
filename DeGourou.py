from setup.login_account import loginAndGetKey
from setup.fulfill import downloadFile

from decrypt.decodePDF import decryptPDF
from decrypt.decodeEPUB import decryptEPUB

# setting up the account and keys
loginAndGetKey()

# acsm file
acsmFile = input("Enter ACSM file (press enter if the file name is URLLink.acsm): ")
if acsmFile == "":
    from os.path import exists
    if exists("URLLink.acsm"):
        acsmFile = "URLLink.acsm"
    else:
        print("URLLink.acsm file does not exists")
        print()
        exit(1)

# downlaod
enrcyptedFile = downloadFile(acsmFile)
print(enrcyptedFile)
print()

# decrypt
if enrcyptedFile.endswith(".pdf"):
    decryptedFile =  decryptPDF(enrcyptedFile)
elif enrcyptedFile.endswith(".epub"):
    decryptedFile =  decryptEPUB(enrcyptedFile)
else:
    print("Not in supported file formats")
    print()
    exit(1)

from os import remove, rename
remove(enrcyptedFile)
rename(decryptedFile,enrcyptedFile)
decryptedFile = enrcyptedFile
print(decryptedFile)
print()