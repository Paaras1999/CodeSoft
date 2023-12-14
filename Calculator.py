import math
#Function to add two numbers.
def addition(a, b):
    return a + b
#Function to Subtarct two numbers.
def subtraction(a, b):
    return a - b
#Function to multiply two numbers.
def multiplication(a, b):
    return a * b
#Function to divide two numbers.
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
#Function to squareroot of a numbers.
def squareroot(a):
    result = math.sqrt(a)
    return result
#Function to exponent of a numbers.
def exp(a):
    return a ** 2
#Function to find the value of sin numbers.
def sin(x):
    result = math.sin(x)
    return result

def cos(x):
    result = math.cos(x)
    return result

def tan(x):
    result = math.tan(x)
    return result

print("""
Choose a number for the following operation for calculating the values of two numbers:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Square root
7. Sin
8. Cos
9. Tan
10. Quit
""")

while True:
    operation = int(input('What operation do you want to use (1-10): '))
    
    if operation == 10:
        print("Thank you for using the scientific calculator!")
        break
    elif operation < 1 or operation > 10:
        print("Invalid operation. Please choose a valid operation (1-10).")
        continue
    
    if operation == 1:
        x1 = float(input("Enter x: "))
        y1 = float(input("Enter y: ")) 
        result = addition(x1, y1)
    elif operation == 2:
        x2 = float(input("Enter x: "))
        y2 = float(input("Enter y: "))
        result = subtraction(x2, y2)
    elif operation == 3:
        x3 = float(input("Enter x: "))
        y3 = float(input("Enter y: "))
        result = multiplication(x3, y3)
    elif operation == 4:
        x4 = float(input("Enter x: "))
        y4 = float(input("Enter y: "))
        result = divide(x4, y4)
    elif operation == 5:
        x5 = float(input("Enter x: "))
        result = exp(x5)
    elif operation == 6:
        x6 = float(input("Enter x: "))
        result = squareroot(x6)
    elif operation == 7:
        x7 = float(input("Enter x: "))
        result = sin(x7)
    elif operation == 8:
        x8 = float(input("Enter x: "))
        result = cos(x8)
    elif operation == 9:
        x9 = float(input("Enter x: "))
        result = tan(x9)
    
    print("Result:", result)
    break