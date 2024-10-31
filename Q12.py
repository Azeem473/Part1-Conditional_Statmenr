temp = int(input("Enter temprature: "))

if temp <= 0 :
    print(f"Tempreature is {temp}*C. IT is  freezing outside")
elif temp < 0 and temp >= 30:
    print(f"Tempreature is {temp}*C. IT is  moderate outside")
else:
    print(f"Tempreature is {temp}*C. IT is  hot outside")