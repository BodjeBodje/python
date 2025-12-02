#global scope
name="amadou"

# num1 = 10
# num2 = 20
# print(num1 + num2)

# a function to add two numbers
def add():
    print(name)#accessing global variable inside function
    print("this is add function")
# #calling the function add
# add()
# add()
# add()

#how to pass data to function
def check_even(number):
    print(name)#accessing global variable inside function
    print("In the check even function")
    print(number % 2 == 0)
# #calling the function check_even
# #true
# check_even(4)
# #false
# check_even(7)

#function to print the first n numbers
def print_numbers(n):
    print(name)#accessing global variable inside function
    print("In the print n function")
    # local scope: this variable is only accessible inside this function
    counter = 0
    while counter <= n:
        print(counter)
        check_even( counter) #calling check_even function inside print_numbers function
        counter += 1
# # `print_numbers(5)` is a function call that will print the numbers from 0 to 5, along with checking
# if each number is even or not by calling the `check_even` function for each number. Additionally,
# it will access the global variable `name` and print "In the print n function" before printing each
# number and checking if it is even.
# print_numbers(5)

#to add two numbers.
def add_n(n1, n2):
    print(f"args {n1} and {n2}")
    sum_ = n1 + n2
    return sum_
    # print(n1 + n2)
# add_n(10, 20)
# a=add_n(100, 200)
# print(a) #None

# a function to print your name: default argument
#Optional argument
def print_name(phone: int, name: str="Guest User"):
    print(f"Name is: {name}")
# print_name("Amadou")
# print_name()

#write a program o take a block of text and convert it to uppercase
def to_uppercase(text)-> str:
    upper_text = text.upper()
    return upper_text
print(to_uppercase("hello world"))