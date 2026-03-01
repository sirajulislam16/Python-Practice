correct_username= "admin"
correct_pssword = "01642"
user_username = input("Enter your username: ")
user_pass = input("Enter your password: ")

if user_username==correct_username and user_pass==correct_pssword:
    print("Loging Successfully")
elif user_username==correct_username and user_pass!=correct_pssword:
    print("Password is invalid")
elif user_username!=correct_username and user_pass== correct_pssword:
    print("Username is wrong")
elif user_username!=correct_username and user_pass!=correct_pssword:
    print("Username and User Password are wrong")

