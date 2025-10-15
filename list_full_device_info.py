#!/usr/bin/env python

"""
Uses get_device_list() method to obtain and write full device info to output.json file. MG, 10.15.25
"""

from dnacentersdk import api
from objectify import objectify
import json


def list_devices():
    object = objectify()
    devices = object.devices.get_device_list()
    
    with open('output.json', 'w') as output_file:
        json.dump(devices, output_file, indent=4)   


def main():
     list_devices()
      

if __name__ == "__main__":
    main()

    
