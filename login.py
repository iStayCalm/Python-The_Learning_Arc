username = "saadisCalm@69"
password = "Calmgoesbrrr@123"

def enterinfo():
    global tuser,tpass
    tuser = input("Enter Username : ")
    tpass = input("Enter Password : ")

enterinfo()

while True:

    if tuser == username and tpass == password:
        print("Logged into Python :) ")
        break
    else:
        print(f"Username or Password incorrect, Please Try again\n")
        enterinfo()