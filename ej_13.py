
prices= {
    "coffe": 4000,
    "capuccino": 7000,
    "pie": 6000
}

total_sold = 0

while True:
    print("---New Customer---")
    product = input("Enter the product (coffe/capuccino/pie) or type'exit' to end the program: ")

    if product == "exit":
        break

    quantity = int(input("Enter the quantity: "))
    
    total_customer = prices[product] * quantity

    if total_customer > 20000:
        discount = total_customer * 0.1
    else:
        discount = 0
    
    total__to_pay = total_customer - discount

    print(f"Total customer: {total__to_pay}")
    
    total_sold += total__to_pay

total_sold += total__to_pay

print("Total Sold: ", total_sold)
