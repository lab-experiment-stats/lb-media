import os, json
def alljsontoone():
    a = []
    for i in range(len(os.listdir(r"D:\ShrekJSON"))):
        print(i)
        with open(r"D:\ShrekJSON"+chr(92)+"frame"+str(i)+".json","r") as f:
            b = json.load(f)
            c = []
            for x in b:
                a.append(x["type"])
                for y in x["data"]:
                    a.append(y)
                a.append(x["color"][0])
                a.append(x["color"][1])
                a.append(x["color"][2])

    with open(r"D:\FinalJson.json","w") as f:
        json.dump(a,f)

def indexList():
    b = [] 
    for i in range(32,48):
        b.append(chr(i))
    for i in range(58,127):
        b.append(chr(i))
    for n in range(ord("0"),ord("9")+1):
        for i in range(32,48):
            b.append(str(chr(n))+chr(i))
        for i in range(58,127):
            b.append(str(chr(n))+chr(i))
    return b

def getSortedValues():
    a = {}
    index = indexList()
    indexIndex = []
    indexIndexQ = {}
    final = ""
    with open(r"D:\FinalJson.json","r",encoding="UTF-8") as f:
        b = json.load(f)
        for x in b:
            if x in a:
                a[x] += 1
            else:
                a[x] = 1
    d = sorted(a.items(), key=lambda x: x[1], reverse=True)
    aba = 0
    print(len(d),len(index))
    for x in d:
        indexIndexQ[x[0]] = index[aba]
        indexIndex.append([index[aba],x[0]])
        aba+=1
    print(indexIndex)
    for x in b:
        final += str(indexIndexQ[x])
    print(len(final))
    with open(r"D:\FinalJson.json","w",encoding="UTF-8") as f:
        f.write(final)
    with open(r"D:\FinalJson_INDEX.txt","w",encoding="UTF-8") as f:
        indexIndexW = ""
        for i in indexIndex:
            indexIndexW+=str(i[1])+","

        f.write(indexIndexW)


alljsontoone()
getSortedValues()