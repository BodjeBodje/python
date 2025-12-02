#list declaration
list_of_numbers = []
list_of_numbers1 = list()
list_of_numbers2 = [1, 2, 3, 4, 5]

#int 0 2 3 4 
even_numbers = [0, 2, 4, 6, 8, 10]

#list operations
#index
first_element = even_numbers[0]
print(first_element)

#slice list[start:end]
block= even_numbers[1:4] #2,4,6
print(block)

# assignment operation. | replace using their index
even_numbers[2] = 10
print(even_numbers)

#Methods/functions for lists
even_numbers.append(12)
print(even_numbers)

even_numbers.remove(8)
print(even_numbers)

even_numbers.sort(reverse=True)
print(even_numbers)

even_numbers.insert(2, 15) #insert 15 at index 2
print(even_numbers)

even_numbers.append("w") #append string to list
print(even_numbers)

# for number in even_numbers:
#     print(f"Current number is: {number}")

even_numbers.pop() #remove last element
print(even_numbers)

#passing list to function
list_a = [1, 2, 4, 6, 10]

def check_list(collection: list[int]) -> list[int]:
    list_even = []
    for n in collection:
        if n % 2 == 0:
            list_even.append(n)
    return list_even
even=check_list(list_a)
print(even)