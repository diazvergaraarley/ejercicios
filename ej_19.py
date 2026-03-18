

out_of_stock = 0
low_stock = 0
regular_stock= 0

for i in range(7):
    product= input(f"Enter the name for product {i+1}: ")
    stock= int(input("Enter the available stock: "))
    if stock == 0:
        out_of_stock += 1
    elif 1 <= stock <= 5:
        low_stock += 1
    elif stock >= 6:
        regular_stock += 1

print(f"""\n
      Out of Stock Products: {out_of_stock}
      Low Stock Products: {low_stock}
      Products with Normal Stock: {regular_stock}
"""
)