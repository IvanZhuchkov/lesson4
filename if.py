n=input("Enter number: ")
try:
    if "." in n:
        n=float(n)
        print("%f is float" %n)
        if n<0:
            print("%f is negative" %n)
        elif n>0:
            print("%f is positive" %n)
        else:
            print("This is 0")
    else:
        n=int(n)
        print("%d is int" %n)
        if n<0:
            print("%d is negative" %n)
        elif n>0:
            print("%d is positive" %n)
        else:
            print("This is 0")
except:    
    print ("Enter is not correct")
print()