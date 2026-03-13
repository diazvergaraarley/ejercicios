prices = {
    "cone": 3000, 
    "cup": 4000, 
    "banana split": 9000
}

total_sold = 0

cust_handled = 0

sales =  {
    "cone": 0, 
    "cup": 0, 
    "banana split": 0
}


while True:
    print("\n---New Customer---")
    product = input("Enter the product (cone/cup/banana split) or type'exit' to end the program: ")
    
    if product == "exit":
        break
    
    if product not in prices:
        print("Invalid product. Try again. ")
        continue
    
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            print("invalid input. Try again.")
            continue
         
    except ValueError:
        print("Invalid input, Try again. ")
        continue
    
    
    total_customer = 0
    total_customer += prices[product] * quantity

    total_customer += prices[product] *quantity
    print (f"Total Customer: {total_customer}")
    
    total_sold += total_customer
    sales[product] += quantity
    cust_handled += 1
    
print("\n ---Sumary---")
print(f"Total sold: {total_sold}")
print(f"Customer handled: {cust_handled}")

most_sold_product = max(sales, key= sales.get)
print(f"Most requested product: {most_sold_product} ({sales[most_sold_product]}) units")
