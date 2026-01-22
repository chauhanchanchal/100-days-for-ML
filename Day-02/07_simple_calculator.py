a=int(input("enter first number:"))
b=int(input("enter seconf number:"))

op=input("Enter operator(+,-,*,/):")

if op=='+':
    print(f"{a} + {b} = {a + b}")

elif op=='-':
    print(f"{a} - {b} = {a - b}")

elif op=='*':
    print(f"{a} * {b} = {a * b}")

elif op=='/':
    print(f"{a} / {b} = {a / b}")