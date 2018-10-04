#Github Lab First program
import string
interface=[]
nonames=[]
task1=[]
zipped=[]
def openfile(filename):
    myfile=open(filename)
    for line in myfile:
        lines=line.split()
        if(len(lines)>=2):
            if lines[0]==("interface"):
                interface.append(lines[1])
            if lines[0]==("no") and lines[1]==("nameif"):
                nonames.append( "no-nameif")
            elif lines[0]==("nameif"):
                nonames.append(lines[1])   
    for i in range(len(interface)-1):
        task1.append((interface[i],nonames[i]))
#    zipped=zip(list_of_interface,list_of_nonames)
#    print(zipped)
    print(task1)   

   # zipped=zip(list_of_tuples[0::2],list_of_tuples[1::2])
openfile("running-config.cfg")



