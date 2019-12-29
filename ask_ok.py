def ask_ok(prompt, retries=2,reminder="Please try again"):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
#            print("Your answer was yes!")
            return True
        if ok in ('n','no','nop','nope'):
#            print("Your answer was no")
            return False
        retries=retries-1
        if retries<0:
           raise ValueError('invalid user reponse')
        print(reminder)