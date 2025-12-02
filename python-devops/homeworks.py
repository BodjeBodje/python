
cpu_usage = 76
cpu_usage = input("Enter the current CPU usage percentage: ")

cpu_usage = int(cpu_usage)

if cpu_usage < 50:
    print("Server is healthy.")
elif cpu_usage >= 50 and cpu_usage < 80:
    print("Server moderate.")
else:
    print("Server is critical.")
    
    
print("-----------------------------------------------------")

start_number = 1
end_number = 10

while start_number <= end_number:
    print(f"Current Number: {start_number}")
    start_number += 1

print("-----------------------------------------------------")

    #password checker
def password_checker():
    correct_password = "python123"
    user_password = input("Enter the password: ")

    if user_password == correct_password:
        print("Access granted.")
    else:
        print("Access denied.")
password_checker()

