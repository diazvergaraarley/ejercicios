hours = int(input("Insert the ammount of hours the car was parked: "))
if hours <= 1:
    total = 5000
else:
    total = 5000 + (hours - 1) * 3000
print("Total to pay: ", total)