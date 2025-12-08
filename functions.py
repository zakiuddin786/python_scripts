def greet_person(name):
    """
    Takes name as an input and returns the greetings
    """
    message = f"Hey hello {name}! How are you doing "
    return message

# name = input("What is your name?")
name = "Zaki" # Global variable
result = greet_person(name)
print(result)

def print_server_status(hostname, status):
    """
    Takes the hostname and status as args and prints the status
    """
    status_local = "Running" # local variable 
    print(f"Status of {hostname} is {status} along with local it is {status_local}")

print_server_status("webserver", "running")
print_server_status("appserver", "stopped")

def caluculate_disk_usage_percentage(used_gb, total_gb):
    """
    Takes the used gb and total gb information and computes the usage percentage
    """
    percentage = (used_gb/total_gb)*100
    print(f" checking to access local status {status_local}")
    return percentage

usage = caluculate_disk_usage_percentage(85,100)

print(f"Disk usage is {usage}%")

#  Function returning multiple values

def get_server_metrics(server_name):
    """
    Gets the cpu, disk and heap usage for give server name
    """
    cpu_usage = 98
    disk_usage = 65
    heap_usage = 76

    return cpu_usage, disk_usage, heap_usage

#  calling the function and unpacking the values
cpu, disk, heap = get_server_metrics("application_server")
print(f"CPU usage is {cpu}, Disk usage is {disk}, Heap usage is {heap}")

server_metrics = get_server_metrics("Database_server")
print(server_metrics)

def deploy_service(service_name, environment, region, version):
    """
    Takes service_name, environment region and version as input and performs the deployment
    """
    print(f"Deploying {service_name} of {environment}, in region {region} with version {version}")
    print(f"Hello {name}") # As name is a global variable we are able to access it in the function

deploy_service("Frontend", "prod", "ap-south-1", "2.2.0")
deploy_service("prod", "ap-south-1", "Frontend", "2.2.0")

#  Keyword arguments and default paraments

def configure_server(server_name, port, enable_ssl=False):
    """
    configure server settings by getting the server_name, port and ssl config
    """

    print(f"Server {server_name} with port {port} has SSL settings turned {enable_ssl}")

configure_server(enable_ssl=True, server_name="databse server", port=9898)
configure_server(server_name="application server", port=1234)

#  Variable length positional arguments *args

def check_service_health(*service_names):
    """
    Takes variable number of services name and performs the health check and demonstrates the 
    variable length positional arguments
    """
    print(f"Finding the health of the provided services {service_names}")

    for index, service_name in enumerate(service_names, start=0):
        print(f"Checking the health of {service_name} at {index}")

check_service_health("application_Server", "database_server")
check_service_health("application_Server")
check_service_health("application_Server", "database_server", "webserver", "computational server")


#  variable lenght keyword arguments passed using **kwargs

def configure_alerts(**alert_settings):
    """
    Takes variable number of alert settings and demonstrates the keyword arguments
    """

    for key, value in alert_settings.items():
        print(f"Key is {key}, Value is {value}")

configure_alerts(email="testing@zaki.com", metric="cpu_utilisation", threshold=85, datapoints=5)
configure_alerts(email="testing@zaki.com", metric="memory_usage", threshold=65, datapoints=3)
configure_alerts(email="testing@zaki.com", metric="cpu_utilisation", threshold=85, datapoints=5, environment="production")
