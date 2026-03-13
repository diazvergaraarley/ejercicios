prices =[]

for i in range(6):
    price =int(input(f"Enter the price for product {i+1}: $"))
    prices.append(price)

exp_count = 0

for price in prices:
    if price > 100000:
        exp_count += 1

print(f"There are {exp_count} products that cost more than $100.000")