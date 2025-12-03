"""
*Employee List

You have a file named Final Project Employees.txt file that contains the following employee information:
    Employee Number (must be an integer)
    First Name (Required)
    Last Name (Required)
    Address (Required)
    City (Required)
    State (must be a valid upper case state)
    Zip (must be 5 numeric digits)

#Here is an example of Final Project Employees.txt:
5, Bruce, Bauer, 101 Markham, Little Rock, AR, 72200
7, Jane, Doe, 100 Chicot, Little Rock, AR, 72209

*Create a Python program that will add, delete, change, display, and save the data. It should display the following menu:
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit

Enter Selection:


'Add a New Employee'
    If the user selects “A”, the program should determine the next available employee number (last number in the list plus one. It should then prompt for all of the data, including First Name, Last Name, Address, City, State, and Zip then print "Employee Added". Be sure to enforce the rules as shown above.

'Delete an Existing Employee'
    If the user selects “D”, the program should ask the user for an employee number. The display an error if the employee does not exit, or delete the employee and print "Employee Deleted".

'Change an Existing Employee'
    If the user selects 3, “C” the program should ask the user for an employee number. It should check if the Employee Number is in the list. If it is not in the list, then the program should display a suitable error message. If the Employee Number is in the list, prompt for changes using the following menu:
    
    (F)irst Name
    (L)Last Name
    (A)ddress
    (C)ity
    (S)tate
    (Z)ip
    (B)ack to Main Menu

    Enter Selection:

Once the user has made a menu selection, prompt for the value and update the data. Be sure to enforce the rules as shown above.


'Print All Employees'
    If the user selects “P”, then display all of the data for all employees with suitable headings.

'Save Changes to File'
    If the user selects S, then write out all of the data in .CSV format, separated with commas.

'Quit'
    If the user selects Q, then exit the program. 


*Python Classes

You will need two classes, 'Employee' and 'EmployeeList'.

    'Employee' - The attributes contain the data about about the Employee.  There are no methods.
    'EmployeeList' - contains a list of Employee objects.  There are various methods in the class to maintain the list.

*Employee Class

Step 1 - Create a class called Employee
Step 2 - Define the initializer. The initializer should accept the following class values:
    Employee Number (must be an integer)
    First Name (Required)
    Last Name (Required)
    Address (Required)
    City (Required)
    State (must be a valid upper case state
    Zip (must be 5 numeric digits)
Step 3 - In the initializer, create the following object attributes:
    Employee Number (must be an integer)
    First Name (Required)
    Last Name (Required)
    Address (Required)
    City (Required)
    State (must be a valid upper case state
    Zip (must be 5 numeric digits)


*EmployeeList Class
Step 1 - Create a class called EmployeeList
Step 2 - Define the initializer, the initializer should accept the following class values:
    filename (string) - name of the employee file.
Step 3 - In the initializer, create the following object attributes:
    EmployeeList of Employee objects.
    filename (string) - name of password file.
Step 4 - Define the methods for the object:

ReadEmployeeFile()
    Opens FileName file containing Employee Data.
    Reads a line a data and splits the data into a list.
    Creates an Employee Object from the data.
    Appends Employee Object to EmployeeList.

WriteEmployeeFile()
    Opens FileName for writing.
    Loops though the EmployeeList.
    Writes the Employee Data in .CSV format.

DisplayEmployeeList()
    Prints appropriate headings.
    Loops through the Employee List.
    Prints the all of the data for each Employee object in the EmployeeList.

ReadEmployee (EmployeeNumber)
    Uses “FindEmployee” to look up the index of employee number, then returns:
        EmployeeNumber
        FirstName
        LastName
        Address
        City
        State
        Zip


AddEmployee (firstName, lastName, address, city, state, zip)
    Determines the next Employee Number by calling NextEmployeeNumber.
    Creates an Employee object and appends it to the EmployeeList.

UpdateEmployee(employeenumber, firstName, lastName, address, city, state, zip)
    Looks for index of employeenumber.
    Updates the object with all of the above values.

DeleteEmployee(employenumber)
    Looks for index of employeenumber.
    Deletes the Employee Object from the list.

FindEmployee(EmployeeNumber)
    Loops through the EmployeeList looking for a matching EmployeeNumber.
    Returns the index of Employee in EmployeeList.
    If Employee not found then return -1.

NextEmployee Number()
    Gets the EmployeeNumber of last employee.
    Adds 1 to it an make it the NewEmployeeNumber.
    Returns the NewEmployeeNumber.
"""
"""
#Sample Script for Final Project

(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: P
 
Employee        First           Last            Address         City            State           Zip            
Number          Name            Name           
--------------- --------------- --------------- --------------- --------------- --------------- ---------------
5               Bruce           Bauer           101 Markham     Little Rock     AR              72200          
7               Jane            Doe             100 Chicot      Little Rock     AR              72209          
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: A
 
Enter First Name: Mary
Enter Last Name: Smith
Enter Address: 100 River
Enter City: Benton
Enter State: AR
Enter Zip: 72134
Employee Added
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: p
 
Employee         First           Last            Address         City            State           Zip            
Number           Name            Name           
--------------- --------------- --------------- --------------- --------------- --------------- ---------------
5                Bruce           Bauer          101 Markham     Little Rock     AR              72200          
7                Jane            Doe            100 Chicot      Little Rock     AR              72209          
8                Mary            Smith          100 River       Benton          AR              72134          
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: C 
 
Enter Employee Number: 8
 
(F)irst Name
(L)Last Name
(A)ddress
(C)ity
(S)tate
(Z)ip
(B)ack to Main Menu
 
Enter Selection: L
 
Enter Last Name: Brown
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: P
 
Employee         First           Last            Address         City            State           Zip            
Number           Name            Name           
--------------- --------------- --------------- --------------- --------------- --------------- ---------------
5                Bruce           Bauer          101 Markham     Little Rock     AR              72200          
7                Jane            Doe            100 Chicot      Little Rock     AR              72209          
8                Mary            Brown          100 River       Benton          AR              72134 
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: D
 
Enter Employee Number: 8
Employee Deleted
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: P
 
Employee         First           Last            Address         City            State           Zip            
Number           Name            Name           
--------------- --------------- --------------- --------------- --------------- --------------- ---------------
5                Bruce           Bauer          101 Markham     Little Rock     AR              72200          
7                Jane            Doe            100 Chicot      Little Rock     AR              72209          
 
(A)dd a New Employee
(D)elete an Existing Employee
(C)hange an Existing Employee
(P)rint All Employees
(S)ave Changes to File
(Q)uit
 
Enter Selection: Q
 
Good-bye

"""

