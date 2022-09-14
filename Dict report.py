d = {}
y = open("Siera.txt " , "w")

i = int(input("How many records you wanna enter : "))
for j in range(i):
    roll =int(input("Enter the roll no : "))
    d[roll] = {}
    name = input("Enter the name of the student : ")
    eng = int(input("English Marks : "))
    hind = int(input("Hindi Marks : "))
    math = int(input("Maths Marks : "))
    
    d[roll]["Name of the student : "] = name
    d[roll]["English marks : "] = eng
    d[roll]["Hindi marks : "] = hind
    d[roll]["Maths marks : "] = math
    y.write("\n*******************************************************************************")
    y.write("\nName of the student : ")
    y.write(name)
    y.write("\nRoll no : ")
    y.write(str(roll))
    y.write("\n##Marks scored ; subject wise## ")
    y.write("\nEnglish : ")
    y.write(str(eng))
    y.write("\nHindi : ")
    y.write(str(hind))
    y.write("\nMaths : ")
    y.write(str(math))
    s = (eng+hind+math)
    y.write("\nTotal Marks : ")
    y.write(str(s))
    y.write("\nAverage Marks : ")
    y.write(str(round(s/3,2)))
    p = round(s*100/60 , 2)
    y.write("\nPercentage : ")
    y.write(str(p))
    
    y.write("\n*******************************************************************************")
    
y.close()
print(d)