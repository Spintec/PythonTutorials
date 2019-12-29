#testez modulul de hashlib SHA512
import hashlib

password=hashlib.md5("hristos".encode())
print(password.hexdigest())
#    print(password.hexdigest())