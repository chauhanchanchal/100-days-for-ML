a = int(input("Enter an integer: "))

val = [1000, 900, 500, 400,
       100, 90, 50, 40,
       10, 9, 5, 4,
       1]
rom = ["M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"]

result = "" 
for i in range(len(val)):  
    count = a // val[i] 
    if count > 0:
        result += rom[i] * count
        a %= val[i] 

print(f"Roman numeral: {result}") 