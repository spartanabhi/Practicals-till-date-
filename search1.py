# a b c d hi x j i
a = open("india.txt" , "r")
b = a.read()
c = b.split()

print (b)
print (c)

hi = str(input("Enter word to search | "))

for i in c:
    if i == hi :
        print(i)
        d = i
        x= a.readlines()
        print (x)
        """for j in x :
            print (j)
            if (i in j == True):
                print(j)
            else :
                print(" ")
    else :
        print(" ")
"""
a.close()