

def ask_ok(prompt,retries=3,reminder="Please try again"):
    while True:
        ok=input(prompt)
        if ok in ("yes"):
            print("yes")
            break
        elif ok in ("no"):
            print("no")
            break
        retries=retries-1

        if retries == 0:
            print("End of program")
        else:
            print(reminder, "you have",retries, " more tries")



ask_ok("Yes or no?")