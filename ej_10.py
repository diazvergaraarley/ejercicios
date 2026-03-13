
attendance =int(input("Please enter the student's presences this month: "))

if 0<= attendance <= 5:
    print("Low attendance")
elif 6<= attendance <= 8:
    print("Mid attendance")

elif 9<= attendance <=30:
    print("High attendance")
else:
    print("Invalid input, please enter a number between 1 & 31")