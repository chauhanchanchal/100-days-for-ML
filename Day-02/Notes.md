# 02 – Variables, Data Types, Operators & Conditional Statements (Python)

### Topics Covered


## 1️⃣ Variables in Python

Variables are used to store values in memory.  
Python automatically determines the data type.

***Example***

```python

age = 20
name = "Chanchal"
height = 5.8
is_student = True

print(age)
print(name)
print(height)
print(is_student)

```


- No need to declare data type
- Variable names are case-sensitive
- Must start with a letter or underscore

## 2️⃣ Data Types in Python

### Common Data Types

|Data |Type	Meaning  |Example|
|-----|--------------|-------|
|int|Integer numbers|10, -5|
|float|Decimal number|3.14|
|str|Text / string  |"Hello"|
|bool|True or False  |True|

***Example***
```python

a = 10          # int
b = 3.5         # float
c = "Python"    # string
d = False       # boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

## 3️⃣ Operators in Python

### 🔹 Arithmetic Operators

Used to perform mathematical operations.

|Operator	|Meaning|
|---------|---------|
|+	|Addition|
|-	|Subtraction|
|*	|Multiplication|
|/	|Division|
|%	|Modulus|
|//	|Floor Division|
|**	|Power|
***Example***
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000
```
### 🔹 Comparison (Relational) Operators

Used to compare values.

|Operator |	Meaning|
|---------|---------|
|== |Equal|
|!= |Not equal|
|> |Greater than|
|< |Less than|
|>= |Greater than or equal|
|<= | Less than or equal|
***Example***
```python
x = 5
y = 10

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
```
### 🔹 Logical Operators

Used to combine multiple conditions.

|Operator|sign|	Meaning|
||-------|------|-------|
|and|&&|Both conditions true|
|or| `||` |At least one true|
|not|! |Reverse condition|


***Example***
```python
age = 22

print(age > 18 and age < 30)   # True
print(age < 18 or age > 60)    # False
print(not age > 18)            # False
```

### 4️⃣ Conditional Statements
## 🔹 if Statement

Executes code only if condition is true.

***Example***
```python

age = 20

if age >= 18:
    print("You are an adult")
```

### 🔹 if-else Statement

Chooses between two paths.

***Example***
```python

num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 🔹 if-elif-else Ladder

Used for multiple conditions.

***Example***
```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```

| No. | Problem Name               | Concept Used              | Key Logic                   |
| --- | -------------------------- | ------------------------- | --------------------------- |
| 1   | Even or Odd Number         | Modulus Operator, if-else | `num % 2 == 0`              |
| 2   | Positive, Negative or Zero | if-elif-else              | Compare with `0`            |
| 3   | Largest of Two Numbers     | Comparison, if-else       | `a > b`                     |
| 4   | Largest of Three Numbers   | Logical Operators         | `a >= b and a >= c`         |
| 5   | Leap Year Check            | Logical Conditions        | `%400` or `%4 and not %100` |
| 6   | Vowel or Consonant         | Strings, Membership       | Character in `aeiou`        |
| 7   | Simple Calculator          | if-elif-else              | Operation based on choice   |

| No. | LeetCode Problem           |
| --- | ---------------------------|
| 1   | 7. Reverse Integer         |
| 3   | 12. Integer to Roman       |
| 4   | 41. First Missing Positive |

Day-02 completed. Learned Python basics for logic building using variables, operators, and conditions. Ready to move to Day-03: Loops in Python.