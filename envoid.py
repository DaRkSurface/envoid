#####################################################
## Void Encryption/Decryption tool (EnVoid)        ##
## Fun Project to VoidSecurity                     ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################


# Imports
import os
import time
from cryptography.fernet import Fernet
from termcolor import colored
import pyfade

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
    print(colored("-----------------------------------------------------------------------------------------------------", "green"))
    print(colored("--Envoided Ciphertxt--:", "red"))
    print(colored(str(envoided, 'utf-8', "red")))
    print(colored("-----------------------------------------------------------------------------------------------------", "green"))
    print(colored("--KEY--:", "red"))
    print(str(key, 'utf-8'))
    print(colored("-----------------------------------------------------------------------------------------------------", "green"))

    time.sleep(8)
    print("""\n\n
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
    print("""\n\n
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
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
                               
    ███████╗███╗   ██╗██╗   ██╗ ██████╗ ██╗██████╗ 
    ██╔════╝████╗  ██║██║   ██║██╔═══██╗██║██╔══██╗
    █████╗  ██╔██╗ ██║██║   ██║██║   ██║██║██║  ██║
    ██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██║   ██║██║██║  ██║
    ███████╗██║ ╚████║ ╚████╔╝ ╚██████╔╝██║██████╔╝
    ╚══════╝╚═╝  ╚═══╝  ╚═══╝   ╚═════╝ ╚═╝╚═════╝ 
                                               
"""))

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
        print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
  
    ███████╗███╗   ██╗██╗   ██╗ ██████╗ ██╗██████╗ 
    ██╔════╝████╗  ██║██║   ██║██╔═══██╗██║██╔══██╗
    █████╗  ██╔██╗ ██║██║   ██║██║   ██║██║██║  ██║
    ██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██║   ██║██║██║  ██║
    ███████╗██║ ╚████║ ╚████╔╝ ╚██████╔╝██║██████╔╝
    ╚══════╝╚═╝  ╚═══╝  ╚═══╝   ╚═════╝ ╚═╝╚═════╝ 
        """)) 
        print("""                                            
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
        print("Did not reckognize input, quitting.")
        time.sleep(0.5)
        quit()
    
#################################################

clearcmd()
art()
options()
