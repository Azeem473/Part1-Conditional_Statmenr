side1 = int(input("Enter the first side of triange: "))
side2 = int(input("Enter the second side of triange: "))
side3 = int(input("Enter the third side of triange: "))

if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("It is valid triange")
else:
    print("Non-valid triange")