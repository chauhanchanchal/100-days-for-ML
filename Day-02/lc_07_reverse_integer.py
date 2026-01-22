a = int(input("Enter an integer:"))
rev = 0

while a != 0:
    digit = a % 10  # Extract the last digit
    rev = rev * 10 + digit  # Append digit to reversed number
    a //= 10   # Remove the last digit from a

print(f"Reversed integer: {rev}")


