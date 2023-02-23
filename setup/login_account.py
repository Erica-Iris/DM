#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This is an experimental Python version of libgourou. 
'''

from setup.libadobe import createDeviceKeyFile, FILE_DEVICEKEY, FILE_DEVICEXML, FILE_ACTIVATIONXML
from setup.libadobeAccount import createDeviceFile, createUser, signIn, activateDevice, exportAccountEncryptionKeyDER, getAccountUUID
from os.path import exists

VAR_MAIL = ""
VAR_PASS = ""
VAR_VER = 1 # None # 1 for ADE2.0.1, 2 for ADE3.0.1
KEYPATH = "adobekey.der"

#################################################################

def takeInput():

    global VAR_MAIL
    global VAR_PASS

    VAR_MAIL = input("Enter Mail: ")
    VAR_PASS = input("Enter Password: ")

    if VAR_MAIL == "" or VAR_MAIL == "":
        print("It cannot be empty")
        print()
        exit(1)


def loginAndGetKey():

    global VAR_MAIL
    global VAR_PASS
    global VAR_VER
    global KEYPATH

    # acc files
    if (not exists(FILE_ACTIVATIONXML)) or (not exists(FILE_DEVICEXML)) or (not exists(FILE_DEVICEKEY)):
        
        takeInput()
        print("Logging in")
        print()

        createDeviceKeyFile()

        success = createDeviceFile(True, VAR_VER)
        if (success is False):
            print("Error, couldn't create device file.")
            exit(1)

        success, resp = createUser(VAR_VER, None)
        if (success is False):
            print("Error, couldn't create user: %s" % resp)
            exit(1)

        success, resp = signIn("AdobeID", VAR_MAIL, VAR_PASS)
            
        if (success is False):
            print("Login unsuccessful: " + resp)
            exit(1)

        success, resp = activateDevice(VAR_VER, None)
        if (success is False):
            print("Couldn't activate device: " + resp)
            exit(1)

        print("Authorized to account " + VAR_MAIL)


    # KEY
    if not exists(KEYPATH):
        print("Exporting keys ...")
        try: 
            account_uuid = getAccountUUID()
            if (account_uuid is not None):
                filename = KEYPATH
                success = exportAccountEncryptionKeyDER(filename)
                if (success is False):
                    print("Couldn't export key.")
                    exit(1)
                print("Successfully exported key for account " + VAR_MAIL + " to file " + filename)

            else:
                print("failed")
                exit(1)

        except Exception as e: 
                print(e)
                exit(1)

    print('All Set')
    print()