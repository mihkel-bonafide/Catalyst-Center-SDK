#!/usr/bin/env python

from dnacentersdk import api
from objectify import objectify
import json

def list_devices():
    object = objectify()
    devices = object.devices.get_device_list()
    
    # obtain and store device IDs as the variable 'device_ids'
    device_ids = [iterator['id'] for iterator in devices['response']]  
    # obtain and store management IP addys as the variable 'management_ips'
    management_ips = [iterator['managementIpAddress'] for iterator in devices['response']]
    
    with open('devices.json', 'w') as dev_file:
        # create dictionary objects
        device_dict = dict(zip(device_ids, management_ips))   
        json.dump(device_dict, dev_file, indent=4)

    # for testing/debugging
    # import json; print(json.dumps(devices, indent=4))
    # for device in devices["response"]:
    #     print(f"ID: {device['id']}, Management IP: {device['managementIpAddress']}") 

def main():
     list_devices()


if __name__ == "__main__":  
    main()
    