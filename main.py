import string
import random
import base64
import os
import UI


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
        toggle = 0 #a variable to set characterset
        try:
            #Toggle for special characters
            special, digits, length = UI.parameters_UI()
            if special:
                toggle += 1
            if digits:
                toggle += 1
            length = int(length)
            if length <= toggle+2 or length > 20: #To make sure all types are included
                length = int("Invalid")
        except ValueError:
            UI.invalid_UI()
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
    os.system("attrib -h random_passwords.txt")
    with open(f"random_passwords.txt","a") as f:
        f.write(f"{final_password}\n") #storing excrpyted password
    os.system("attrib +h random_passwords.txt")
    print(f'"{decrypt(final_password)}" stored successfully!')


def pwd_display(): #displaying passwords
    try:
        caption, password = [], []
        with open("random_passwords.txt","r") as f:
            for line in f.readlines(): #taking single line from file
                line = line.replace("\n","")
                line = decrypt(line)
                contents = line.split(":")
                caption.append(contents[0])
                password.append(contents[1])
        UI.pwd_display_UI(caption, password)
    except FileNotFoundError:
        UI.invalid_UI()


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
            try:
                username = master[0].replace("\n","")
                master_password = master[1].replace("\n","")
            except IndexError: #incase master file contents were deleted
                print("Master file was tampered with!\nDeleting passwords...")
                os.remove("random_passwords.txt")
                os.remove("master.txt")
                quit() 
            while True:
                try:
                    input_username, input_password = UI.master_UI()
                except NameError:
                    quit()
                break
            if master_password == input_password and username == input_username:  
                return False, username
            else: #input password is not the same as master
                print("Incorrect Password !")
                return True, username
    except FileNotFoundError:
        with open("master.txt","w") as f: #on first boot/ master file was deleted
            username, master_password = UI.master_UI()
            f.write(f"{encrypt(username)}\n") #write username
            f.write(encrypt(master_password)) #write password
            os.system("attrib +h master.txt") #hides master file
            if os.path.exists("random_passwords.txt"): #incase master file was deleted
                os.remove("random_passwords.txt") #passwords will be deleted 
        return False, username
        

run = True
while run:
    run, username = start()

while True:
    while True:
        try:
            u = UI.display_UI()
        except NameError:
            print("Have a good day!")
            quit()
        break
    if u==1:
        pwd_maker()
    elif u==2:
        pwd_display()
    elif u==3:
        print("Have a good day!")
        quit()
