print ("\nThis is a 'Calculator' program. Please enter two numbers, and math operator, when requested.\n")

a = float(input("Enter the First Number: "))
c = input("Enter the Operator (+,-,*,/): ")
b = float(input("Enter the Second Number: "))

if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    if b == 0:
        print ("ERROR; CANNOT DIVIDE BY ZERO")
    else:
        result = a / b
else:
    result = print ("INVALID OPERAND TYPE")

print (f'{a} {c} {b} = {result}')
