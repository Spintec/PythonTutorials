#caz:
#am un positional argument name si un keyword argument
#keyword arguments cu 2x * (exemplu: def function(**args) is practic ca un dictonar,
#iar daca keyword-ul dictionarului coincide deja cu numele unui argument,
#voi primi eroarea ce o returneaza programul daca il rulez.


def foo(name, **kwds):
    return 'name' in kwds
foo("first Name",
    name="Jesus")
