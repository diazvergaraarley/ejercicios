print(f"""
Choose your pet type:
       
1. Dog
2. Cat
3. Rabit
"""
)

option = int(input("Enter an option to Choose your Pet Type: "))
if option == 1:
    pet_type= "Dog"
    print("The recommended food for your", pet_type, "is Chicken")
elif option == 2:
    pet_type= "Cat"
    print("The recommended food for your", pet_type, "is Fish")
elif option == 3:
    pet_type= "Rabit"
    print("The recommended food for your", pet_type, "is Carrot")
else:
    print("Invalid option")