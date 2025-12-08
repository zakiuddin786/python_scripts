import os
import sys

def backup_python_files(directory_name, backup_directory_name):
    """
    This creates a backup of python files present in a given directory

    Args:
        directory_name (str) : The source directory from where the backup is to be made
        backup_directory_name (str) : The destination directory where the backup is to be stored
    
    Return: 
        bool : True if the backup is successful, False otherwise

    Raise: 
        ValueError: If the source doesn't exists
    """
    files = os.listdir(directory_name)
    python_files = [file for file in files if file.endswith(".md")]

    try:
        os.makedirs(backup_directory_name, exist_ok=True) # IF the directory doesnt exists then create it

        for file_name in python_files:
            destination = f"{backup_directory_name}/{file_name}"
            print(f"backing up to {destination}")
            os.system(f"cp {directory_name}/{file_name} {destination}")
    except Exception as e:
        print(f" Backup failed with exception {e}")
        return False
    print("BAckup completed!")
    return True

# command line arguments
print(f"Script name is {sys.argv[0]}")
print(f"Other arguments passsed are {sys.argv[1:]}")
source = sys.argv[1]
destination = sys.argv[2]
print(f"backing up from the source: {source} to destination: {destination}")
backup_python_files(source, destination )

print(f"{sys.platform} {sys.version}")


# Not good way of writing the function 

def process_deployment(service, version, env):
    # validate
    # build
    # test 
    # deploy
    # verify
    # notify
    return True

#  a better way of creating the function which does one thing well

def validate_deployment(service, version, env):
    """
    """
    pass

def build_service(service, version):
    """
    """
    pass

def deploy_service(service, version, env):
    """
    """
    pass


def verify_deployment(service, env):
    """
    """
    pass