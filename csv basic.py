import csv
f = open("data.csv" , "w", newline = "")
x = csv.writer(f)
x.writerows(["rollno" , "Name" , "per"])
a = [ ]
while True :
    rollno = int(input("enter the roll no : "))
    Name = input("Enter name : ")
    per = float(input("Enter Percentage : "))
    d =  [rollno , Name , per]
    a.append(d)
    ch = input("Y/N : ")
    if ch == "n":
        break
x.writerows(a)
f.close()    

