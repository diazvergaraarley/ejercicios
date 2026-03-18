
students = []

n = int(input("¿How many Students are you registering? "))

for i in range(n):
    student= {}
    name= input(f"Enter the name for student {i+1}: ")
    student["name"]= name
    speaking= float(input("Speaking note: "))
    reading= float(input("Reading note: "))
    listening = float(input("Listening note: "))
    student["speaking"] = speaking
    student["listening"] = listening
    student["reading"] = reading
    average = (speaking + listening + reading) / 3
    student["average"] = average
    if average < 60:
        level = "Low"
    elif average <= 79:
        level = "Mid"
    else:
        level = "High"
    student["level"] = level
    students.append(student)
total= 0
for student in students:
    total += student["average"]

grup_average= total /len(students)

best_student= students[0]
for student in students:
    if student["average"] > best_student["average"]:
        best_student = student
low = 0
medium = 0
high = 0

for student in students:
    if student["level"] == "Low":
        low += 1
    elif student["level"] == "Mid":
        medium += 1
    else:
        high += 1
        
        
print(f"""\n
      Group Average: {grup_average: .2f}
      Best Student: {best_student["name"]}
      
      Students in Low Level: {low}
      Students in Mid Level: {medium}
      Students in High Level: {high}
      """
      )