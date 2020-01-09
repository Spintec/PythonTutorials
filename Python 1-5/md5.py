#Exercitiu MD5

import hashlib,os,binascii

#Function that adds salt to a password before hashing it with sha256
def hash_salt(password):
    salt=hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    pwdhash=binascii.hexlify(pwdhash)
    return (salt+pwdhash).decode('ascii')





