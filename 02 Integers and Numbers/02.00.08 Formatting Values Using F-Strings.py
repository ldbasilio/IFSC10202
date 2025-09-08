# There are several ways to align variables in f-strings. The various alignment options are as follows: 
# "<" - The field will be left-aligned within the available space. This is usually the default for strings.
# ">" - The field will be right-aligned within the available space. This is the default for numbers.
# "^" - Forces the field to be centered within the available space.

#The following is an example using alignment for both a number and a string. The "|" is used in the f-string to help 
#delineate the spacing. That number after the ":" will cause that field to be that number of characters wide. The first line 
#in the print() statement using f-strings is an example of using f-strings for debugging purposes which will be covered later.
from math import pi
variable = pi
print(f"Using Numeric variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

#A fill character can also be used in the alignment of f-strings. This is shown in the following example:
from math import pi
variable = pi
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")

# There are many ways to represent strings and numbers when using f-strings. The most common ones are:
# "s" - String format - this is the default type for strings
# "d" - Decimal Integer. This uses a comma as the number separator character.
# "n" - Number. This is the same as d except that it uses the current locale setting to insert the appropriate 
# number separator characters.
# "e" - Exponent notation. Prints the number in scientific notation using the letter 'e' to indicate the exponent. 
# The default precision is 6
# "f" - fixed-point notation. Displays the number as a fixed-point number. The default precision is 6.
# "%" - is percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.

#The following is a basic example of the use of f-strings with numbers:
import math
variable = 10
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:d}")
print(f"This prints also with formatting {variable:n}")
print(f"This prints with spacing {variable:10d}")
print()
variable = math.pi
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:f}")
print(f"This prints with spacing {variable:20f}")

#The following are examples of the exponent notation and the percentage notation:
variable = 4
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with percent formatting {variable:%}")
print()
variable = 403267890
print(f"Using Numeric variable = {variable}")
print(f"This prints with exponential formatting {variable:e}")

# There are several options when formatting floating point numbers. The number of decimal places, the use of the number 
# separator character, and forcing a plus (+) or minus (-) sign can also be specified. 
# These are shown in the following example:'''
variable = 1200356.8796
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places: {variable:.2f}")
print(f"With four decimal places: {variable:.3f}")
print(f"With two decimal places and a comma: {variable:,.2f}")
print(f"With a forced plus sign: {variable:+.2f}")
print()
variable *= -1
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places and a comma: {variable:,.2f}")

# Let's demonstrate how to format floating point numbers and align the number with headings.  Note that each column is 
# 10 characters wide:
print(f'{"Number":>10s}{"Square":>10s}{"Cube":>10s}')
x = 1.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 2.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 3.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')

# The following program demonstrates the use of strings, decimals, and floats for a report that is often produced 
# in a typical Python program. Notice the use of the dollar sign ($) before the variables that are to be displayed as prices.
APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 10
numCheese = 6
prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}{"":5s}${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}{"":5s}${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}{"":5s}${prcCheese:>5.2f}')
print(f'{"":10s}{"Total:":>10s}{"":5s}${total:>5.2f}')
