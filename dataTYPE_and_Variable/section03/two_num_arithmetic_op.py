a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

c= input("What do you want? + , - ,* , /, **, //: ")
if c== "+":
    print("Addition of your numbers is: ",a+b)
elif c == "-":
    print("Subtraction of your numbers is: ", a-b)
elif c == "*":
    print("Multiplication of your numbers is: ", a*b)
elif c == "/":
    if b == 0:
        print("Unidentified")
    else:
        print("Division of your numbers is: ", a/b)
elif c =="%":
    if b == 0:
        print("Unidentified")
    else:
        print("Modulous of your numbers is: ", a%b)
elif c == "**":
    print("Exponent of your numbres is: ", a**b)
elif c == "//":
    print("Floor division of your numbers is: ", a//b)
