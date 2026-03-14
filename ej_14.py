
capacity = int(input("Please enter the Theater Capacity: "))

total_people = 0
children = 0
adults = 0
senior_adults = 0
for i in range(capacity):

    user_input = input("Please insert customer age (or write 'exit' to finish): ")

    if user_input =="exit":
        break

    try:        
        age = int(user_input)
        
        if 0 < age < 18:
            print("Customer belongs to Children category.")
            children +=1
            total_people += 1
            
        elif 18<= age <= 64:
            print("Customer belongs to Adults category.")
            adults += 1
            total_people += 1
            
        elif age >64:
            print("Customer belongs to Senior Adults category.")
            senior_adults += 1
            total_people += 1
            
        else:
            print("Enter a valid number.")
            
    except ValueError:
        print("Invalid input, must be a number")
        

    
remaining_seats = capacity - total_people
    
print(f"""\n
Total Children: {children}
Total Adults: {adults}
Total Senior Adults: {senior_adults}
Total people: {total_people}
"""
)
if total_people == capacity:
    print("Theater is full")
else:
    print(f"There are {remaining_seats} remaining seats.")