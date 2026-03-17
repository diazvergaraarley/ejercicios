
max_cat= 0
soldest= ""    
edibles = 0
toys = 0
accessories = 0


for i in range(10):
    
    category = input("Select the product category (a. accessory b. food, c. toy ): ")
    
    quantity= int(input("Enter the total purchase amount: "))
    
    if category== "a":
        accessories+= quantity 
    elif category== "b":
        edibles +=  quantity 
    elif category== "c":
        toys +=  quantity 
          
max_cat = edibles
soldest = "Food"

if toys > max_cat:
    max_cat = toys
    soldest = "Toys"

if accessories > max_cat:
    max_cat = accessories
    soldest = "Accessories"
        
print(f"""
      Total per category:
       
      Food: {edibles}
      Toys: {toys}
      Accessories: {accessories}
      
      Category with the most sales: {soldest}
      """
      )