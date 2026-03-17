

more_req = ""
max_serv = 0
total_day = 0
haircut= 0
total_hc= 0
brush= 0
total_brush=0
paint= 0
total_paint= 0

for i in range(7):
    name = input("Enter customer name: ")
    option = input("Enter requested service (a. cut, b. brush, c. paint): ").lower()
    if option == "a" or option == "cut":
        service = "Haircut"
        price = 40000
        haircut +=1
        total_hc+=price
    elif option == "b" or option == "brush": 
        service = "Hairbrush"
        price = 35000
        brush += 1
        total_brush += price
    elif option == "c" or option == "paint":
        service = "Hair Painting"
        price = 50000
        paint += 1
        total_paint += price

    total_day += price 

    print(f"""\n
    Customer name: {name}
    Your service: {service}
    Price: {price}
    """
    )

max_serv = haircut
more_req = "Haircut"
if brush > max_serv:
    more_req = "Hairbrush"
if paint > max_serv:
    more_req = "Hair Painting"


print(f"""\n
Total Haircut customers: {haircut}
{total_hc}
Total Hairbrush customers: {brush}
{total_brush}
Total Hair Painting customers: {paint}
{total_paint}
Most requested service today: {more_req}
Total sales today: {total_day}
"""
)
