while True:
    user_inpnt = input("say something(type 'STOP' to exit):")

    if user_inpnt.upper() == "STOP":
       print("stopping the program.")
       break

print(f"I got that : {user_inpnt}")