# This program finds the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(f"{a} is the largest number.")# f"{a} means a string with value of a
elif b > a:
    print(f"{b} is the largest number.")
else:
    print("Both numbers are equal.")