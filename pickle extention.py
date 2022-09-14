import pickle
d = {}
with open("recordss.dat" , "wb") as  f :
    chh = "y"
    
    print("For Create = 1 ")
    print("For Display = 2 ")
    print("For Add = 3 ")
    print("For Search = 4 ")
    print("For Delete = 5 ")
    while True :
        chh = input("Kuch aur karna hai ?  : ")
        if chh == "n":
            break
        rec = (input("Enter your choice : "))
        
        ch = "y"
        while True :
            if rec == "1":
                def create():
                    
                    roll =int(input("Enter the roll no : "))
                    d[roll] = {}
                    name = input("Enter the name of the student : ")
                    per = float(input("Enter the percentage : "))
                    d[roll]["Name of the student : "] = name
                    d[roll]["Percentage of the student : "] = per
                    print(d)
                    pickle.dump(d, f)
                
                    
                create()
                ch = input("Wanna continue : ")
                if ch=="n":
                    break
       
            elif rec == "2" :
                def add():
                    
                    roll =int(input("Enter the roll no : "))
                    d[roll] = {}
                    name = input("Enter the name of the student : ")
                    per = float(input("Enter the percentage : "))
                    d[roll]["Name of the student : "] = name
                    d[roll]["Percentage of the student : "] = per
                    print(d)
                    pickle.dump(d, f)
                
                    
                add()
                ch = input("Wanna continue : ")
                if ch=="n":
                    break
                
            elif rec == "3" :
                s = int(input("Enter the roll no to be searched : "))
                
                def search(s):
                    
                    for i in d :
                       if s == i:
                           print(i , d[i])
                ch = input("Wanna continue : ")
                if ch=="n":
                    break
               
                search(s)    
                    
                    
                    
