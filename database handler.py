import getpass


def add():
    print 'add'
    if len(param)%2==0 and len(param)>0:
        print "good param"

        digest=parseParam(param)
        for element in digest:
            key = parsePlate(element[0])
            hand = filename(key)
            lines = getLines(hand)
            print lines
            lines.insert(1,element)
            print lines
            file = handle(hand, 'w')
            file.writelines(lines)
        return 0
    return 1



def parseParam(pa):
    n=len(pa)/2
    newline=[]
    for i in range (n):
        el1=pa[i*2]
        el2=pa[i*2+1]
        newline.append("{}:{}\n".format(el1,el2))
    return newline

def stop():
    pass

def remove():
    pass


def printOwner():
    pass


def help():

    if param=="":
        print("Command:")
        print("add\nrm\nprow\nhelp\nexit")
        print("help [command]\ninfo about command")

    else:
        man = {
               "add": "add [plate1] [owner1] [plate2] [owner2]...\nadd new data",
               "rm": "rm [plate1] [plate2]...\nremove some data",
               "prow": "prow [plate1] [plate2]\nprint the owner associated with a plate",
               "help":"help [command]", "exit": "no params"
               }
        if len(param)==1:
            if param[0] in man.keys():
                print man[param[0]]
            else:
                print "help:unknown command"
        else:
            print "more than one param supplied"


def find(plate,filename):
    lines=getLines(filename)
    flag=False
    for el in lines:
        par=el.split(":")
        if par[0]==plate:



def handle(name,mode):
    file=open(name,mode)
    return file

def parsePlate(plate):
    key=plate[0]
    return key

def getLines(filename):
    reader=handle(filename,'r')
    lines=reader.readlines()
    reader.close()
    return lines

def handleCommand(result):
    if result:
        print("bad command\nplease type help for more informations")


def filename(letter):
    alph = "abcdefghijklmnopqrstuvwxyz"
    name = "database/targhe"+letter.upper()+".json"
    return name


def parseCommand(command):
    setC=command.split(" ")
    if len(setC)>1:
        return (setC[0],setC[1:])
    else :
        return (setC[0],None)

keys={"add":add,"rm":remove,"prow":printOwner,"help":help,"exit":stop}
username=getpass.getuser()
param=0

while(True):
    command =raw_input(username+"@DataPlate:~$ ")
    cmd,param= parseCommand(command)
    if param==None:
        param=""
    if cmd in list(keys.keys()):
        handleCommand(keys[cmd]())

    else:
        print("unknown command")



exit(0)