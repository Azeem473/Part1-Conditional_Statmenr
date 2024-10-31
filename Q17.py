num=int(input("Enter any number: "))

if num % 2 == 0 :
    print(num,"is divisible by 2")
elif num % 3  == 0 :
    print(num,"is divisible by 3")
elif num % 2 == 0 or num % 3 == 0 :
    print(num,"is divisible by both")
else:
    print(num, "is not divisible by 2 and 3 or both")