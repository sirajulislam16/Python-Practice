def calc(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            return "Math Error"
        else:
            return num1/num2
    elif operator=="**":
        return num1**num2
    elif operator=="%":
        if num2==0:
            return "Undefined operation"
        else:
            return num1%num2
        
num1= int(input("Enter your first number: "))
operator= input("Enter your operator: ")
num2= int(input("Enter your second number: "))

print(calc(num1,num2,operator))