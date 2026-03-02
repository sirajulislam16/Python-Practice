def max(a,b):
    if a>b:
        return f"{a} is greater then your ex"
    else:
        return f"{b} is greater than your ex"

a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
print(max(a,b))