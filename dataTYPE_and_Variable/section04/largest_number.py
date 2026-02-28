num_1=int(input("Number 1 : "))
num_2=int(input("Number 2 : "))
num_3=int(input("Number 3 : "))

if num_1> num_2 and num_1>num_3:
    print(num_1, "is largest")
elif num_2>num_1 and num_2>num_3:
    print(num_2, "is largest")
else:
    print(num_3,"is largest")