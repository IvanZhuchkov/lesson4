n=input("Enter number: ")
m=(("."in n) and "number is float") or "number is int"
print(m)
print("number is negative" if "-" in n else "number is positive")
n=float(n)
if n:
    pass
else:
    print( "number is zero")