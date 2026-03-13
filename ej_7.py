time = int(input("Enter the arrival time 0-23: "))

if 6 <= time <=11:
   print("Morning"),
elif 12 <= time <=17:
    print("Afternoon"),
elif 18 <= time <=22:
    print("Night")
else:
    print("Out Of Time")