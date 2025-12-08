import os

#  get current working directory
current_working_directory = os.getcwd()
print(f"Current working directory is {current_working_directory}")

# check the list of files present inside a directory
files = os.listdir(current_working_directory)
print(f"Files inside {current_working_directory} are {files}")

# check if a file exists in the given directory
file_name="functions.py"
if os.path.exists(f"{current_working_directory}/{file_name}"):
    size = os.path.getsize(f"{current_working_directory}/{file_name}")
    print(f"{file_name} exists with size {size} bytes")

else:
    print("File doesnt exists")