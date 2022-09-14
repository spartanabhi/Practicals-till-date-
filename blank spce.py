a = open("indiaa.txt" , "r")
b = a.read()
c = 0
d = [ ]
for i in b:
    if i==" ":
        c+=1
        d.append(i)
    else :
        continue
print(len(d))
#print(c)