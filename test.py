f = open('test2.process','r')
l = f.readlines()
lines=[]
for i in l:
    lines.append(i.strip('\n'))

def writeFromInputFileToGUI(startCount,lengthCount,cType):
    for i in range(1,lengthCount):
        listLineStr = lines[startCount+i].split(',')
        if cType == 1:
            print(lines[startCount+i])
        elif cType == 2:
            listLineNumbers = lines[startCount+i].split('[', 1)[1].split(']')[0]
            print(listLineStr[0])
            print('Elm '+listLineNumbers.replace(',',''))
        elif cType == 3:
            print(listLineStr[0])
            print(listLineStr[1])
        elif cType == 4:
            print(listLineStr[0])
        elif cType == 5:
            print(listLineStr[0])
        
for count, line in enumerate(lines):
    #print(count,line)
    if line.startswith('# NASTRAN INPUT/OUTPUT FILES:'):
        a=count
    elif line.startswith('# GROUPS OF ELEMENTS INPUT:'):
        b=count
        writeFromInputFileToGUI(a,b-a,1)
    elif line.startswith('# COMPOSITE MATERIAL FACING INPUT:'):
        c=count
        writeFromInputFileToGUI(b,c-b,2)
    elif line.startswith('# COMPOSITE MATERIAL CORE INPUT:'):
        d=count
        writeFromInputFileToGUI(c,d-c,3)
    elif line.startswith('# METALLIC MATERIAL INPUT:'):
        e=count
        writeFromInputFileToGUI(d,e-d,4)
    elif line.startswith('# END'):
        f=count
        writeFromInputFileToGUI(e,f-e,5)
    else:
        pass    

# def writeNastranInputFiles(startCount,lengthCount):
#     for i in range(1,lengthCount):
#         print(lines[startCount+i])
