num = int(input("Enter the number: "))
count=0
if num>1:
    for i in range(1,num+1):
    # 1 theke num porjonto number diye num er modulous ber korbo
     if num%i == 0:
        count=count+1 
    if count == 2:
        print("It's a prime number",num)
    elif count !=2:
        print("It's a composite number", num)

elif num==1:
    print("1 is not a prime or composite number")
elif num<0:
    print("negative numbers are neither prime or composite.")