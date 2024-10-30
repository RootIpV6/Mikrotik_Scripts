from mikrotik_connect import connect_to_mikrotik

# Device information
mikrotik_ip = "192.168.88.1"
username = "admin"
password = "password"

def print_critical_logs():
    # Establish connection to MikroTik device
    api, api_pool = connect_to_mikrotik(mikrotik_ip, username, password)
    
    # Connection check
    if api is None or api_pool is None:
        print("Failed to connect to MikroTik device.")
        return
    
    try:
        # Retrieve critical logs
        log_resource = api.get_resource('/log')
        critical_logs = log_resource.get({'topics': 'critical'})

        # Display critical logs on the screen
        if critical_logs:
            print("Critical Logs:")
            for log in critical_logs:
                # check time and message
                time = log.get('time', 'Unknown time')
                message = log.get('message', 'No message provided')
                print(f"Time: {time}, Message: {message}")
        else:
            print("No critical log entries found.")
            
    except Exception as e:
        print("An error occurred while fetching logs:", e)
        
    finally:
        # Disconnect from MikroTik device if api_pool exists
        if api_pool:
            api_pool.disconnect()
            print("Disconnected from MikroTik device.")

if __name__ == "__main__":
    print_critical_logs()