class Employee():
    def __init__(self, number, firstname, lastname, address, city, state, zipcode):
        self.EmployeeNumber = int(number)
        self.FirstName = firstname
        self.LastName = lastname
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zipcode


class EmployeeList():
    def __init__(self, filename):
        self.EmployeeList = []
        self.FileName = filename
    def ReadEmployeeFile(self):
        infile = open(self.FileName, "r")
        line = infile.readline()
        while line != "":
            line = line.strip()
            if line != "":
                parts = line.split(",")
                if len(parts) >= 7:
                    number = parts[0].strip()
                    firstname = parts[1].strip()
                    lastname = parts[2].strip()
                    address = parts[3].strip()
                    city = parts[4].strip()
                    state = parts[5].strip()
                    zipcode = parts[6].strip()

                    employee = Employee(number, firstname, lastname, address, city, state, zipcode)
                    self.EmployeeList.append(employee)
            line = infile.readline()
        infile.close()

    def WriteEmployeeFile(self):
        outfile = open(self.FileName, "w")
        for emp in self.EmployeeList:
            line = str(emp.EmployeeNumber) + ", " + emp.FirstName + ", " + emp.LastName + ", " + emp.Address + ", " + emp.City + ", " + emp.State + ", " + emp.Zip + "\n"
            outfile.write(line)
        outfile.close()

    def DisplayEmployeeList(self):
        print ("")
        print ("Employee         First           Last            Address         City            State           Zip            ")
        print ("Number           Name            Name           ")
        print ("--------------- --------------- --------------- --------------- --------------- --------------- ---------------")

        for emp in self.EmployeeList:
            print ("{:15d}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(
                emp.EmployeeNumber,
                emp.FirstName,
                emp.LastName,
                emp.Address,
                emp.City,
                emp.State,
                emp.Zip))
        print ("")

    def FindEmployee(self, employeenumber):
        for i in range(len(self.EmployeeList)):
            if self.EmployeeList[i].EmployeeNumber == employeenumber:
                return i
        return -1

    def ReadEmployee(self, employeenumber):
        index = self.FindEmployee(employeenumber)
        if index == -1:
            return None, None, None, None, None, None, None
        emp = self.EmployeeList[index]
        return emp.EmployeeNumber, emp.FirstName, emp.LastName, emp.Address, emp.City, emp.State, emp.Zip

    def NextEmployeeNumber(self):
        if len(self.EmployeeList) == 0:
            return 1
        last_emp = self.EmployeeList[-1]
        return last_emp.EmployeeNumber + 1

    def AddEmployee(self, firstname, lastname, address, city, state, zipcode):
        new_number = self.NextEmployeeNumber()
        emp = Employee(new_number, firstname, lastname, address, city, state, zipcode)
        self.EmployeeList.append(emp)

    def UpdateEmployee(self, employeenumber, firstname, lastname, address, city, state, zipcode):
        index = self.FindEmployee(employeenumber)
        if index != -1:
            emp = self.EmployeeList[index]
            emp.FirstName = firstname
            emp.LastName = lastname
            emp.Address = address
            emp.City = city
            emp.State = state
            emp.Zip = zipcode

    def DeleteEmployee(self, employeenumber):
        index = self.FindEmployee(employeenumber)
        if index != -1:
            del self.EmployeeList[index]
            return True
        else:
            return False

