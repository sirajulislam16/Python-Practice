import random #this module help to create random number

# computer gussing number
system_num=random.randint(1,11) # you need random number between 1 to 10
count= 0

while True:
    user_num= int(input("Enter your number: ")) #user input
    count = count+1 #it couts how many time you have tried

    if user_num==system_num:
        print(f"You are right lady boy.\nYou have taken {count} times to be correct")
        break
    elif user_num>system_num:
        print("Beshi boro cinta koris na")
        
    elif user_num<system_num:
        print("Why do you think so small? You cheap...")
        
    