#!/usr/bin/env python

from dnacentersdk import api
from lehost import host, x, y

def main():
    muh_interface = api.DNACenterAPI(
        base_url=host,
        username=x,
        password=y,
        verify=False, 
    )

    devices = muh_interface.devices.get_device_list()

    # for debugging
    import json; print(json.dumps(devices, indent=4))
    # for device in devices["response"]:
    #     print(f"ID: {device['id']}, Management IP: {device['managementIpAddress']}")        


if __name__ == "__main__":
    main()

    
