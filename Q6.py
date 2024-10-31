n1 = int(input("Enter first number: "))
n2 = int(input("Enter 2nd number: "))

if n1 > n2:
    print(n1, "is larger than", n2)
elif n2 > n1:
    print(n2, "is larger than", n1)
else:
    print(n1,"is Equal to", n2)