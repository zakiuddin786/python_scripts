log_line = "2025-11-17 17:08:45 [ERROR] 123-def-123-123 Database connection failed on server-007"

notify_admin = False
timestamp_year , timestamp_hour, level, request_id, message = log_line.split(" ", 4)
print(f"timestamp year is {timestamp_year}, hour is {timestamp_hour}, level is {level}, request_id, {request_id}, message is {message}")

if "ERROR" in level:
    server_number = message.split("server-")[1].strip()
    print(f" Error occurred for request_id {request_id} on server number {server_number}")
    notify_admin = True

if notify_admin:
    print('notifying the admin about failure')