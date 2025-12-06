age = 98

if age >=18:
    status="adult"
else:
    status= "minor"

travelled_countries = 48

traveller_status = "Tourist" if travelled_countries >=50 else "Traveller"

print(status)
print(traveller_status)

servers = ["database-1", "database-2", "webserver-1", "webserver-2"]
for server in servers: 
    print(f"sshing into the server {server}")

app_name = "SyncQues"

for char in app_name:
    print(f"{char} . ")


for i in range(10): # range stops at stop -1 
    print(i)


for i in range(5, 10): # range starts from start and goes till stop -1
    print(i)

for i in range(20, 40, 5): # step increments
    print(i)

for i in range (10, 0, -1): # counting backwards
    print(i)

for i in range (len(servers)):
    print(f" server {i} is {servers[i]}")

for index, server in enumerate(servers): # cleaner than range(len(servers))
    print(f" server {index} is {server}")

for ind, server in enumerate(servers, start=2): # cleaner than range(len(servers))
    print(f" server {ind} is {server}")

servers_info = {
    "prod_web_server": {
        "ip": "10.0.2.1",
        "status": "running",
        "ram_gb": 8
        },
     "dev_web_server": {
        "ip": "10.1.2.1",
        "status": "running",
        "ram_gb": 8
        },
    "prod_database": {
        "ip": "10.2.2.1",
        "status": "running",
        "ram_gb": 8
        },
    "dev_database": {
        "ip": "10.3.2.1",
        "status": "stopped",
        "ram_gb": 8
        }
}

for server_name in servers_info:
    print(f"Server {server_name} config is {servers_info[server_name]}")

retry_count = 0
max_retries = 4

while retry_count < max_retries:
    print(f" Attempt {retry_count + 1} trying to connect to server")
    retry_count+=1

#  Loop control statements (break, continue, pass)

for i in range(100): 
    if (i/2 == 10):
        print(f" found the value {i} which gives a reminder of 10 when divided by 2")
        break # Exits the loop immediately
    else:
        print(i)


for i in range(10): 
    if (i%2== 0):
        print(f" skipping {i}")
        continue # Jumps to next iteration
    print(f"processing {i}")

for i in range(10): 
    if (i%2== 0):
        pass # does nothing
    else:
        print(f"starting processing {i}")

square_nums = []
for num in range(10):
    square_nums.append(num*num)

# squared = [ num*num for num in range(20) if (num*num)%2 == 0]
squared = [ num*num if (num*num)%2==0 else -1 for num in range(20)]

#  [Expression for item in iterable ]

print(square_nums)
print(squared)

lines = ["info good", "Error db connection failed.        ", "Error timedout", "waring thread leak"]

errors = [line.strip() for line in lines if "Error" in line]
print(errors)

users = [{"id": 1}, {"id":2}, {"id":3}]

user_ids = [user["id"] for user in users]

print(user_ids)
#  List comphrensions can be useful in 
# 1. cleaning input data
# 2. parsing logs 
# 3. extract json api fields 
# 4. scraping urls from html tags 

# Why list comphrensions:
# 1. python compiles it as optimised C expression internally so it is a bit faster 
# 2. list comprehension creates the entire list at once 