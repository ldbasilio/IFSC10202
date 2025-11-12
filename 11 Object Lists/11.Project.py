"""
11.Project.py

This program reads student info and scores from files, calculates running averages, semester averages, and letter grades, and then prints a formatted list.
"""

class Student():

    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []    # list of string grades (can be "")

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


class StudentList():

    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        new_student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(new_student)

    def find_student(self, tnumber):
        for i in range(len(self.Studentlist)):
            if self.Studentlist[i].TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        print ("{:>10s}{:>10s}{:>12s}{:>16s}{:>18s}{:>10s}".format(
            "First", "Last", "TNumber", "Running Avg", "Semester Avg", "Grade"))
        print ("-" * 76)

        for student in self.Studentlist:
            run_avg = student.RunningAverage()
            sem_avg = student.TotalAverage()
            grade = student.LetterGrade()

            print ("{:>10s}{:>10s}{:>12s}{:16.2f}{:18.2f}{:>10s}".format(
                student.FirstName,
                student.LastName,
                student.TNumber,
                run_avg,
                sem_avg,
                grade))

    def add_student_from_file(self, filename):
        student_file = open(filename, "r")

        line = student_file.readline()
        while line != "":
            parts = line.split(",")
            first = parts[0].strip()
            last = parts[1].strip()
            tnum = parts[2].strip()

            self.add_student(first, last, tnum)

            line = student_file.readline()

        student_file.close()

    def add_scores_from_file(self, filename):
        score_file = open(filename, "r")

        line = score_file.readline()
        while line != "":
            parts = line.split(",")
            tnum = parts[0].strip()

            if len(parts) > 1:
                score = parts[1].strip()
            else:
                score = ""

            index = self.find_student(tnum)

            if index != -1:
                self.Studentlist[index].Grades.append(score)

            line = score_file.readline()

        score_file.close()


print ("\nStudent Scores Program\n")

student_list = StudentList()

student_list.add_student_from_file("11.Project Students.txt")
student_list.add_scores_from_file("11.Project Scores.txt")

student_list.print_student_list()
