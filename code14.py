a=input("enter side1:")
b=input("enter side2:")
c=input("enter side3:")
if a==b==c :
    print("equil triangle")
elif a==b or b==c or c==a :
    print("isoceles")
else:
    print("scalene")