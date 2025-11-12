"""
11.00.02 Create an Object List
We have seen how to create a list of objects. Now lets create a new object that manages the list of objects.

Lines 1-25: This is the same Ball class that we have used in previous examples
Lines 26-27: Create a new class called BallList
Lines 29-34: Initializer for the BallList. Simply create an attribute that contains an empty list.
Lines 36-42: add_ball method - adds a ball to the list. Creates a Ball object and appends it to the list.
Lines 44-49: delete_ball - deletes a ball from the list. Uses find_ball method to find the index of the ball, then deletes it from the list.
Lines 51-58: change_pressure - changes the pressure in a particular ball. Uses find_ball method to find the index of the ball, then adds the pressure to the specific ball
Lines 60-65: find_ball - finds a ball in the list. Loops through the ball list and searches for a match in the BallType. Returns the index when the ball is found.
Lines 67-69: number_of_balls - returns the number of balls in the list
Lines 71-78 - print_ball_list - prints the list and the number of balls
Lines 80-91 - add_ball_from_file - reads a file and appends the values to the list. Note the used of self.add_ball to add the ball.
Lines 95-121 - main prog
"""

from math import pi
 
# Step 1 - Define the class object "Ball"
class Ball():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
 
# Step 3 - Define the object attributes for a ball
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure
 
# Step 4 - Define Actions (Methods) associated with the object
# Calculate Circumference for a ball
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
 
# Step 4 - Here is another action
# Change the pressure in the ball
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure
 
# Step 1 - Define the class object "BallList"
class BallList ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self):
 
# Step 3 - Define the object attributes
# Create an empty ball list
		self.Balllist = []
 
# Step 4 - Define Actions (Methods) associated with the object
# Add a ball to the list
	def add_ball(self, balltype="Basketball", diameter=9.51, pressure=8.0):
#		Create a new ball object
		myball = Ball(balltype, diameter, pressure)
#		Append ball object to list
		self.Balllist.append(myball)
 
# Delete a ball from the list
	def delete_ball(self, balltype):
#		Find the ball and get the index
		index = self.find_ball(balltype)
#		Delete the entry
		del self.Balllist[index]
 
# Change the pressure of a ball
	def change_pressure(self, balltype, pressurechange):
#		Find the ball dnd get the index
		index = self.find_ball(balltype)
#		Change the pressure
		self.Balllist[index].Pressure += pressurechange
#		Return the new pressure
		return self.Balllist[index].Pressure
 
# Find a ball and return the index
	def find_ball(self, balltofind):
		for i in range(len(self.Balllist)):
			if self.Balllist[i].BallType == balltofind:
				return i
		return -1		
 
#  Returns the number of balls in the list
	def number_of_balls(self):
		return len(self.Balllist)
 
# Print the ball list
	def print_ball_list(self):
		print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Diameter", "Pressure", "Circumference"))
		for i in range(len(self.Balllist)):
			print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(self.Balllist[i].BallType, self.Balllist[i].Diameter, self.Balllist[i].Pressure, self.Balllist[i].Circumference()))
		print()
		print("{} balls in list".format(self.number_of_balls()))
		print()
		
# Read a file and append the vales to the ball list
	def add_ball_from_file(self, filename):
		ballfile = open(filename)
		x = ballfile.readline()
		while x != "":
#			print(x) # display what was read
			y = x.split(",")
#			print(y) # display the result of the split
			self.add_ball(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
			x = ballfile.readline()
		ballfile.close()
	
 
'''#--------------------------------------------------------------------
 
# Create a Ball List
myballlist = BallList()
 
# Read Ball List from File
myballlist.add_ball_from_file("11.00.01 Balls.txt")
 
# Display List
myballlist.print_ball_list()
 
# Pump up the Basketball
myballlist.change_pressure("Basketball", 1)
 
# Deflate the volleyball
myballlist.change_pressure("Volleyball", -1)
 
# Add a Baseball
myballlist.add_ball("Baseball", 2.75, 0.0)
 
# Display List
print()
myballlist.print_ball_list()
 
# Delete Soccerball
myballlist.delete_ball("Soccerball")
 
# Display List
myballlist.print_ball_list()

Copy, paste and run the above code as 11.00.03 Object List Management.py'''