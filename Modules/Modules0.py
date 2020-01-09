#I need to add python path sys.path.insert in order to run it
import sys,os
print(sys.path[1])
sys.path.append(os.path.join(sys.path[1],'Python 1-5'))
import ask_ok

print(ask_ok.__name__)
