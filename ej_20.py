

total = 0

basic = 0
premium = 0
family = 0
register = ""
price = 0
more_req = ""
max_serv = 0

n = int(input("¿How many Users are you registering? "))

for i in range(n):
    name = input(f"Enter the name for Customer {i+1}: ")
    age = int(input("Enter the Customer age: "))
    if age < 18:
        register = "Junior Registration"
    elif age > 59:
        register = "Senior Registration"
    else:
        register = "Regular Registration"
    print("\n Registration type: ", register)

    plan = input(f"""\n Plans:  \n 1. Basic \n 2. Premium \n 3. Family \n \nPlease select your plan: """).lower()
    if plan == "1" or plan == "basic":
        price = 50000
        basic+= 1
        print("Plan you selected: Basic")
    elif plan == "2" or plan == "premium":
        price = 90000
        premium += 1
        print("Plan you selected: Premium")
    elif plan == "3" or plan == "family":
        price = 130000
        family += 1
        print("Plan you selected: Family")
    
    total += price
    print("Price: ", price)
    print("\n")
    
max_serv = basic
more_req = "Basic Plan"
if max_serv < premium:
    more_req = "Premium Plan"
if max_serv < family:
    more_req = "Family Plan"
print("\n")
print("Total Sold: ", total)
print("Total Basic Plan Customer: ", basic)
print("Total Premium Plan Customer: ", premium)
print("Total Family Plan Customer: ", family)
print("Most Requested Plan: ", more_req)