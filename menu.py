s="""           Main Menu
       Please, select file:
1) Lesson1.py
2) Project.cpp
3) Ivan.mai
4)Exit"""
print(s)
n=input()
if n=="1":
    print("Opening \"Lesson1.py\"...")
elif n=="2": 
    print("Opening \"Project.cpp\"...")
elif n=="3":
    print("Opening \"Ivan.mai\"...")
else:
    print("Closing...")