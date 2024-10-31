marks = int(input("Enter Your Marks: "))

if marks >=90:
    print("You got A grade with", marks,"% marks")
elif marks < 90 and marks >=80:
    print("You got B grade with", marks,"% marks")
elif marks < 80 and marks >=65:
    print("You got C grade with", marks,"% marks")
elif marks < 65 and marks >=35:
    print("You got D grade with", marks,"% marks")
else:
    print("You got F grade with", marks,"% marks")