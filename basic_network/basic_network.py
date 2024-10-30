# Define basic IP address information
ip_range = "192.168.1.0/24"
gateway = "192.168.1.1"
interface = "ether1"

# Create simplified MikroTik script
mikrotik_script = f"""
/ip address
add address={gateway}/24 interface={interface}
/ip dhcp-server network
add address={ip_range} gateway={gateway}
/ip pool
add name=dhcp_pool ranges=192.168.1.10-192.168.1.50
/ip dhcp-server
add address-pool=dhcp_pool interface={interface} lease-time=10m name=dhcp1
"""

# Write the script to a file
with open("simple_mikrotik_script.rsc", "w") as file:
    file.write(mikrotik_script)

print("Simplified MikroTik script created.")
