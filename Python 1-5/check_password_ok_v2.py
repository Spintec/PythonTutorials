
def check_password(name,password,retries=2,reminder="Wrong credentials, please try again..."):
    while True:
        name = input("Name please: ")
        password = input("Password please: ")
        if name in ("Hesuus", "hesuus") and password == "gogul":
            print("Welcome back Hesuus ")
            break
        elif name in ("Hanuman", "hanuman") and password == "hua":
            print("Welcome back Hanuman")
            break
        retries = retries - 1
        if retries < 0:
            raise ValueError("Wrong credentials")
        print(reminder)
#check_password("Please enter your name: ","Please enter your password: ")
check_password("","")
