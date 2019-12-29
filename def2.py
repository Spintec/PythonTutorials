def cheeseshop(kind,*arguments,**keywords):
    print("Do you have any",kind,"sir?")
    print("I'm sorry, we're all out of ",kind)
    for arg in arguments:
        print(arg)
    print("-"*30)
    for kw in keywords:
        print(kw,":",keywords[kw])
cheeseshop("stinky cheese","It's stinking up our shop!!","arg2?",
           shopkeeper="Donald Trump",
           client="Donald Duck")
