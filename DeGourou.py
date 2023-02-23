from setup.login_account import loginAndGetKey
from setup.fulfill import downloadFile

from decrypt.decodePDF import decryptPDF
from decrypt.decodeEPUB import decryptEPUB

import argparse
from os import mkdir, remove, rename
from os.path import exists

from setup.params import FILE_DEVICEKEY, FILE_DEVICEXML, FILE_ACTIVATIONXML
from decrypt.params import KEYPATH
from setup.data import createDefaultFiles

def main(acsmFile, login):
    
    # user login
    if login:
        if not exists("account"):
            mkdir("account")
        loginAndGetKey()
        exit(0)

    # setting up the account and keys
    if not (exists(FILE_ACTIVATIONXML) and exists(FILE_DEVICEXML) and exists(FILE_DEVICEKEY) and exists(KEYPATH)):
        if not exists("account"):
            mkdir("account")
        createDefaultFiles()

    # cheek for file existance
    if not exists(acsmFile):
        print(f"{acsmFile} file does not exist")
        print()
        exit(1)

    # download
    encryptedFile = downloadFile(acsmFile)
    print(encryptedFile)
    print()

    # decrypt
    if encryptedFile.endswith(".pdf"):
        decryptedFile = decryptPDF(encryptedFile)
    elif encryptedFile.endswith(".epub"):
        decryptedFile = decryptEPUB(encryptedFile)
    else:
        print("File format not supported")
        print()
        exit(1)

    remove(encryptedFile)
    rename(decryptedFile, encryptedFile)
    decryptedFile = encryptedFile
    print(decryptedFile)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and Decrypt an encrypted PDF or EPUB file. It uses Dummy account for ADE, you can overide using --login")
    parser.add_argument("file", type=str, nargs='?', default="URLLink.acsm", help="Path to the ACSM file")
    parser.add_argument("-l", "--login", action="store_true", help="Login to your ADE account. (optional)")
    args = parser.parse_args()
    if args.file == "URLLink.acsm" and not exists(args.file):
        parser.print_help()
    else:
        main(args.file, args.login)
