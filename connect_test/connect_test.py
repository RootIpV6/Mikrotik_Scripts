from routeros_api import RouterOsApiPool

def connect_to_mikrotik(ip, username, password):
    try:
        api_pool = RouterOsApiPool(ip, username=username, password=password, plaintext_login=True)
        api = api_pool.get_api()
        print("Successfully connected to MikroTik device")
        return api, api_pool
    except Exception as e:
        print("Error occurred during connection:", e)
        return None, None
