def volum(lungime,latime,inaltime,/):
    vol=lungime*latime*inaltime
    print(vol)
volum(30,30,40)

def keyword_only_arguments(*,arg1):
    print(arg1)
keyword_only_arguments(arg1="The Keyword!!!!")
