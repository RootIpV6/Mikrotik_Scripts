from mikrotik_connect import connect_to_mikrotik

# Device information
mikrotik_ip = "192.168.88.1"
username = "admin"
password = "password"

def enable_romon():
    # Establish connection to MikroTik device
    api, api_pool = connect_to_mikrotik(mikrotik_ip, username, password)
    
    # link check
    if api is None or api_pool is None:
        print("Failed to connect to MikroTik device.")
        return
    
    try:
        # romon access
        romon = api.get_resource('/tool/romon')
        romon_status = romon.get()

        # Result check
        if romon_status and 'enabled' in romon_status[0]:
            # Check if RoMON is enabled and enable it if not
            if not romon_status[0]['enabled']:
                romon.set(id=romon_status[0]['.id'], enabled='yes')
                print("RoMON was disabled, it has been enabled.")
            else:
                print("RoMON is already enabled.")
        else:
            print("Failed to retrieve RoMON status.")
            
    except Exception as e:
        print("An error occurred while checking RoMON status:", e)
        
    finally:
        # Disconnect from MikroTik device
        api_pool.disconnect()
        print("Disconnected from MikroTik device.")

if __name__ == "__main__":
    enable_romon()
