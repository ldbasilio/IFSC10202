"""
- Create a Python program that calculates the running average, semester average, and letter grade for students based on a variable number of grades.
- Logic:
    - Step 1 - Create a class called Student
    - Step 2 - Define the initializer, the initializer should accept the folloing class values:
        firstname (string)
        lastname (string)
        tnumber (string)
        scores (List of string scores) Note this list is variable in length
    - Step 3 - In the initializer, create the following object attributes
        FirstName (string)
        LastName (string)
        TNumber (string)
        Grades (List of string grades) Note that this list is variable in length
-   Step 4 - Define the methods for the object
        RunningAverage(self) - calculates the running average (non-blank) of the scores
        TotalAverage(self) - calculates the average oft the scores, where missing scores are treated a zero
        LetterGrade(self) - Returns the letter grade based on TotalAverage, where
            >= 90 is an"A"
            >= 80 and < 90 is a "B"
            >= 70 and < 80 is a "C"
            >= 60 and < 70 is a "D"
            < 60 is an "F"

As you read each line from StudentScores.txt, you will create one Student object. You can reuse this object as you read the next student.

# Copy, paste and save the file below as 10.Project Student Scores.txt
Jim,Evans,T123456,95,,71
Joe,Smith, T654321,90,80,85,97
Jane,Doe,T121212,,100,99

# Note about 10.Project Student Scores.txt
Jim Evans has 3 scores - the second score is missing
Joe Smith has 4 scores
Jane Doe has 2 scores - the first score is missing
"""

"""
    First       Last        ID      Running     Semester
Letter
    Name        Name       Number   Average     Average
Grade
------------ ------------ ------------ ------------ ------------ ------------
    Jim         Evans      T123456  83.00        55.33
F
    Joe         Smith      T654321  88.00        88.00
B
    Jane        Doe        T121212  99.50        66.33
D
"""

class Student():

    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        total = 0.0
        count = 0

        for g in self.Grades:
            if g.strip() != "":
                total += float(g)
                count += 1

        if count == 0:
            return 0.0

        return total / count

    def TotalAverage(self):
        if len(self.Grades) == 0:
            return 0.0

        total = 0.0

        for g in self.Grades:
            if g.strip() == "":
                value = 0.0
            else:
                value = float(g)
            total += value

        return total / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


print ("\nStudent Scores Program\n")

# Print header
print ("{:>10s}{:>10s}{:>12s}{:>16s}{:>16s}{:>8s}".format(
    "First", "Last", "TNumber", "Running Avg", "Semester Avg", "Grade"))
print ("-" * 72)

# Open the student scores file
infile = open("10.Project Student Scores.txt", "r")

line = infile.readline()
while line != "":
    line = line.strip()

    if line != "":
        parts = line.split(",")

        first = parts[0].strip()
        last = parts[1].strip()
        tnum = parts[2].strip()

        scores = []
        for i in range(3, len(parts)):
            scores.append(parts[i].strip())

        student = Student(first, last, tnum, scores)

        run_avg = student.RunningAverage()
        sem_avg = student.TotalAverage()
        grade = student.LetterGrade()

        print ("{:>10s}{:>10s}{:>12s}{:16.2f}{:16.2f}{:>8s}".format(
            student.FirstName,
            student.LastName,
            student.TNumber,
            run_avg,
            sem_avg,
            grade))

    line = infile.readline()

infile.close()