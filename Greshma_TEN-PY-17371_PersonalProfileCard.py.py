# Task 1 - Personal Profile Card

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
favourite_subject = input("Enter your favourite subject: ")

birth_year = 2024 - age

print("\n")
print("=" * 35)
print("       🪪  PERSONAL PROFILE CARD")
print("=" * 35)
print(f"  Name            : {name}")
print(f"  Age             : {age}")
print(f"  Birth Year      : {birth_year}")
print(f"  City            : {city}")
print(f"  Favourite Subject: {favourite_subject}")
print("=" * 35)
