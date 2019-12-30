#from passwd import users
#from passwd import passwords
from passwd import upass
#functia check_sec
def check_sec(name,password):
    while True:
        user = input(name)
        userpasswd = input(password)

        if user in upass:
            if userpasswd==(upass[user]):
                print("Welcome, ",user)
                break
            print("One more chance to get this right...")
        else:
            print("Fuck off and/or die")
            break

#check_sec("Please enter your name: ","Please enter your password: ")













#RUN IT!
