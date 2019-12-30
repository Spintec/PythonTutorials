#cand nu stii cate argumente vrei sa dai pentru o functie se folosesc keyword only arguments like so:
#Arbitrary argument lists
def concatt(*args,separatorr="/"):
    return separatorr.join(args)

print(concatt("luni","marti","miercuri","joi"))

print(concatt("luni","marti","miercuri","joi",separatorr="//"))

print(concatt("luni","marti","miercuri","joi",separatorr="/:/"))

#Normal call with separate arguments
print(list(range(3,6)),"<-- Normal call with separate arguments")

#Unpacking argument lists

args=[3,6]
print(list(range(*args)),"<-- Unpacking argument list")

def parrot(volts,state="a stiff",action="VOOM!"):
    print("This parrot wouldn't",action )
    print("if you put",volts,"volts throught it")
    print("He'd be",state)

pdic={"volts":"10000","state":"DEAD!","action":"flying around"}
parrot(**pdic)