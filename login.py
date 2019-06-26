from collections import defaultdict
from getpass import *

users = defaultdict(str)

def encrypt(password):
    encrypted = ""
    for letter in password:
        encrypted += str(hex(ord(letter))[2:])
    encrypted = int(encrypted, 16)
    return encrypted

logins = open("src/logins.csv", 'r')
lines = logins.read().split("\n")[:-1]
for line in lines:
    login = line.split(",")
    username = login[0].lower()
    password = login[1]
    users[username] = password
logins.close()

def login():
    username = raw_input("Enter your username:\n")
    user = username.lower()
    if user not in users:
        print "Welcome, " + username + ". It looks like you don't have an account. Let's register you for a new account."
        password = encrypt(raw_input("Enter a password for your account. To go back, type back.\n"))
        if password == encrypt("back") or password == encrypt("BACK"):
            login()
        else:
            users[user] = password
            newLogins = open("src/logins.csv", "w")
            for name in users:
                newLogins.write(name + "," + users[name] + ",\n")
            newLogins.close()
    else:
        while True:
            print "Welcome, " + username + "."
            password = encrypt(getpass(prompt="Please enter your password. To go back, type back.\n"))
            if password == encrypt("back") or password == encrypt("BACK"):
                login()
                break
            else:
                if password == users[user]:
                    print "Login successful!"
                    break
                else:
                    print "Password incorrect, please try again."
                    print

if __name__== "__main__":
    login()
