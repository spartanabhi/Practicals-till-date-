#import pickle
a = open("india.txt" , "r")
#d = a.read()
s = a.readlines()
b = list(s)
for i in (range(len(b)) ) :
   
    if b[i][0] == "A" :
        print("True")
        print(b[i])
    elif b[i][0] != "A" :
        print("False")
        print(b[i])