f = open('test.process','r')
l = f.readlines()
lines=[]
for i in l:
    lines.append(i.strip('\n'))

def writeNastranInputFiles(startCount,lengthCount):
    for i in range(1,lengthCount):
        print(lines[startCount+i])

def writeGroupOfElements(startCount,lengthCount):
    for i in range(1,lengthCount):
        listLineStr = lines[startCount+i].split(',')
        listLineNumbers = lines[startCount+i].split('[', 1)[1].split(']')[0]
        
        print(listLineStr[0])
        print([int(s) for s in listLineNumbers.split(',')])

for count, line in enumerate(lines):
    #print(count,line)
    if line.startswith('# NASTRAN INPUT/OUTPUT FILES:'):
        a=count
    elif line.startswith('# GROUPS OF ELEMENTS INPUT:'):
        b=count
        writeNastranInputFiles(a,b-a)
    elif line.startswith('# COMPOSITE MATERIAL FACING INPUT:'):
        c=count
        writeGroupOfElements(b,c-b)
    elif line.startswith('# COMPOSITE MATERIAL CORE INPUT:'):
        d=count
        writeCompositeMatFacing(c,d-c)
    elif line.startswith('# METALLIC MATERIAL INPUT:'):
        e=count
        writeCompositeMatCore(d,e-d)
    elif line.startswith('# END'):
        f=count
        writeMetallicMat(e,f-e)
    else:
        pass    

# def writeNastranInputFiles(startCount,lengthCount):
#     for i in range(1,lengthCount):
#         print(lines[startCount+i])
