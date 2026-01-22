# This program finds the largest of three numbers

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
if x >= y and x >= z:
    print(f"{x} is the largest number.")
elif y >= x and y >= z:
    print(f"{y} is the largest number.")
else:
    print(f"{z} is the largest number.")