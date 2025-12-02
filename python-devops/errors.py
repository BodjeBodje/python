# number=19
# print(19/0)

try:
    # number=10
    # print(19/0)
    file=open("nonexistent.txt")
except Exception as e:
    print(f"An exception occurred this is desc {e}")
    new_file=input("enter the proper file name")
finally:
    print("This is the finally block")