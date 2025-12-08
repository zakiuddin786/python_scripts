from pathlib import Path

base_dir = Path(__file__).resolve().parent # This will get the path where the script is actually present
print(f"Base directory is {base_dir}")

functions_path = base_dir / "functions.py"
log_parser_path = base_dir / "log_parser.py"
test_log_path = base_dir / "test_log.log"

file = open("./functions.py", "r") # not recommended way of dealing with files 

# using path lib to open the file

if functions_path.exists():
    print("path exists reading the file")
    print(functions_path.read_text()) # it has auto open/close 
else:
    print("PAth doesn't exists")

print(file.read())

# without path lib 
# with open("./log_parser.py", "r") as f:
#     content = f.read() # reads the entire file, (be careful when dealing with huge files)
#     print(content)

# with path lib
if log_parser_path.exists():
    with log_parser_path.open("r") as f:
        for line in f:
            print(line, end="") # avoid double new lines


# print("reading line by line")
# # .\\log_parser.py
# with open("./log_parser.py", "r") as f:
#     for line in f: # reading file line by line (memory efficient)
#         print(line)

# print("reading line by line")
# lines = []
# with open("./log_parser.py", "r") as f:
#     lines = f.readlines()
#     print(lines)

lines = []
if log_parser_path.exists():
    with log_parser_path.open("r") as f:
        lines = f.readlines()
        print(lines)
else:
    print("log parser path doesnt exists")

# with open("./test_log.log", "r") as f:
#     errors = []
#     information = []
#     warnings = []

#     for line_num, line in enumerate(f, start=1):
#         if "ERROR" in line:
#             errors.append((line_num, line))
#         elif "WARN" in line: 
#             warnings.append((line_num, line))
#         else:
#             information.append((line_num,line))

# if errors:
#     print("Errors from the file are")
#     for line_num, error_message in errors:
#         print(f" {line_num}: {error_message}")

# if warnings:
#     print("warnigns from the file are")
#     for line_num, warning_message in warnings:
#         print(f" {line_num}: {warning_message}")
        
# if information:
#     print("information from the file are")
#     for line_num, info_message in information:
#         print(f" {line_num}: {info_message}")

if test_log_path.exists():
    with test_log_path.open("r") as f:
        errors = []
        information = []
        warnings = []

        for line_num, line in enumerate(f, start=1):
            if "ERROR" in line:
                errors.append((line_num, line))
            elif "WARN" in line: 
                warnings.append((line_num, line))
            else:
                information.append((line_num,line))

    if errors:
        print("Errors from the file are")
        for line_num, error_message in errors:
            print(f" {line_num}: {error_message}")

    if warnings:
        print("warnigns from the file are")
        for line_num, warning_message in warnings:
            print(f" {line_num}: {warning_message}")
            
    if information:
        print("information from the file are")
        for line_num, info_message in information:
            print(f" {line_num}: {info_message}")


#  Write operations over the file


# with open("./test_log.log", "w") as f: # write mode overwrites the entire file
#     f.write("2025-11-17 17:08:45 [INFO] 987-def-123-123 Written from the file operation")

# with open("./test_log.log", "a") as f: # append mode adds the content at the end of file
#     f.write("2025-11-17 17:08:45 [INFO] 987-def-123-123 Written from the file operation")

# with open ("./test_log.log", "a") as f:
#     f.writelines(lines) # write multiple lines at once