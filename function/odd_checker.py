def even_odd(num):
    if num%2==0:
        return"It is an even number"
    elif num==0:
        return"Zero isn't an even or odd"
    else:
        return"It is an odd number"

num=int(input("Enter your number: "))
print(even_odd(num))