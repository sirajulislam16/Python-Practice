# Half pyramid pattern 
num = int(input("Enter your number: "))
# for i in range(1, num+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("")


#reversed pyramid
for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print("")