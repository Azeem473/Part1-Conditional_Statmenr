n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2 and n1 > n3:
    print(n1, "is larger than", n2,"and","is larger than",n3)
elif n2 > n3 and n2 > n1 :
    print(n2, "is larger than", n3,"and","is larger than",n1)
elif n3 > n1 and n3 > n2 :
    print(n3, "is larger than", n1, "and","is larger than",n2)
