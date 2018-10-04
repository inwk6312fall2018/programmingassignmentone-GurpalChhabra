#Github Lab First program
''' Write a Python function to create a new configuration file that replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." and also change the security-level to "10"'''

import string
interface=[]
nonames=[]
ipdetails=[]

def replace_172(filename):
    myfile=open(filename)
    for line in myfile:
        lines=line.replace("172","10")
        final=lines.replace("192","10")
        print(final)


replace_172("running-config.cfg")



