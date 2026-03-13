age = int(input("Enter your age:"))

if age <=12:
    ticket = 8000
elif age >= 13 <=59:
    ticket = 12000
elif age >= 60:
    ticket = 9000

print("Your ticket price is: ", ticket)