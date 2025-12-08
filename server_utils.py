import os

def check_disk_usage(path="/"):
    """
    write the logic to check the disk usage using the os module 
    and return it in percentage
    """
    return "85%"

def check_memory_usage():
    """
    write the logic to check the memory usage 
    """
    return 76

def get_server_status():
    """
    write the logic and send it
    """

    return {
        "memory_usage": check_memory_usage(),
        "disk_usage": check_disk_usage()
    }