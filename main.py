import string
import random
import base64

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
        length, special, digits, toggle = parameters()
        password = pwd_gen(length, special, digits, toggle+2)
        print(password)
        keep = input("KEEP Password(Y/N): ")
        if keep.lower() == "y":
            caption = input("Enter a tag for password: ")
            break
    final_password = f"{caption}:{password}"
    final_password = encrypt(final_password)
    print(f'"{decrypt(final_password)}" stored successfully!')
    with open(f"{username}_passwords.txt","a") as f:
        f.write(f"{final_password}\n")


def encrypt(string_sample):
    string_bytes = string_sample.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def decrypt(base64_string):
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    string_sample = string_bytes.decode("ascii")
    return string_sample


def user():
    try:
        with open("username.txt","r") as f:
            username = decrypt(f.read())
    except FileNotFoundError:
        with open("username.txt","w") as f:
            username = input("Enter your username: ")

    with open("username.txt","w") as f:
        f.write(str(encrypt(username)))
    print(f"Welcome to the password manager {username}!")
    return username

username = user()
pwd = pwd_maker()
