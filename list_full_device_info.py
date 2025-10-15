#!/usr/bin/env python

from dnacentersdk import api
from objectify import objectify
import json

def list_devices():
    object = objectify()
    devices = object.devices.get_device_list()
    
    with open('output.json', 'w') as output_file:
        json.dump(devices, output_file, indent=4)   


    # for testing/debugging
    # import json; print(json.dumps(devices, indent=4))
    # for device in devices["response"]:
    #     print(f"ID: {device['id']}, Management IP: {device['managementIpAddress']}") 

def main():
     list_devices()
      

if __name__ == "__main__":
    main()

    
