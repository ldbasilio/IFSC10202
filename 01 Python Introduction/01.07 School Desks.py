print ("Please enter the # of students for 3 different classrooms :)")

desk = int(2)

classA = int(input("Classroom A: "))
classB = int(input("Classroom B: "))
classC = int(input("Classroom C: "))

roomA = classA // desk
roomB = classB // desk
roomC = classC // desk

if classA % desk != 0:
    classA += 1
roomA = classA // desk

if classB % desk != 0:
    classB += 1
roomB = classB // desk

if classC % desk != 0:
    classC += 1
roomC = classC // desk

total = roomA+roomB+roomC

print (f"You will need {total} desks minimum for every student.")
