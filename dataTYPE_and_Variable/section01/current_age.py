import datetime
birth_year= int(input("Enter your birth year: "))
current_year= datetime.datetime.now().year
current_age= current_year-birth_year
print(current_age)
