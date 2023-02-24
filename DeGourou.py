from setup.loginAccount import loginAndGetKey
from setup.fulfill import downloadFile

from decrypt.decodePDF import decryptPDF
from decrypt.decodeEPUB import decryptEPUB

import argparse
from os import mkdir, remove, rename
from os.path import exists
from sys import exit

from setup.params import FILE_DEVICEKEY, FILE_DEVICEXML, FILE_ACTIVATIONXML
from decrypt.params import KEYPATH
from setup.data import createDefaultFiles

def main(acsmFile, login, outputFilename):
    
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

    print()

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
    if outputFilename is None:
        tempName = encryptedFile
    else:
        tempName = outputFilename
    rename(decryptedFile, tempName)
    print(tempName)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and Decrypt an encrypted PDF or EPUB file. It uses Dummy account for ADE, you can overide using --login")
    parser.add_argument("file", type=str, nargs='?', default=None, help="Path to the ACSM file")
    parser.add_argument("-l", "--login", action="store_true", help="Login to your ADE account. (optional)")
    parser.add_argument("-o", "--output", type=str,  default=None, help="Output file name. (optional)")
    args = parser.parse_args()

    # check for default value
    if args.file == None:
        if exists("URLLink.acsm"):
            args.file = "URLLink.acsm"
        else:
            parser.print_help()
            exit(0)

    main(args.file, args.login, args.output)
