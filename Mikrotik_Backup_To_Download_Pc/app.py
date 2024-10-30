from librouteros import connect
from librouteros.query import Key
import datetime

# Device information
mikrotik_ip = '192.168.88.1'
username = 'admin'
password = 'password'

# Create File Name
backup_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"

try:
    # Establish connection to MikroTik device
    api = connect(username=username, password=password, host=mikrotik_ip)

    # Backup command
    api(cmd='/system/backup/save', file_name=backup_filename)
    print(f"Backup created successfully on MikroTik: {backup_filename}")

    # backup download
    backup_file = api(cmd='/file/print', where=Key('name') == backup_filename)
    if backup_file:
        with open(backup_filename, 'wb') as file:
            file.write(backup_file[0]['contents'])
        print(f"Backup downloaded successfully: {backup_filename}")
    else:
        print("Backup file not found on MikroTik.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # close API connection
    if 'api' in locals():
        api.close()
        print("API connection closed.")
