def ask_ok(prompt,retries=4,reminder="Please try again!"):
    while True:
        ok=input(prompt)
        if ok in ('yes','ye','y'):
            return True
        if ok in ('no','nope','nah','n'):
            return False
        retries=retries-1
        if retries == 0:
            raise ValueError("Invalid user response")
        print(reminder)

ask_ok("Is this what you were looking for?",2,"'Da fuck, man?")