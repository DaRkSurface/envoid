#####################################################
## Void Encryption/Decryption tool (EnVoid)        ##
## Made to communicate with VoidSecurity Memebers. ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################


# Imports
import os
import time
from cryptography.fernet import Fernet
import clipboard

#################################################

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def encrypt():
    key = Fernet.generate_key()

    envoid = Fernet(key)

    plaintext = input("Text to EnVoid: ")
    bytetext = bytes(plaintext, encoding= 'utf-8')
    print("[*] Encrypting..\n ")
    time.sleep(0.3)
    envoided = envoid.encrypt(bytetext)
    

    print(str(envoided, 'utf-8'))
    print(str(key, 'utf-8'))

    time.sleep(8)
    print("""
    ------------------------------------------
    [1] Decrypt again.
    [2] Options
    [3] Quit
    """)
    select = input("Option: ")
    if select == "1":
        print("Encrypting again. ")
        time.sleep(0.5)
        clearcmd()
        encrypt()
    elif select == "2":
        clearcmd()
        options()
    elif select == "3":
        print("quitting..")
        time.sleep(0.5)
        quit()
    else:
        print("did not reckognize input.")
        print("Quitting.")
        time.sleep(0.5)
        quit()
    

def decrypt():
    ciphertext = input("Eneter EnVoided text: ")
    bytetext = bytes(ciphertext, encoding= 'utf-8')

    key = input("Enter key: ")
    devoid = Fernet(key)
    print("[*] Decrypting.. \n")
    time.sleep(0.3)
    devoided = devoid.decrypt(bytetext)
    print(str(devoided, 'utf-8'))
    time.sleep(8)
    print("""
    ------------------------------------------
    [1] Decrypt again.
    [2] Options
    [3] Quit
    """)
    select = input("Option: ")
    if select == "1":
        print("Decrypting again. ")
        time.sleep(0.5)
        clearcmd()
        decrypt()
    elif select == "2":
        clearcmd()
        options()
    elif select == "3":
        print("quitting..")
        time.sleep(0.5)
        quit()
    else:
        print("did not reckognize input.")
        print("Quitting.")
        time.sleep(0.5)
        quit()

def art():
    print("""
                               
     _____     _____     _   _ 
    |   __|___|  |  |___|_|_| |
    |   __|   |  |  | . | | . |
    |_____|_|_|\___/|___|_|___|
                           
    """)

def options():
    optionslayout = print("""
    [1] Encrypt Plaintext
    [2] Decrypt Ciphertext
    [3] Credits
    [4] Quit
    """)
    option = input("Option: ")
    if option == "1":
        encrypt()
    elif option == "2":
        decrypt()
    elif option == "3":
        clearcmd()
        print("""
         _____     _____     _   _ 
        |   __|___|  |  |___|_|_| |
        |   __|   |  |  | . | | . |
        |_____|_|_|\___/|___|_|___|
                   
                Coded by drk

        Encryptor/Decrytor for VoidSecurity
        https://voidsecurity.ml/downloads/envoid/

        """)
        time.sleep(4)
        clearcmd()
        art()
        options()
    elif option == "4":
        print("[-] Quitting..")
        time.sleep(0.5)
        quit()
    else:
        print("Did not reckognizq input, quitting.")
        time.sleep(0.5)
        quit()
    
#################################################

clearcmd()
art()
options()