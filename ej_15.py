
cars = 0
motorcycle = 0
max_paid = 0
max_plate = ""
total_paid = 0
i = 0
for i in range(3):
    plate = input(f"Enter de vehicle's plate {i+1}: ")
    v_clas= input("Enter the type of vehicle (moto/car): ").lower()
    if v_clas == "car":
        cars += 1
        price = 4000
    elif v_clas == "moto":
        motorcycle += 1
        price = 2000
        
    hours = int(input("Enter the ammount of hours parked: "))
    quantity = price * hours
    if quantity > max_paid:
        max_paid = quantity
        max_plate = plate
    print(f"Total to pay: {quantity}")
    total_paid += quantity

print(f"Total Motorcycles: {motorcycle}")
print(f"Total Cars: {cars}")
print(f"Total collected: {total_paid}")
print(f"VTPM: {max_plate}")
print(f"Max Paid: {max_paidasas}")