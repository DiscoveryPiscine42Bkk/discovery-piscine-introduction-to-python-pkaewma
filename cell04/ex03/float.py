from cmath import inf


user_input = input("Please enter a number")
try:
    number = float(user_input)
    if number . is_integer():
        print(f"The number {inf(number)} is an integer.")
    elif '.' in user_input:
        print(f"The number {user_input} is a decimal")
    else:
        print(f"The number {user_input} is not a decimal")

except ValueError:
<<<<<<< HEAD
    print("That's not a valid number.")
=======
    print("That's not a valid number.")
>>>>>>> 1b72b64 (now)
