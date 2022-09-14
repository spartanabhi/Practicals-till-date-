a = open("indiaa.txt" , "r")
b = a.read()
c = b.split()

s = input("Enter the word to find : ")
def search(s):
    for i in c :
       
       if i==s:
            
            print(i)
            print(c.count(i))
            print("yess")
            break
      
search(s)


