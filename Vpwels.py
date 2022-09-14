a = open("india.txt" , "r")
b = a.read()
y = list(b)
c = 0
for i in y:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
        c+=1
        
print("No of vowels : " , (c))
a.close()