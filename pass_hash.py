import random
def hashof(s) :
    hash = 0
    n = len(s)
    for i in range(n) :
        curr = ord(s[i])
        for j in range(i+1, n) :
            x = ord(s[j])
            hash += (curr)*37 - (x % curr)*29
    return hash

def salt() :
    s = ""
    for i in range(7) :
        ch = chr(random.randint(ord('a'), ord('z')))
        s += ch
    return s

user_pass = {}
saltof = {}
while(1) :
    num = int(input("1 for signup / 2 for login : "))
    if(num == 1) :
        username = input("Enter mail id : ")
        passw = input("Create pass : ")
        passhash = hashof(passw)
        saltof[username] = salt()
        user_pass[username] = saltof[username] + str(passhash)
    else :
        username = input("Enter mail id : ")
        passw = input("Enter your pass : ")
        passhash = saltof[username] + str(hashof(passw))
        if(passhash == user_pass[username]) :
            print("Welcome!!!")
        else :
            print("Wrong password!!!")
