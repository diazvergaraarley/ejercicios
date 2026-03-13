print("Menu:")
print("1. Coffe - 4000")
print("2. Tea - 3500")
print("3. Juice - 5000")

option = input("What drink do you wish today? : ").lower()

quantity= int(input("How many will you take? "))

if option == "1" or option == "coffe":
    drink = "Coffe"
    price = 4000
elif option == "2" or option == "tea": 
    drink = "Tea"
    price = 3500
elif option == "3" or option == "juice":
    drink = "Juice"
    price = 5000
else:
    print("Please insert one of the options.")

total = price * quantity

print(f"""
      
      Your drink: {drink}
      Quantity: {quantity}
      Total to pay: {total}
        """
      
      )