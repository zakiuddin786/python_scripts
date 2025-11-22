fruits = ["apple", "banana", "mango", "orange"]
numbers = [198, 90, 100, 1000, 200, 300]
mixed_list = [1, "zaki", True]
nested_list = [["zaki", "uddin", "MD", "Engineer", "Amazon"], 1, 2, ["Mohammed"]]

mixed_list.append("Engineer at amazon") # single element to be added at end 

numbers.extend([700, 877]) # multiple elements to be added

numbers.insert(2, 987) # inserting at specific index 

numbers.remove(90) # remove a specific value

deleted_number = numbers.pop() # remove and return last element

index = fruits.index("banana") # get the index of element

numbers.sort()

print(f"banana is at {index}")
print(f"deleted number is {deleted_number}")
print(fruits)
print(numbers)
print(mixed_list)
print(nested_list)



print(len(fruits))
print(len(numbers))
print(len(mixed_list))
print(len(mixed_list))
print(len(nested_list))
print(len(nested_list[0]))


