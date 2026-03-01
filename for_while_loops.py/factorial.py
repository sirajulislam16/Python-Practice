num = int(input("Enter your number: "))
fatcorial=1
for i in range(1,num+1):
    fatcorial=fatcorial*i
    i = i+1
print(f"Factorial of {num} is ",fatcorial )