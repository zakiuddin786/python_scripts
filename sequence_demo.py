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


empty_tuple = ()
print(type(empty_tuple))
single_element_tuple = (2, )
print(type(single_element_tuple))
mixed_tuple = ("Zaki", 1, True)
print(type(mixed_tuple))
# mixed_tuple[0] = "Mr Zaki" This will not work and give assignment error

# mixed_tuple.append(54)  tuple doesnt support append it is only for lists

# del mixed_tuple[2]  Tuple doesn't support item deletion

new_mixed_tuple = mixed_tuple + ("Engineer", "Software")

print(len(new_mixed_tuple))
print((new_mixed_tuple))

name, rank, exists = mixed_tuple
print(name, type(name))
print(rank, type(rank))

#  Dictionary key

network_stats = {
    ("database-01", 70): "High CPU",
    ("database-01", 20): "Low CPU",
    ("database-01", 50): "Moderate CPU",
}

print(network_stats["database-01", 50])

# []  -> These are used for declaring lists
# () -> These are used for declaring tuples
# {} -> These are used for declaring dictionaries

empty_dict = {}
server_info = {
    "hostname": "Database server",
    "ip_address": "10.0.0.1",
    "port": "1234",
    "is_running": "True"
}

print(type(empty_dict))
print(server_info)

print(server_info["ip_address"])
print(server_info.get("ip_adggddress")) # IF key doesn't exists, returns None
print(server_info.get("ip_address")) 
server_info["ip_address"] = "10.2.0.2"
print(server_info.get("ip_adggddress","0.0.8.9")) # IF key doesn't exists, returns default value
print(server_info.get("ip_address")) 

server_info['max_connections'] = 500
print(server_info)

#  Dictonary methods
print(server_info.keys())
print(server_info.values())
print(server_info.items())

del server_info["max_connections"]
print(server_info.items())


if "port" in server_info:
    print(f'Port is defined as {server_info["port"]} in server_info')

infra_config = {
    "production": {
        "web_servers": 5,
        "database_servers": 4,
        "region": "ap-south-1"
    },
    "staging": {
        "web_servers": 1,
        "database_servers": 1,
        "region": "ap-south-1"
    }
}

total_servers = 0
for env_name, env_config in infra_config.items():
    # total_servers += (env_config["web_servers"]) + (env_config["database_servers"]) # similar to the below
    total_servers = total_servers + (env_config["web_servers"]) + (env_config["database_servers"])


print(f"Total servers to be launched {total_servers}")


#  Comparison operators !, = , >, <, >=, <=
a = 20
b = 30 

print( a == b) # False
print( a != b) # True
print( a > b) # False
print( a < b)  # True
print( a >= b) # False
print( a <= b) # True

print("mango" < "banana") # lexicographical comparison

# Logical operators and, or, not

print(a >10 and b < 40)
print(a >10 or b < 20)
print(not (a >10 or b < 20))

# Assignment Operators  =, +=, -=, /=

abc = 5
print(abc)
abc+=6
print(abc)
abc-=1
print(abc)
abc/=2
print(abc)


age = input("Enter your age")
# print(age + 5)
age = int(age) # input() always returns a string so doing the type conversion explicitly
print(age + 5)

if age >=75:
    print("Your a senior citizen")
elif age >=50 and age<=75:
    print("Your an adult")
elif age>=30 and age<=50:
    print("Your in your 30's - 50s")
else:
    print("Your young")

account_details = {
    "balance": "500.98"
}

int_number = 98
string_number = str(int_number)

print(type(int_number))
print(type(string_number))

print(float(account_details["balance"])*2)

abc = 20
defg = 5.0

print(abc*defg)
