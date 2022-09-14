a = open("indiaa.txt" , "r")
b = a.read()
c = list(b)

s = input("Enter the character to replace : ")
def replace(s):
    y = open("indiaa.txt " , "w")
    for i in range (len(c)) :
        if c[i] == s :
            c[i] = "#"
            print(i)
        
        y.write(c[i])
    y.close()

           
           
replace(s)
print(c)
