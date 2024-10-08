students=[]

while True:
    roll=input("Enter roll number (or 'Complete' to finish) : ")
    if roll.lower()=='complete':
        break

    name=input("Enter name : ")
    marks=input("Enter marks : ")

    student = {
        'roll' : roll,
        'name' : name,
        'marks' : marks
    }

    students.append(student)
    print()


with open("Marks.data", 'w') as file:
    for student in students:
        file.write(f"{student['roll']},{student['name']},{student['marks']}\n")


print()
print("Records saved.")