import string
import random
import base64
import os

def pwd_gen(length, special, digits, toggle):
    pwd= []
    #Entire character set
    chars = "".join(string.ascii_letters)
    if digits: #toggle for digits
        chars = chars.join(string.digits)
        pwd.append(random.choice(string.digits))
    if special: #toggle for special characters
        chars = chars.join("!@#$%^&*?_")
        pwd.append(random.choice("!@#$%^&*?_"))
    pwd.append(random.choice(string.ascii_uppercase)) #picking one lowercase letter
    pwd.append(random.choice(string.ascii_lowercase)) #picking one uppercase letter
    
    #Making random password
    for i in range(length-toggle):
        pwd.append(random.choice(chars))
    #Shuffling password    
    pwd_shuff = ""
    for i in range(length):
        n = random.randint(0,length-i)-1
        pwd_shuff += pwd[n]
        del(pwd[n])
    return pwd_shuff


def parameters():
    #Exception Handling format 
    while True:
        toggle = 0
        print("Enter the requirements of the password to be generated:")
        try:
            #Toggle for special characters
            special = input("Special characters in password(Y/N): ")
            if special.lower() == "y":
                special = True
                toggle += 1
            elif special.lower() == "n":
                special = False
            else:
                special = int("Invalid")
            #Toggle for numbers
            digits = input("Numbers in password(Y/N): ")
            if digits.lower() == "y":
                digits = True
                toggle += 1
            elif digits.lower() == "n":
                digits = False
            else:
                digits = int("Invalid")
            #Input Length of Password
            length = int(input("Enter length of password: "))
            if length < toggle+2: #To make sure all types are included
                print("Since Length of the password is too short,")
                length = int("Invalid")
        except ValueError:
            print("Invalid input")
            continue
        break
    return length, special, digits, toggle


def pwd_maker():
    while True:
        length, special, digits, toggle = parameters() #taking password criteria
        password = pwd_gen(length, special, digits, toggle+2) #generating password
        print(password) #asking user to keep the password or not
        keep = input("KEEP Password(Y/N): ")
        if keep.lower() == "y":
            caption = input("Enter a tag for password: ")
            break
    final_password = f"{caption} : {password}" #save format
    final_password = encrypt(final_password) #encryption
    with open(f"random_passwords.txt","a") as f:
        f.write(f"{final_password}\n") #storing excrpyted password
    print(f'"{decrypt(final_password)}" stored successfully!')


def pwd_display(): #displaying passwords
    with open("random_passwords.txt","r") as f:
        for line in f.readlines(): #taking single line from file
            line = line.replace("\n","")
            print(f"{decrypt(line)}") #printing decrypted line


def encrypt(string_sample): #base64 encryprion
    string_bytes = string_sample.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def decrypt(base64_string): #base64 decryption
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    string_sample = string_bytes.decode("ascii")
    return string_sample


def start():
    try:
        with open("master.txt","r") as f:
            master = []
            for line in f.readlines():
                master.append(decrypt(line))
            username = master[0].replace("\n","")
            master_password = master[1].replace("\n","")
            input_password = input(f"Enter password for {username} account: ")
            if master_password == input_password:
                return False, username
            else:
                print("Incorrect Password !")
                return True, username
    except FileNotFoundError:
        with open("master.txt","w") as f:
            username = input("Enter username: ")
            master_password = input("Enter password: ")
            f.write(f"{encrypt(username)}\n")
            f.write(encrypt(master_password))
            if os.path.exists("random_passwords.txt"):
                os.remove("random_passwords.txt")
        return False, username

run = True
while run:
    run, username = start()

while True:
    while True:
        try:
            u = int(input('''
Options:
1. Create and save a new password
2. Display all passwords
3. Save and Exit\n
>>> '''))
        except ValueError:
            print("Invalid Input")
            continue
        break
    if u==1:
        pwd_maker()
    elif u==2:
        pwd_display()
    elif u==3:
        quit()
    else:
        print("Invalid input")
