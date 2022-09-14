import mysql.connector as conn

con = conn.connect(host = "localhost" , user = "root" , password = "" , database = "mydatabase")
if con.is_connected():
    print("Established")
else :
    print("Failed")

cur = con.cursor()
'''
x = "Create Database mydatabase"
cur.execute(x)'''
'''
x = "Use mydatabase"
cur.execute(x) '''


#x = '''Create table spartan
#       (Sn int , Sname varchar(19), per float(3))'''
#cur.execute(x)

while True :
    print("0. Create Records ")
    print("1. Add Records")
    print("2. Search Records")
    print("3. Update Records")
    print("4. Delete Records")
    print("5. Display Records")
    chh = input("Wanna initialize : ")
    if chh == "n":
        break
    rec = int(input("Enter your choice : "))
    if rec == 0:
        s = int(input("How many rec u wanna enter : "))
        for i in range(s):
            r  = int(input("Rollno : "))
            n  = (input("Name : "))
            p  = float(input("Per : "))
            cur.execute("Insert into spartan values ({}, '{}', {})".format(r,n,p))
            con.commit()
            print(" ")

    elif rec == 1 :
        s = int(input("How many rec u wanna add : "))
        for i in range(s):
            r  = int(input("Rollno : "))
            n  = (input("Name : "))
            p  = float(input("Per : "))
            cur.execute("Insert into spartan values ({}, '{}', {})".format(r,n,p))
            con.commit()
            print(" ")
   
    elif rec == 2 :
         s = int(input("Enter the roll to be searched  : "))
         
         x= "select * from Spartan where Sn = %s"  %(s,)
         cur.execute(x)
         data = cur.fetchall()
         for i in data :
             print(i)
             
    elif rec == 3 :
        s = int(input("Enter the roll to be Updated : "))
        print("1. Name ")
        print("2. Percentage  ")
        
        c = int(input("Enter your choice : "))
        chh = "y"
        while True : 
            if c == 1:
                namee = input("Enter the new name : ")
                x = "Update Spartan set Sname = '%s' where Sn = %s " %(namee , s)
                cur.execute(x)
                con.commit()
                cur.execute("Select * from Spartan")
                data = cur.fetchall()
                for i in data :
                    print(i)
            elif c == 2 :
                pere = float(input("Enter the new per : "))
                x = "Update Spartan set per = %s where Sn = %s " %(pere , s)
                cur.execute(x)
                con.commit()
                
                cur.execute("Select * from Spartan")
                
                
                chh = input("Wanna continue : ")
                if chh == "n":
                    break
    elif rec == 4 :
        s = int(input("Enter the roll to be Deleted : "))
        x = "Delete from Spartan where Sn=%s" %(s)
        cur.execute(x)
        con.commit()
        cur.execute("Select * from Spartan")
        data = cur.fetchall()
    elif rec == 5 :
        print("1. All records")
        print("2. Specific record")
        a = int(input("enter your choice : "))
        if a == 1:
            x = "Select * from spartan"
            cur.execute(x)
            data = cur.fetchall()
            for i in data :
                print(i)
       
        elif a == 2 :
           
         s = int(input("Enter the roll to be searched  : "))
     
         x= "select * from Spartan where Sn = %s"  %(s,)
         cur.execute(x)
         data = cur.fetchall()
         for i in data :
             print(i)
                

        

con.close()








