#creating a password manager
from cryptography.fernet import Fernet 
import base64
''' 
def write_key():
    encryption = fer.generate_key
    with open('encryption.key', 'wb') as key:
        key.write(encryption)
'''
def load_key():
    file = open("encrypt.key", 'rb')
    encryption = file.read()
    file.close()
    return encryption

'''
sudo_pwd = input("Enter the sudo password:")
'''
encrypt = load_key() 
cypto = base64.urlsafe_b64encode(encrypt)

#functions
def view():
    with open('passwd.txt','r') as vault:
        for data in vault.readlines():
            pwd_data = data.rstrip()  #strips the blank new line created be \n
            user , passw = pwd_data.split("|") #this splits every | and makes it a list 
            print("User name :", user, "& Password:", cypto.decrypt(passw.encode()).decode())
def add():
    acc_name = input("Enter Account name:")
    pwd = input("Enter password ")

    with open('passwd.txt', 'a') as vault: #a- append , w- overwrite , r -read only
        vault.write(acc_name + "|" + cypto.encrypt(b'pwd.encode()').decode() + "\n") 


while True:
    operation = input("View or Add password or Press q to quit: ").lower()

    if operation == "q":
        print("Poitu vaanga tataa")
        break
    if operation == "view":
        view()
    elif operation == "add":
        add()
    else:
        print("Invalid operation")
        continue 

'''
while True:
    operation = input("Add or View press q to quit? ").lower()
    if operation == "q":
        break

    if (operation == "view") or  (operation == "view"):
        view()
    elif operation == "add" or "Add":
        add()
    else:
        print("Invalid mode.")
        continue

'''