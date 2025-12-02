"""
10.00.00 Object Oriented Programming
What Is Object Oriented Programming?
In programming/scripting, we use logic. This logic dictates actions that we take and how we perform them. Focusing on the action in programming is rather difficult, instead, we can look at the bigger picture. Take a ball for example. We can bounce the ball, and this is an action. But this action is way more complicated than taking a step back and saying "This is a ball, I can bounce it.'"

By using object oriented programming, we can make it easier to see how two things relate. Since we've taken a step back to see that the ball can bounce, we can also see it's relation to the object is bounces off of.

Now that we've discussed how OOP can make programming easier, let's make our own class. We'll try to build that ball we were just talking about.

A class is basically a template for an object. It's something that we can make attributes for and perform actions on. We can make our own attributes and even our own methods for our object. First, we'll need to know more about something called object oriented programming (OOP), so let's get started!

Step 1 - Define the Class
When we make a new class, we have to define it (much like a function). We do this by entering the keyword class, followed parenthesis. Notice that there is a colon after the class definition. This means we will indent any code that pertains to the Ball object.

# Step 1 - Define the class object "Ball"
class Ball ():

Step 2 - Define the Initializer:
Now that we have our class, we have to define our initializer. This is the function that runs when we create a new instance of our class. Essentially, we use this to define any variables or attributes that we want to use throughout the object. Some examples (which we'll be using in our class) are the type of the Ball, the diameter of the ball, and the pressure of the ball.)

When we define our initializer, we essentially just make a function with the name __init__ (There are two underscores there). This must be the first function of our class.

   def __init__(self, balltype, diameter, pressure):

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

It it also possible to define defaults, in case values were not supplied in the inititializer.

    def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
So far, here is our object

# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
    def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
Now that we're done defining init, let's move on to giving the ball object some attributes.

Step 3 - Define Object Attributes
An object attribute is simply data that was want to keep aboiut an object. It can be numbers, strings and any other datatype. They are create in the init function. Atributes are called "properties" in other programming languages.

We can see here that init is just like any other function, but there are some things that make this a bit more complicated. We've already covered that classes are objects, but what if we want to make an attribute that plays off of another attribute, how do we use our object within itself? Well, we can use self. Self is basically a way of telling the object that this is found within itself. When we define attributes, we have to define them as part of the object's self. Let's go ahead and define our objects attributes so we can see an example:

self.BallType = balltype
self.Diameter = diameter
self.Pressure = pressure

Here we can see that we've successfully defined the attributes for our ball. Our BallType, Diameter, and Pressure are initialized to the values passed to it. When we're defining/changing attributes within our class, we need to refer to them with the self.(ATTRIBUTE) format. This tells the class that the following attribute is its own. Now that we have our attributes, let's see if we can make some actions to perform on ball.

So now, our object looks like:
# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
 
# Step 3 - Define the object attributes
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure

Step 4 - Make the Actions
We'll be making two actions today. One to determine the circumference of the ball, and the other is to change the pressure of the balls. When we're making actions, we define them as normal functions, except they need to take self as an argument, just like init. Let's go ahead and make our action, we'll name it Circumference:

   def Circumference(self):
       circumference =  math.pi * self.Diameter
       return circumference

As you can see, the Circumference method has no parameters (outside of self) and it calculates the circumference of the ball.

Let's define another method called ChangePressure, which adds an amount to the current pressure. Note that the current pressure is returned.

   def ChangePressure(self, pressurechange):
       self.Pressure += pressurechange
       return self.Pressure

We can see here that this action is very simple, even though it sounded complicated. This is the beauty of object oriented programming. Let's exit making our class and bounce our ball!

Step 5 - Create the Instance
If we want to use the Ball class, we'll need to make an instance of the class first. Basically this means that we need to call our class and assign it to a variable. Here we will create 4 different balls:
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()

#Now, let's print the state of each of the ball objects:
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())

#Set a new diameter to myball1:
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

#So our object is almost complete:
from math import pi
 
# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
 
# Step 3 - Define the object attributes
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure
 
# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
 
# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure
 
# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()
 
# Print the attributes
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())

Step 6 - Use the Objects
#Set a new diameter to myball1:
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

#Pump up myball1 with 1 pound of air:
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

#So here is our complete object:
from math import pi
 
# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
 
# Step 3 - Define the object attributes
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure
 
# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
 
# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure
 
# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()
 
# Print the attributes
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())
 
# Change the Diameter attribute of myball1
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
 
# Add Pressure to myball1
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
"""