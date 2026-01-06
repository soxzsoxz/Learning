user_name = "soc"
user_age = 21

print(f"Hello my name is {user_name} I'm {user_age} years old")

#  input รับค่าเป็น string เสมอ
years_input = input("Enter your birth years : ")

#  แปลงค่าเป็น int
birth_years = int(years_input)
current_years = 2026
age = current_years - birth_years

print(f"You are {age} years old")
