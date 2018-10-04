#Github Lab First program
''' Write a Python function to Return a list that contains the tuple (interfacename,"nameif"- value). Write a Python function called "list_ifname_ip" to scan the configuration and return a dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value'''

import string
interface=[]
nonames=[]
ipdetails=[]

def list_ifname_ip(filename):
    d=dict()
    myfile=open(filename)
    for line in myfile:
        lines=line.strip()
        lines=line.split()
        if(len(lines)>=2):
            if lines[0]==("interface"):
                interface.append(lines[1])
            elif lines[0]==("no") and lines[1]==("nameif"):
                ipdetails.append( "no-nameif")
                ipdetails.append( "no-vlan")
                ipdetails.append( "no-ip")
                ipdetails.append( "no-subnet")
            elif lines[0]==("nameif"):
                ipdetails.append(lines[1])   
            elif lines[0]==("vlan"):                 
                ipdetails.append(lines[1])
            elif lines[0]==("ip") and lines[1]==("address"):
                ipdetails.append(lines[2])
                ipdetails.append(lines[3]) 
    i=0
    j=4
    for x in range(len(interface)):
        empty=[]
        empty.append(ipdetails[i:j])
        d[interface[i]]=empty
        i+=4
        j+=4
    print(d)


list_ifname_ip("running-config.cfg")