def get_required(prompt):
    value = input(prompt)
    while value.strip() == "":
        print ("Value is required.")
        value = input(prompt)
    return value.strip()

def get_state(prompt):
    value = input(prompt)
    value = value.strip().upper()
    while not (len(value) == 2 and value.isalpha()):
        print ("State must be 2 upper case letters.")
        value = input(prompt)
        value = value.strip().upper()
    return value

def get_zip(prompt):
    value = input(prompt)
    value = value.strip()
    while not (len(value) == 5 and value.isdigit()):
        print ("Zip must be 5 numeric digits.")
        value = input(prompt)
        value = value.strip()
    return value

def get_int(prompt):
    value = input(prompt)
    while True:
        try:
            num = int(value)
            return num
        except:
            print ("Employee Number must be an integer.")
            value = input(prompt)


print ("\nEmployee List Program\n")

employees = EmployeeList("Final Project Employees.txt")
employees.ReadEmployeeFile()

selection = ""

while selection != "Q":
    print ("(A)dd a New Employee")
    print ("(D)elete an Existing Employee")
    print ("(C)hange an Existing Employee")
    print ("(P)rint All Employees")
    print ("(S)ave Changes to File")
    print ("(Q)uit")
    print ("")
    selection = input("Enter Selection: ")
    selection = selection.strip().upper()
    print ("")
    if selection == "A":
        first = get_required("Enter First Name: ")
        last = get_required("Enter Last Name: ")
        address = get_required("Enter Address: ")
        city = get_required("Enter City: ")
        state = get_state("Enter State: ")
        zipcode = get_zip("Enter Zip: ")
        employees.AddEmployee(first, last, address, city, state, zipcode)
        print ("Employee Added")
        print ("")
    elif selection == "D":
        empnum = get_int("Enter Employee Number: ")
        deleted = employees.DeleteEmployee(empnum)
        if deleted:
            print ("Employee Deleted")
        else:
            print ("Employee not found")
        print ("")
    elif selection == "C":
        empnum = get_int("Enter Employee Number: ")
        print ("")
        index = employees.FindEmployee(empnum)
        if index == -1:
            print ("Employee not found")
            print ("")
        else:
            change_selection = ""
            while change_selection != "B":
                print ("(F)irst Name")
                print ("(L)Last Name")
                print ("(A)ddress")
                print ("(C)ity")
                print ("(S)tate")
                print ("(Z)ip")
                print ("(B)ack to Main Menu")
                print ("")
                change_selection = input("Enter Selection: ")
                change_selection = change_selection.strip().upper()
                print ("")
                number, first, last, address, city, state, zipcode = employees.ReadEmployee(empnum)
                if change_selection == "F":
                    first = get_required("Enter First Name: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
                elif change_selection == "L":
                    last = get_required("Enter Last Name: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
                elif change_selection == "A":
                    address = get_required("Enter Address: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
                elif change_selection == "C":
                    city = get_required("Enter City: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
                elif change_selection == "S":
                    state = get_state("Enter State: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
                elif change_selection == "Z":
                    zipcode = get_zip("Enter Zip: ")
                    employees.UpdateEmployee(empnum, first, last, address, city, state, zipcode)
                    print ("")
    elif selection == "P":
        employees.DisplayEmployeeList()
    elif selection == "S":
        employees.WriteEmployeeFile()
        print ("Changes saved to file.")
        print ("")
    elif selection == "Q":
        print ("Good-bye")
        print ("")
    else:
        if selection != "":
            print ("Invalid selection.")
            print ("")
