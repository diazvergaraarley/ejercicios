
low_commitment=0
mid_commitment=0
high_commitment=0

for customer in range(5):
    print(f"\n Customer {customer+1}: ")
    
    name = input("Enter your name: ")

    asisted_days = int(input("Enter the days asisted this week: "))

    avg_minutes = int(input("Enter the average of minutes per day: "))

    if asisted_days < 3:
        print("Low Commitment")
        low_commitment += 1
    elif 3 <= asisted_days <= 4:
        print("Mid Commitment")
        mid_commitment += 1
    elif asisted_days >= 5:
        print("High commitment")
        high_commitment += 1

print(f"""\n----Summary----
Low commitment people: {low_commitment}
Mid commitment people: {mid_commitment}
High commitment people: {high_commitment}
      ----"""
)