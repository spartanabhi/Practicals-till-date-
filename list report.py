l = []
y = open("list.txt " , "w")
i = int(input("How many records you wanna enter : "))
for j in range(i):
   
    name = input("Name of the Student : ")
    rno = int(input("Enter the roll no : "))
    eng = int(input("English : "))
    hind = int(input("Hind : "))
    sst = int(input("Social science : "))
    l.append(name)
    l.append(rno)
    l.append(eng)
    l.append(hind)
    l.append(sst)
    y.write("\n*******************************************************************************")
    y.write("\nName of the student : ")
    y.write(name)
    y.write("\nRoll no : ")
    y.write(str(rno))
    y.write("\n##Marks scored ; subject wise## ")
    y.write("\nEnglish : ")
    y.write(str(eng))
    y.write("\nHindi : ")
    y.write(str(hind))
    y.write("\nSocial Science : ")
    y.write(str(sst))
    s = (eng+hind+sst)
    y.write("\nTotal Marks : ")
    y.write(str(s))
    y.write("\nAverage Marks : ")
    y.write(str(round(s/3,2)))
    p = round(s*100/60 , 2)
    y.write("\nPercentage : ")
    y.write(str(p))
    
    y.write("\n*******************************************************************************")
   

y.close()    

    