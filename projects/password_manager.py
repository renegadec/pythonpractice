from cryptography.fernet import Fernet

# create key using code below
''' def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"Username: {user} | Password: {fer.decrypt(passw.encode()).decode()}" )
        

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    option = input("1. Add New Password 2. View Existing Password Q. To Quit: ")
    if option.lower() == "q":
        break

    if option == "1":
        add()
    elif option == "2":
        view()
    else:
        print("invalid option")
        continue