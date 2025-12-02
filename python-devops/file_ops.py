#A python program to read from a file
# import input
# import os
# print(os.listdir)

# print(os.getcwd())
# os.chdir("new")
# print("new")
# from .input
# print(input.add(1,2))

# def add(n1,n2):
#     return n1+n2

print("---------------------------------------------------------")
def read_write(input_file,output_file):
    with open(input_file, 'r') as file:
        content=file.read()
        new_content=content.upper()
        print(f"This is my new content: {new_content}")
        
        with open(output_file,'w') as file:
            file.write(new_content)
read_write("sets.py", "new_sets.py")

# with open('class24.txt', 'r') as file:
#     content=file.read()
#     new_content=content.upper()
#     print(f"This is my new content: {new_content}")
    
#     with open('class24_output.txt','w') as file:
#         file.write(new_content)
        

# #open
# file=open('class24.txt', 'r')
# #read the content of the file
# content=file.read()
# #print the contents
# print(content)
# #close the file
# file.close()