age = 120.00
name = "zaki"
is_a_mentor = True
first_name = "Mohammed"
last_name = "Zakiuddin"

print("Age is ", age, " type is ", type(age))
print("Name is ", name, " type is ", type(name))
name = 11123
print("Name is ", name, " type is ", type(name))

print("mentor is ", is_a_mentor, " type is ", type(is_a_mentor))
# Variable Naming rules:
# 1. Can contain letters (a,z, A-Z), digits(0-9), underscore
# 2. cannot start with digits
# 3. convention : follows a snake_case

# core data types:
# Numeric: int, float, complex
# Text: str
# Sequence: list, tuple, range
# Mapping: dict
# Boolean: bool
# Set: set, frozenset

# =============
# Integer examples
year = 2025
temperature = -15
large_number = 9999999999999999999999999999999999999999999999

print(large_number*2)

a = -10
b = 3
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b)  # multiplication
print(a/b) # division (returns float)
print(a//b) #floor division returns an int
print((a+b-1)//b) # ceil division similarly can use math.ceil()
print(-(-a//b)) # ceil division can work for negative numbers as well
print(a%b) # modulo gives the remainder

#  Server memory calculation

total_servers = 10
memory_per_server_gb = 32
avg_cpu_util=72.3
total_memory_gb = total_servers * memory_per_server_gb

print(" Total memory needed for servers is ",total_memory_gb)
print(f" Total memory needed for {total_servers} servers is {total_memory_gb} GB and avg cpu utilisation is {avg_cpu_util}")

#  Indexing in strings
server_name = "Mohammed   Web_Server   Zaki"
server_name=server_name.strip() # Remove leading/trailing whitespaces
print(server_name[0]) # accessing the first character
print(server_name[1]) # accessing the second character
print(server_name[-1]) # accessing the last character
print(server_name[-2]) # accessing the second last character
# Slicing in strings

print(server_name[0:3]) # printing from index 0 till 3
print(server_name[3:6])
print(server_name[6:])  # printing from index 6 till the end
print(server_name[::3])  # printing every 3rd character

print(server_name.lower())  # converts to lower case
print(server_name.upper())  # converts to upper case

print("Server" in server_name) # True (check if substring exists in a given string)
print(server_name.startswith("Md")) # check if the string starts or ends  using the endswith
print(server_name.endswith("Zaki")) # check if the string starts or ends  using the endswith

print("Server name is ", server_name)
updated_server_name = server_name.replace("Zaki", "Zakiuddin") # replace the word 
print(f"Updated server name is {updated_server_name}")