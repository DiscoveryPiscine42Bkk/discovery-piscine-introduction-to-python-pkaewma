num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

addition = num1 + num2
subtration = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtration}")
print(f"{num1} * {num2} = {multiplication}")
<<<<<<< HEAD
print(f"{num1} / {num2} = {division}")
=======
print(f"{num1} / {num2} = {division}")
>>>>>>> 1b72b64 (now)
