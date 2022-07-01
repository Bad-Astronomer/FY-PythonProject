import string
import random

def pwd_gen(length, special, digits, toggle):
    pwd= []
    #Entire character set
    chars = "".join(string.ascii_letters)
    if digits: #toggle for digits
        chars = chars.join(string.digits)
        pwd.append(random.choice(string.digits))
    if special: #toggle for special characters
        chars = chars.join("!@#$%^&*?.,_")
        pwd.append(random.choice("!@#$%^&*?.,_"))
    pwd.append(random.choice(string.ascii_uppercase)) #picking one uppercase letter
    pwd.append(random.choice(string.ascii_lowercase)) #picking one lowercase letter
    
    #Making random password
    for i in range(length-toggle):
        pwd.append(random.choice(chars))
    #Shuffling password    
    pwd_shuff = ""
    for i in range(length):
        n = random.randint(1,length-i)-1
        pwd_shuff += pwd[n]
        del(pwd[n])
    print(pwd_shuff)


#Exception Handling format 
while True:
    toggle = 2
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
        if length <= toggle: #To make sure all types are included
            print("Since Length of the password is too short,")
            length = int("Invalid")
    except ValueError:
        print("Invalid input")
        continue
    break

#Calling password generator function
pwd_gen(length, special, digits, toggle)
