#STEP 1: Take input from the user
name = input("Enter your name: ")

#STEP 1 B: type casting
name=int(name)

#STEP 2: check if n%2==0
if name % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")