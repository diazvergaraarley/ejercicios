vanilla = 0
chocolate = 0
strawberry = 0

for i in range(5): 
    flavor = input(f"Enter your Ice Cream Flavor (vainilla, chocolate, strawberry) #{i+1}: " )
    
    if flavor == "vainilla" :
        vanilla += 1
    elif flavor == "chocolate" :
        chocolate +=1 
    elif flavor == "strawberry":
        vanilla
    else:
        print("Invalid flavor")

print(f"""--------- 
Final results:
"Vainilla: " {vanilla},
"Chocolate: " {chocolate},
"Strawberry: " {strawberry}""")